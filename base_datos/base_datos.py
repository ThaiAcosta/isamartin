import sqlite3
from modelo.socio import Socio


def conectar(ruta):
    
    conexion = sqlite3.connect(ruta)
    return conexion

def crear_tablas(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo     TEXT NOT NULL,
            edad                INTEGER,
            tipo_identificacion TEXT,
            identificacion      TEXT,
            nacionalidad        TEXT,
            rol                 TEXT DEFAULT 'socio',
            fecha_inscripcion   TEXT,
            estado              TEXT DEFAULT 'Activo',
            usuario             TEXT UNIQUE NOT NULL,
            contrasenia         TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cuotas (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            socio_id            INTEGER NOT NULL,
            estado              TEXT DEFAULT 'Pendiente',
            fecha_vencimiento   TEXT,
            periodo             TEXT
        )          
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXIST clubes (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre              TEXT, 
            descripcion         TEXT, 
            ubicacion           TEXT, 
            presidente          TEXT, 
            fecha_fundacion     TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actividades (
        
        )
    """)
    
    conexion.commit()
    
    
def _objeto_socio(fila):
    (_id, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, rol, fecha_inscripcion, estado, usuario, contrasenia) = fila
    return Socio(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, rol, fecha_inscripcion, estado, usuario, contrasenia)


def guardar_socio(conexion, socio):
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (socio.get_usuario(),))
    if cursor.fetchone() is not None:
        print(f"El socio '{socio.get_usuario()}' ya existe, no se vuelve a insertar.")
        return
    
    cursor.execute("""
        INSERT INTO socios (nombre_completo, edad, tipo_identificacion,
                            identificacion, nacionalidad, rol,
                            fecha_inscripcion,estado, usuario, contrasenia)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        socio.nombre_completo,
        socio.edad,
        socio.get_tipo_identificacion(),
        socio.get_identificacion(),
        socio.get_nacionalidad(),
        socio.rol,
        socio.fecha_inscripcion.isoformat(),
        socio.estado,
        socio.get_usuario(),
        socio.get_contrasenia()
    ))
    conexion.commit()

def guardar_cuota(conexion, usuario, cuota):
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        raise ValueError("El socio no existe")
    
    socio_id = fila[0]
    cursor.execute("""
        INSERT INTO cuotas (socio_id, estado, fecha_vencimiento, periodo)
        VALUES (?, ?, ?, ?)
    """,(
        socio_id,
        cuota.get_estado(),
        cuota.fecha_vencimiento.isoformat(),
        cuota.periodo
    ))
    conexion.commit()

def listar_cuotas_de_socio(conexion, usuario):
    """Devuelve una lista de objetos Cuota para el socio con ese usuario."""
    cursor = conexion.cursor()
    
def buscar_socio_por_usuario(conexion, usuario):
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, apellido FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return None
    return _objeto_socio(fila)
