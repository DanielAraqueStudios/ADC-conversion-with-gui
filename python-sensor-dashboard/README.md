# python-sensor-dashboard

This project implements a graphical user interface (GUI) for monitoring and graphing two analog signals via USART. The application allows users to configure various settings such as ADC resolutions, adjustable sampling intervals, and apply averaging filters for each signal with configurable sample sizes.

## Project Structure

```
python-sensor-dashboard
├── src
│   ├── app
│   │   ├── __init__.py
│   │   ├── gui
│   │   │   ├── __init__.py
│   │   │   ├── dashboard.py
│   │   │   ├── charts.py
│   │   │   └── widgets.py
│   │   ├── serial
│   │   │   ├── __init__.py
│   │   │   ├── connection.py
│   │   │   └── parser.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── config.py
│   │       └── filters.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_serial.py
│   │   └── test_filters.py
│   └── main.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To start the application, run the following command:

```
python src/main.py
```

## Features

- Monitor and graph two analog signals in real-time.
- Adjustable ADC resolutions.
- Configurable sampling intervals through the GUI.
- Averaging filter functionality for each signal with configurable sample sizes.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.