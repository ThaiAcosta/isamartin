import tkinter as tk
from tkinter import messagebox
from servicios.servicio_autenticacion import autenticar

class VentanaLogin:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesión")
        self.ventana.geometry("1200x500")
        self.ventana.resizable(False, False)

        # Nombre del club (obtenido directamente mediante servicio si es dinámico)
        self.titulo = tk.Label(self.ventana, text="Club de Socios", font=("Arial", 24))
        self.titulo.pack(pady=20)

        self.texto_usuario = tk.Label(self.ventana, text="Ingrese su usuario")
        self.texto_usuario.pack()
        self.ingreso_usuario = tk.Entry(self.ventana)
        self.ingreso_usuario.pack()

        self.texto_contrasenia = tk.Label(self.ventana, text="Ingrese su contraseña")
        self.texto_contrasenia.pack()
        self.ingreso_contrasenia = tk.Entry(self.ventana, show="*")
        self.ingreso_contrasenia.pack()

        self.boton = tk.Button(self.ventana, text="Ingresar", bg="green", command=self.ingresar)
        self.boton.pack(pady=10)

    def ingresar(self):
        usuario = self.ingreso_usuario.get()
        contrasenia = self.ingreso_contrasenia.get()

        # Delegamos las validaciones, la consulta a la BD y la lógica de roles al servicio
        error, socio = autenticar(usuario, contrasenia)

        if error is not None:
            messagebox.showerror("Error", error)
            return

        # Ocultar login
        self.ventana.withdraw()

        # Abrir panel según el rol
        if socio.rol == "admin":
            from interfaz.panel_admin import PanelAdmin
            PanelAdmin(self.ventana, socio)
        else:
            from interfaz.panel_socio import PanelSocio
            PanelSocio(self.ventana, socio)
    
    def iniciar(self):
        self.ventana.mainloop()