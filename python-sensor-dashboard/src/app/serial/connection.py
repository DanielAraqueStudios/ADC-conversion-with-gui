import serial

class SerialConnection:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial = None

    def open(self):
        if self.serial is None:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=1)

    def close(self):
        if self.serial is not None:
            self.serial.close()
            self.serial = None

    def read_data(self):
        if self.serial is not None and self.serial.is_open:
            return self.serial.readline().decode('utf-8').strip()
        return None