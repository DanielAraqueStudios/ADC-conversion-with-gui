import serial
import json
from threading import Thread, Lock
import time

class SensorHandler:
    def __init__(self):
        self.serial_port = None
        self.is_connected = False
        self.data_lock = Lock()
        self.latest_data = {
            'temperature': 0.0,
            'intensity': 0.0
        }
        
    def connect(self, port='COM15', baudrate=9600):
        try:
            self.serial_port = serial.Serial(port, baudrate)
            self.is_connected = True
            Thread(target=self._read_serial, daemon=True).start()
            return True
        except Exception as e:
            print(f"Error connecting: {e}")
            return False
            
    def _read_serial(self):
        while self.is_connected:
            if self.serial_port.in_waiting:
                try:
                    data = self.serial_port.readline().decode().strip()
                    values = json.loads(data)
                    with self.data_lock:
                        self.latest_data = values
                except Exception as e:
                    print(f"Error reading data: {e}")
