from tkinter import ttk

def apply_dark_theme(root):
    style = ttk.Style()
    
    # Configure colors
    style.configure('.',
        background='#252f40',
        foreground='#ffffff',
        font=('Segoe UI', 10)
    )
    
    style.configure('Header.TLabel',
        font=('Segoe UI', 24, 'bold'),
        foreground='#ffffff',
        background='#252f40'
    )
    
    style.configure('Control.TFrame',
        background='#2c3e50',
        relief='flat'
    )
    
    style.configure('Modern.TButton',
        font=('Segoe UI', 10),
        background='#007bff',
        foreground='white'
    )
    
    style.configure('Status.TLabel',
        font=('Segoe UI', 9),
        background='#252f40',
        foreground='#adb5bd'
    )

    # Configure root window
    root.configure(bg='#252f40')
