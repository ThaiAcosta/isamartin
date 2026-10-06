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
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre              TEXT,
            dia                 TEXT,
            horario             DATETIME
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socio_actividad (
            socio_id     INTEGER,
            actividad_id INTEGER,
            PRIMARY KEY (socio_id, actividad_id),
            FOREIGN KEY (socio_id) REFERENCES socios(id),
            FOREIGN KEY (actividad_id) REFERENCES actividades(id)
        )
    """)

    conexion.commit()
    
def guardar_club(conexion, club):
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM clubes WHERE nombre = ?", (club,))
    fila = cursor.fetchnone()
    if fila is None:
        return f'El club {club.nombre()} ya existe, no se vuelve a insertar.'
    
    cursor.execute("""
        INSERT INTO clubes (nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        VALUES (?, ?, ?, ?, ?)
    """, (
        club.nombre,
        club.descripcion,
        club.ubicacion,
        club.presidente,
        club.fecha_fundacion
    ))
    
def guardar_actividad(conexion, actividad):
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM clubes WHERE nombre = ?", (actividad,))
    fila = cursor.fetchone()
    if fila is None:
        return f'La actividad {actividad.nombre()} ya existe, no se vuelve a insertar.'
           
    cursor.execute("""
        INSERT INTO actividades (nombre, dia, horario)
        VALUES (?, ?, ?)
    """, (
        actividad.nombre,
        actividad.dia,
        actividad.horario
    ))
    
def _objeto_socio(fila):
    (_id, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, rol, fecha_inscripcion, estado, usuario, contrasenia) = fila
    return Socio(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, rol, fecha_inscripcion, estado, usuario, contrasenia)


def guardar_socio(conexion, socio):
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (socio.get_usuario(),))
    fila = cursor.fetchone()
    if fila is None:
        return f'El socio {socio.get_usuario()} ya existe, no se vuelve a insertar.'
    
    cursor.execute("""
        INSERT INTO socios (nombre_completo, edad, tipo_identificacion,
                            identificacion, nacionalidad, rol,
                            fecha_inscripcion,estado, usuario, contrasenia)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        socio.nombre_completo,
        socio.edad,
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
    
    cursor.execute("""
        INSERT INTO clubes ()
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
    cursor.execute("SELECT * FROM cuotas WHERE usuario = ?", (usuario))
    fila = cursor.fetchnone()
    
def buscar_socio_por_usuario(conexion, usuario):
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, apellido FROM socios WHERE usuario = ?", (usuario))
    fila = cursor.fetchone()
    if fila is None:
        return None
    return _objeto_socio(fila)
