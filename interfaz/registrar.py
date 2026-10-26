import tkinter as tk
from datetime import date
from base_datos.base_datos import conectar, guardar_socio, obtener_club
from modelo.socio import Socio

RUTA_BD = "club.db"
conexion = conectar(RUTA_BD)
club = obtener_club(conexion)

ventana = tk.Tk()
ventana.title("Registro")
ventana.geometry("1200x700")
ventana.resizable(False, False)

titulo = tk.Label(ventana, text=club.get_nombre(), font=("Arial", 24))
titulo.pack(pady=20)

texto_nombre = tk.Label(ventana, text="Ingrese su nombre completo")
texto_nombre.pack()
ingreso_nombre = tk.Entry(ventana)
ingreso_nombre.pack()

texto_edad = tk.Label(ventana, text="Ingrese su edad")
texto_edad.pack()
ingreso_edad = tk.Entry(ventana)
ingreso_edad.pack()

texto_tipo = tk.Label(ventana, text="Ingrese su tipo de identificación (DNI, pasaporte...)")
texto_tipo.pack()
ingreso_tipo = tk.Entry(ventana)
ingreso_tipo.pack()

texto_identificacion = tk.Label(ventana, text="Ingrese su número de identificación")
texto_identificacion.pack()
ingreso_identificacion = tk.Entry(ventana)
ingreso_identificacion.pack()

texto_nacionalidad = tk.Label(ventana, text="Ingrese su nacionalidad")
texto_nacionalidad.pack()
ingreso_nacionalidad = tk.Entry(ventana)
ingreso_nacionalidad.pack()

texto_usuario = tk.Label(ventana, text="Ingrese su usuario")
texto_usuario.pack()
ingreso_usuario = tk.Entry(ventana)
ingreso_usuario.pack()

texto_contrasenia = tk.Label(ventana, text="Ingrese su contraseña")
texto_contrasenia.pack()
ingreso_contrasenia = tk.Entry(ventana, show="*")
ingreso_contrasenia.pack()

texto_repetir = tk.Label(ventana, text="Repita su contraseña")
texto_repetir.pack()
ingreso_repetir = tk.Entry(ventana, show="*")
ingreso_repetir.pack()


def registrarse():
    nombre = ingreso_nombre.get()
    edad = ingreso_edad.get()
    tipo = ingreso_tipo.get()
    identificacion = ingreso_identificacion.get()
    nacionalidad = ingreso_nacionalidad.get()
    usuario = ingreso_usuario.get()
    contrasenia = ingreso_contrasenia.get()
    repetir = ingreso_repetir.get()

    if nombre == "" or edad == "" or tipo == "" or identificacion == "" or nacionalidad == "" or usuario == "" or contrasenia == "":
        mensaje.config(text="Completá todos los campos", fg="red")
    elif not edad.isdigit():
        mensaje.config(text="Error: la edad tiene que ser un número", fg="red")
    elif contrasenia != repetir:
        mensaje.config(text="Error: las contraseñas no coinciden", fg="red")
    else:
        fecha = str(date.today())
        socio = Socio(nombre, int(edad), tipo, identificacion, nacionalidad, "socio", fecha, "activo", usuario, contrasenia)
        resultado = guardar_socio(conexion, socio)

        if resultado is None:
            mensaje.config(text="Socio registrado correctamente", fg="green")
        else:
            mensaje.config(text="Error: ese usuario ya existe", fg="red")


boton = tk.Button(ventana, text="Registrarse", bg="green", command=registrarse)
boton.pack(pady=10)

mensaje = tk.Label(ventana, text="")
mensaje.pack()

ventana.mainloop()
conexion.close()