import tkinter as tk
from tkinter import ttk

class PanelAdmin(tk.Toplevel):
    def __init__(self, master, socio):
        super().__init__(master)
        self.title("Panel del Administrador - Real Madrid")
        self.geometry("400x300")
        self.resizable(False, False)
        self.socio = socio
        
        # Estilos visuales
        self.configure(bg="#F8F9FA")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background="#F8F9FA", foreground="#1E293B", font=('Segoe UI', 11))
        style.configure('Title.TLabel', font=('Segoe UI', 13, 'bold'), foreground="#002244")
        style.configure('TButton', font=('Segoe UI', 10, 'bold'), background="#C5A059", foreground="white")
        style.map('TButton', background=[('active', '#AA7C11')])
        
        ttk.Label(self, text=f"Administrador: {socio.nombre_completo}", style='Title.TLabel').pack(pady=20)
        ttk.Label(self, text="Panel de gestión de socios").pack(pady=5)
        ttk.Button(self, text="Cerrar", command=self.destroy).pack(pady=30)