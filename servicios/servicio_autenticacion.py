from base_datos.base_datos import conectar, buscar_socio_por_usuario
from pathlib import Path

RUTA_DB = Path(__file__).parent.parent / "club.db"

def autenticar(usuario, contrasenia):
    if usuario == "" or contrasenia == "":
        return "Completa usuario y contraseña", None

    conexion = conectar(RUTA_DB)
    socio = buscar_socio_por_usuario(conexion, usuario)
    conexion.close()

    if socio is None:
        return "El usuario no existe", None
    if socio.get_contrasenia() != contrasenia:
        return "Contraseña incorrecta", None
    return None, socio