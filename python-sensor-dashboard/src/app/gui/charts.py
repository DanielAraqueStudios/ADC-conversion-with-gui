import matplotlib.pyplot as plt
import numpy as np

class Chart:
    def __init__(self, title="Analog Signal Chart"):
        self.title = title
        self.fig, self.ax = plt.subplots()
        self.ax.set_title(self.title)
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Signal Value")
        self.x_data = []
        self.y_data = []

    def update_chart(self, new_time, new_value):
        self.x_data.append(new_time)
        self.y_data.append(new_value)
        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, label="Signal")
        self.ax.set_title(self.title)
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Signal Value")
        self.ax.legend()
        plt.draw()
        plt.pause(0.01)

    def configure_chart(self, xlim=None, ylim=None):
        if xlim:
            self.ax.set_xlim(xlim)
        if ylim:
            self.ax.set_ylim(ylim)

    def show(self):
        plt.show()