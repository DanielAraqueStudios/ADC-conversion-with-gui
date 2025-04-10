import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import serial
import threading
import time
from collections import deque
import json
from serial_handler import SerialHandler

class SensorDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Sensor Dashboard")
        self.root.geometry("1200x800")
        
        # Variables para datos
        self.temp_data = deque(maxlen=100)
        self.intensity_data = deque(maxlen=100)
        self.time_labels = deque(maxlen=100)
        
        # Variables de control
        self.is_running = False
        self.plot_paused = False
        self.serial_port = None
        
        # Configuración inicial
        self.temp_sample_time = 1.0
        self.intensity_sample_time = 1.0
        self.temp_filter_enabled = False
        self.intensity_filter_enabled = False
        self.temp_filter_samples = 10
        self.intensity_filter_samples = 10
        self.temp_buffer = []
        self.intensity_buffer = []
        
        self.setup_gui()
        self.setup_plot()
        
    def setup_gui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Control Panel con selección de puerto
        control_frame = ttk.LabelFrame(main_frame, text="Control Panel", padding="5")
        control_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Selector de puerto COM
        ttk.Label(control_frame, text="Port:").grid(row=0, column=0)
        self.port_selector = ttk.Combobox(control_frame, values=SerialHandler.get_available_ports())
        self.port_selector.grid(row=0, column=1, padx=5)
        if self.port_selector['values']:
            self.port_selector.set(self.port_selector['values'][0])
        
        self.conn_button = ttk.Button(control_frame, text="Connect", command=self.toggle_connection)
        self.conn_button.grid(row=0, column=2, padx=5)
        
        self.status_label = ttk.Label(control_frame, text="Disconnected")
        self.status_label.grid(row=0, column=3)
        
        # Configuración de sensores
        sensor_config = ttk.LabelFrame(main_frame, text="Sensor Configuration", padding="5")
        sensor_config.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Tiempo de muestreo
        ttk.Label(sensor_config, text="Time Unit:").grid(row=0, column=0)
        self.time_unit = ttk.Combobox(sensor_config, values=['ms', 's', 'min'])
        self.time_unit.set('s')
        self.time_unit.grid(row=0, column=1)
        
        # Temperatura
        ttk.Label(sensor_config, text="Temperature Sample Time:").grid(row=1, column=0)
        self.temp_time = ttk.Entry(sensor_config)
        self.temp_time.insert(0, "1")
        self.temp_time.grid(row=1, column=1)
        
        self.temp_filter_var = tk.BooleanVar()
        ttk.Checkbutton(sensor_config, text="Temperature Filter", 
                       variable=self.temp_filter_var,
                       command=self.toggle_temp_filter).grid(row=2, column=0)
        
        self.temp_samples = ttk.Combobox(sensor_config, 
                                       values=['3','5','10','15','20','30'])
        self.temp_samples.set('10')
        self.temp_samples.grid(row=2, column=1)
        self.temp_samples.state(['disabled'])
        
        # Intensidad
        ttk.Label(sensor_config, text="Intensity Sample Time:").grid(row=3, column=0)
        self.intensity_time = ttk.Entry(sensor_config)
        self.intensity_time.insert(0, "1")
        self.intensity_time.grid(row=3, column=1)
        
        self.intensity_filter_var = tk.BooleanVar()
        ttk.Checkbutton(sensor_config, text="Intensity Filter",
                       variable=self.intensity_filter_var,
                       command=self.toggle_intensity_filter).grid(row=4, column=0)
        
        self.intensity_samples = ttk.Combobox(sensor_config,
                                            values=['3','5','10','15','20','30'])
        self.intensity_samples.set('10')
        self.intensity_samples.grid(row=4, column=1)
        self.intensity_samples.state(['disabled'])
        
    def setup_plot(self):
        # Configuración de la gráfica
        self.fig = Figure(figsize=(10, 6))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=2)
        
        self.temp_line, = self.ax.plot([], [], 'r-', label='Temperature')
        self.intensity_line, = self.ax.plot([], [], 'b-', label='Intensity')
        self.ax.legend()
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Value')
        self.ax.grid(True)

    def toggle_connection(self):
        if not self.is_running:
            try:
                selected_port = self.port_selector.get()
                if not selected_port:
                    tk.messagebox.showerror("Error", "Please select a COM port")
                    return
                    
                self.serial_port = serial.Serial(selected_port, 115200)
                self.is_running = True
                self.conn_button.config(text="Disconnect")
                self.status_label.config(text="Connected")
                self.port_selector.state(['disabled'])  # Deshabilitar selección mientras está conectado
                
                # Iniciar thread de lectura
                self.read_thread = threading.Thread(target=self.read_serial)
                self.read_thread.daemon = True
                self.read_thread.start()
                
                # Iniciar actualización de gráfica
                self.update_plot()
                
            except Exception as e:
                tk.messagebox.showerror("Error", f"Could not connect: {str(e)}")
        else:
            self.is_running = False
            if self.serial_port:
                self.serial_port.close()
            self.conn_button.config(text="Connect")
            self.status_label.config(text="Disconnected")
            self.port_selector.state(['!disabled'])  # Rehabilitar selección de puerto

    def read_serial(self):
        while self.is_running:
            try:
                if self.serial_port.in_waiting:
                    line = self.serial_port.readline().decode('utf-8').strip()
                    data = json.loads(line)
                    
                    # Aplicar filtros si están habilitados
                    if self.temp_filter_enabled:
                        self.temp_buffer.append(data['temp'])
                        if len(self.temp_buffer) >= self.temp_filter_samples:
                            data['temp'] = sum(self.temp_buffer)/len(self.temp_buffer)
                            self.temp_buffer = []
                            
                    if self.intensity_filter_enabled:
                        self.intensity_buffer.append(data['intensity'])
                        if len(self.intensity_buffer) >= self.intensity_filter_samples:
                            data['intensity'] = sum(self.intensity_buffer)/len(self.intensity_buffer)
                            self.intensity_buffer = []
                    
                    # Agregar datos a las colas
                    self.temp_data.append(data['temp'])
                    self.intensity_data.append(data['intensity'])
                    self.time_labels.append(time.strftime('%H:%M:%S'))
                    
            except Exception as e:
                print(f"Error reading serial: {e}")
                break

    def update_plot(self):
        if not self.plot_paused and self.is_running:
            self.temp_line.set_data(range(len(self.temp_data)), list(self.temp_data))
            self.intensity_line.set_data(range(len(self.intensity_data)), 
                                       list(self.intensity_data))
            
            self.ax.relim()
            self.ax.autoscale_view()
            self.canvas.draw()
            
        self.root.after(100, self.update_plot)

    def toggle_temp_filter(self):
        self.temp_filter_enabled = self.temp_filter_var.get()
        if self.temp_filter_enabled:
            self.temp_samples.state(['!disabled'])
        else:
            self.temp_samples.state(['disabled'])

    def toggle_intensity_filter(self):
        self.intensity_filter_enabled = self.intensity_filter_var.get()
        if self.intensity_filter_enabled:
            self.intensity_samples.state(['!disabled'])
        else:
            self.intensity_samples.state(['disabled'])

if __name__ == "__main__":
    root = tk.Tk()
    app = SensorDashboard(root)
    root.mainloop()
