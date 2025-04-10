import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from .styles import apply_styles
from utils.sensor_handler import SensorHandler
from utils.chart_handler import ChartHandler

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.sensor_handler = SensorHandler()
        
        # Aplicar estilos
        apply_styles()
        
        # Crear frame principal con grid de 3x3
        self.main_frame = ttk.Frame(root, padding=20)
        self.main_frame.grid(sticky='nsew')
        
        # Configurar grid
        for i in range(3):
            root.grid_columnconfigure(i, weight=1)
            root.grid_rowconfigure(i, weight=1)
        
        self._create_header()
        self._create_sensor_cards()
        self._create_config_panel()
        self._create_chart()
        
        # Inicializar manejador de gráficas
        self.chart_handler = ChartHandler(self.fig, self.ax)
        
    def _create_header(self):
        header = ttk.Frame(self.main_frame)
        header.grid(row=0, column=0, columnspan=3, sticky='ew')
        
        title = ttk.Label(header, text="Sensor Dashboard", 
                         style='Header.TLabel')
        title.pack(side='left')
        
        status_frame = ttk.Frame(header)
        status_frame.pack(side='right')
        
        self.status_indicator = ttk.Label(status_frame, 
                                        text="●", 
                                        style='Disconnected.TLabel')
        self.status_indicator.pack(side='left')
        
        self.status_label = ttk.Label(status_frame, 
                                     text="Desconectado",
                                     style='Status.TLabel')
        self.status_label.pack(side='left')

    def _create_sensor_cards(self):
        # ... código para crear las tarjetas de sensores
        pass

    def _create_config_panel(self):
        # ... código para crear el panel de configuración
        pass

    def _create_chart(self):
        # ... código para crear la gráfica
        pass
