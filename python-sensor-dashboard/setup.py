from setuptools import setup, find_packages

setup(
    name='python-sensor-dashboard',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A GUI application for monitoring and graphing analog signals via USART.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'PyQt5',  # or any other GUI framework you choose
        'pyserial',  # for serial communication
        'matplotlib',  # for plotting graphs
        'numpy',  # for numerical operations
    ],
    entry_points={
        'console_scripts': [
            'sensor-dashboard=main:main',  # Adjust according to your main function
        ],
    },
)