from tkinter import ttk
import tkinter as tk

def apply_styles():
    style = ttk.Style()
    
    # Colores del tema Soft UI
    style.configure('.',
        background='#ffffff',
        foreground='#252f40',
        font=('Inter', 10)
    )
    
    # Estilo para encabezados
    style.configure('Header.TLabel',
        font=('Inter', 24, 'bold'),
        foreground='#252f40'
    )
    
    # Estilos para tarjetas de sensores
    style.configure('SensorCard.TFrame',
        background='#ffffff',
        relief='raised',
        borderwidth=1
    )
    
    # Estilos para indicadores de estado
    style.configure('Connected.TLabel',
        foreground='#2dce89'
    )
    
    style.configure('Disconnected.TLabel',
        foreground='#f5365c'
    )
    
    # Estilos para botones
    style.configure('Primary.TButton',
        background='#5e72e4',
        foreground='#ffffff'
    )
