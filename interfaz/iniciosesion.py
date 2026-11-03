import tkinter as tk
from tkinter import messagebox
from servicios.servicio_autenticacion import autenticar  # Tus imports intactos

class VentanaLogin:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Club de Socios - Real Madrid")
        self.geometry = "1200x500"
        self.ventana.geometry(self.geometry)
        self.ventana.resizable(False, False)
        
        # --- ESTILO VISUAL REAL MADRID (Sin tocar lógica) ---
        self.ventana.configure(bg="#F8F9FA")
        
        self.titulo = tk.Label(
            self.ventana, 
            text="⚪ CLUB DE SOCIOS - REAL MADRID ⚪", 
            font=("Segoe UI", 20, "bold"),
            fg="#002244", 
            bg="#F8F9FA"
        )
        self.titulo.pack(pady=30)

        self.texto_usuario = tk.Label(self.ventana, text="Ingrese su usuario", bg="#F8F9FA", fg="#475569")
        self.texto_usuario.pack(pady=2)
        self.ingreso_usuario = tk.Entry(self.ventana, font=("Segoe UI", 11), bd=2, relief="solid")
        self.ingreso_usuario.pack(pady=5, ipadx=10, ipady=3)

        self.texto_contrasenia = tk.Label(self.ventana, text="Ingrese su contraseña", bg="#F8F9FA", fg="#475569")
        self.texto_contrasenia.pack(pady=2)
        self.ingreso_contrasenia = tk.Entry(self.ventana, show="*", font=("Segoe UI", 11), bd=2, relief="solid")
        self.ingreso_contrasenia.pack(pady=5, ipadx=10, ipady=3)

        # Botón estilizado en tonos dorados del club
        self.boton = tk.Button(
            self.ventana, 
            text="Ingresar", 
            bg="#C5A059",           # Dorado Real Madrid
            fg="white", 
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            activebackground="#AA7C11",
            activeforeground="white",
            cursor="hand2",
            padx=20, pady=5,
            command=self.ingresar
        )
        self.boton.pack(pady=20)

    def ingresar(self):
        usuario = self.ingreso_usuario.get()
        contrasenia = self.ingreso_contrasenia.get()

        # Tu lógica original intacta
        error, socio = autenticar(usuario, contrasenia)

        if error is not None:
            messagebox.showerror("Error", error)
            return

        self.ventana.withdraw()

        if socio.rol == "admin":
            from interfaz.panel_admin import PanelAdmin
            PanelAdmin(self.ventana, socio)
        else:
            from interfaz.panel_socio import PanelSocio
            PanelSocio(self.ventana, socio)
    
    def iniciar(self):
        self.ventana.mainloop()