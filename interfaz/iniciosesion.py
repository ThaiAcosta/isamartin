#trae la librería para hacer ventanas.
import tkinter as tk 
from base_datos.base_datos import conectar, buscar_socio_por_usuario, obtener_club

#guarda el nombre del archivo de la base de datos ,abre la conexión con SQLite y busca el club en la base y devuelve un objeto
RUTA_BD = "club.db"   
conexion = conectar(RUTA_BD)    
club = obtener_club(conexion)  

#tk.Tk() crea la ventana principal, title es el texto de la barra de arriba, geometry("1200x500") define el tamaño de ancho x alto y resizable(False, False) bloquea el cambio de tamaño
ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("1200x500")
ventana.resizable(False, False)

#Label es un texto fijo en pantalla, club.get_nombre usa el getter de la clase Club, pack es lo que coloca el elemento en la ventana y pady agrega espacio vertical
titulo = tk.Label(ventana, text=club.get_nombre(), font=("Arial", 24))
titulo.pack(pady=20)

texto_usuario = tk.Label(ventana, text="Ingrese su usuario")
texto_usuario.pack()
ingreso_usuario = tk.Entry(ventana)
ingreso_usuario.pack()

#Si el usuario escribe 1234, en pantalla ve ****. Con ingreso_contrasenia.get() seguimos recibiendo 1234, el texto verdadero, y por eso se puede comparar con la contraseña guardada.
#Sin el show, la contraseña se vería tal cual la escribís, como en el código del año pasado.
texto_contrasenia = tk.Label(ventana, text="Ingrese su contraseña")
texto_contrasenia.pack()
ingreso_contrasenia = tk.Entry(ventana, show="*")
ingreso_contrasenia.pack()

def ingresar():
    usuario = ingreso_usuario.get()
    contrasenia = ingreso_contrasenia.get()

    #Va a la base de datos, busca un socio con ese usuario y devuelve un objeto Socio o None.
    socio = buscar_socio_por_usuario(conexion, usuario)

    #Si devolvió None, el usuario no existe. Esta comprobación va primero, porque si socio es None no podemos llamar métodos sobre él.
    #config(...) cambia las propiedades de un widget que ya existe. fg es el color del texto.
    if usuario == "" or contrasenia == "":
        mensaje.config(text="Completá usuario y contraseña", fg="red")
    elif socio is None:
        mensaje.config(text="Error: el usuario no existe", fg="red")
    elif not socio.verificar_acceso(usuario, contrasenia):
        mensaje.config(text="Error: contraseña o usuario incorrecto", fg="red")
    elif socio.es_admin():
        mensaje.config(text="Hola " + usuario + ", ingresaste como administrador", fg="green")
    else:
        mensaje.config(text="Hola " + usuario + ", ingresaste como socio", fg="green")

#Button crea el botón. bg es el color de fondo. command=ingresar dice qué función se ejecuta al hacer click. Va sin paréntesis porque le pasamos la función para que la llame tkinter cuando haga falta. Con paréntesis se ejecutaría al crear el botón.
boton = tk.Button(ventana, text="Ingresar", bg="green", command=ingresar)
boton.pack(pady=10)

mensaje = tk.Label(ventana, text="")
mensaje.pack()

ventana.mainloop()
conexion.close()