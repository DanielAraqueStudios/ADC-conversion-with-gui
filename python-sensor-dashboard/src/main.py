from app.gui.dashboard import Dashboard
from app.serial.connection import SerialConnection
from app.utils.config import DEFAULT_SAMPLING_INTERVAL, DEFAULT_ADC_RESOLUTION

def main():
    # Initialize the serial connection
    serial_connection = SerialConnection()
    serial_connection.open()

    # Create the dashboard GUI
    dashboard = Dashboard(serial_connection, DEFAULT_SAMPLING_INTERVAL, DEFAULT_ADC_RESOLUTION)
    
    # Start the main event loop
    dashboard.run()

if __name__ == "__main__":
    main()