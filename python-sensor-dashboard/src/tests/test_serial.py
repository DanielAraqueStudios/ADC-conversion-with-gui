import unittest
from app.serial.connection import SerialConnection
from app.serial.parser import DataParser

class TestSerialConnection(unittest.TestCase):
    def setUp(self):
        self.serial_connection = SerialConnection(port='COM3', baudrate=9600)

    def test_open_connection(self):
        self.assertTrue(self.serial_connection.open())
    
    def test_close_connection(self):
        self.serial_connection.open()
        self.assertTrue(self.serial_connection.close())

    def test_read_data(self):
        self.serial_connection.open()
        data = self.serial_connection.read()
        self.assertIsNotNone(data)
        self.serial_connection.close()

class TestDataParser(unittest.TestCase):
    def setUp(self):
        self.data_parser = DataParser()

    def test_parse_temperature(self):
        raw_data = "TEMP:25.00"
        parsed_data = self.data_parser.parse(raw_data)
        self.assertEqual(parsed_data['temperature'], 25.00)

    def test_parse_weight(self):
        raw_data = "PESO:70.50"
        parsed_data = self.data_parser.parse(raw_data)
        self.assertEqual(parsed_data['weight'], 70.50)

if __name__ == '__main__':
    unittest.main()