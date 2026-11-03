import tkinter as tk
from tkinter import ttk

class PanelSocio(tk.Toplevel):
    def __init__(self, master, socio):
        super().__init__(master)
        self.title("Panel del Socio - Real Madrid")
        self.geometry("450x350")
        self.resizable(False, False)
        self.socio = socio
        
        # Estilos visuales
        self.configure(bg="#F8F9FA")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background="#F8F9FA", foreground="#1E293B", font=('Segoe UI', 11))
        style.configure('Title.TLabel', font=('Segoe UI', 14, 'bold'), foreground="#002244")
        style.configure('TButton', font=('Segoe UI', 10, 'bold'), background="#C5A059", foreground="white")
        style.map('TButton', background=[('active', '#AA7C11')])

        ttk.Label(self, text=f"¡Bienvenido/a: {socio.nombre_completo}!", style='Title.TLabel').pack(pady=20)
        
        frame_datos = ttk.Frame(self)
        frame_datos.pack(pady=5)
        
        ttk.Label(frame_datos, text=f"👤 Usuario: {socio.get_usuario()}").pack(anchor="w", pady=2)
        ttk.Label(frame_datos, text=f"📌 Estado: {socio.estado}").pack(anchor="w", pady=2)
        ttk.Label(frame_datos, text=f"⭐ Rol: {socio.rol}").pack(anchor="w", pady=2)
        
        ttk.Button(self, text="Cerrar", command=self.destroy).pack(pady=30)
