import serial
import serial.tools.list_ports
import json
import time

class SerialHandler:
    def __init__(self, port=None, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial = None
    
    @staticmethod
    def get_available_ports():
        return [port.device for port in serial.tools.list_ports.comports()]
        
    def connect(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate)
            return True
        except Exception as e:
            print(f"Error connecting to serial port: {e}")
            return False
            
    def disconnect(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
            
    def send_config(self, config):
        if self.serial and self.serial.is_open:
            try:
                config_json = json.dumps(config)
                self.serial.write(config_json.encode() + b'\n')
                return True
            except Exception as e:
                print(f"Error sending configuration: {e}")
                return False
        return False
        
    def read_data(self):
        if self.serial and self.serial.is_open:
            try:
                if self.serial.in_waiting:
                    line = self.serial.readline().decode('utf-8').strip()
                    return json.loads(line)
            except Exception as e:
                print(f"Error reading data: {e}")
        return None
