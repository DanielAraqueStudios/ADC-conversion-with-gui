import tkinter as tk
from tkinter import ttk
from .charts import Chart
from .widgets import SensorControlWidget
from ..serial.connection import SerialConnection
from ..utils.config import DEFAULT_SAMPLING_INTERVAL, DEFAULT_ADC_RESOLUTION
from ..utils.filters import AverageFilter

class Dashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Sensor Dashboard")
        self.master.geometry("800x600")

        self.serial_connection = SerialConnection()
        self.sampling_interval = DEFAULT_SAMPLING_INTERVAL
        self.adc_resolution = DEFAULT_ADC_RESOLUTION

        self.chart = Chart(self.master)
        self.sensor_control = SensorControlWidget(self.master, self.update_sampling_interval)

        self.setup_ui()

    def setup_ui(self):
        self.sensor_control.pack(side=tk.TOP, fill=tk.X)
        self.chart.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.update_display()

    def update_display(self):
        # Method to update the display with new data
        data = self.serial_connection.read_data()
        if data:
            self.chart.update_chart(data)

        self.master.after(self.sampling_interval, self.update_display)

    def update_sampling_interval(self, interval):
        self.sampling_interval = interval
        self.update_display()

    def start(self):
        self.serial_connection.open()
        self.update_display()
        self.master.mainloop()

    def stop(self):
        self.serial_connection.close()