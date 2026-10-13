import sqlite3
from modelo.socio import Socio
from datetime import date
from modelo.cuota import Cuota

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
        CREATE TABLE IF NOT EXISTS clubes (
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
    cursor.execute("SELECT id FROM clubes WHERE nombre = ?", (club.get_nombre(),))
    fila = cursor.fetchone()
    if fila is not None:
        return f'El club {club.get_nombre()} ya existe, no se vuelve a insertar.'
    cursor.execute("""
        INSERT INTO clubes (nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        VALUES (?, ?, ?, ?, ?)
    """, (
        club.get_nombre(),
        club.descripcion,
        club.ubicacion,
        club.get_presidente(),
        club.get_fecha_fundacion()
    ))
    conexion.commit()
    return f'El club {club.get_nombre()} se guardó correctamente.'
    
def guardar_actividad(conexion, actividad):
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM actividades WHERE nombre = ?", (actividad.nombre,))
    fila = cursor.fetchone()
    if fila is not None:
        return f'La actividad {actividad.nombre} ya existe, no se vuelve a insertar.'

    cursor.execute("""
        INSERT INTO actividades (nombre, dia, horario)
        VALUES (?, ?, ?)
    """, (
        actividad.nombre,
        actividad.dia,
        actividad.horario
    ))
    conexion.commit()
    return f'La actividad {actividad.nombre} se guardó correctamente.'
    
def _objeto_socio(fila):
    (_id, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, rol, fecha_inscripcion, estado, usuario, contrasenia) = fila
    return Socio(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, rol, fecha_inscripcion, estado, usuario, contrasenia)

def guardar_socio(conexion, socio):
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (socio.get_usuario(),))
    fila = cursor.fetchone()
    if fila is not None:
        return f'El socio {socio.get_usuario()} ya existe, no se vuelve a insertar.'
    
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
        socio.fecha_inscripcion,
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
    """Devuelve una lista con las cuotas del socio."""
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return []
    socio_id = fila[0]

    cursor.execute("SELECT periodo, estado, fecha_vencimiento FROM cuotas WHERE socio_id = ?", (socio_id,))

    cuotas = []
    fila = cursor.fetchone()
    while fila is not None:
        cuotas.append(fila)
        fila = cursor.fetchone()

    return cuotas
    
def buscar_socio_por_usuario(conexion, usuario):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return None
    return _objeto_socio(fila)

def anotar_socio_actividad(conexion, usuario, nombre_actividad):
    """Anota al socio en la actividad indicada."""
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return "El socio no existe."
    socio_id = fila[0]

    cursor.execute("SELECT id FROM actividades WHERE nombre = ?", (nombre_actividad,))
    fila = cursor.fetchone()
    if fila is None:
        return f"La actividad {nombre_actividad} no existe."
    actividad_id = fila[0]

    cursor.execute("INSERT OR IGNORE INTO socio_actividad (socio_id, actividad_id) VALUES (?, ?)", (socio_id, actividad_id))
    conexion.commit()
    return f"Te anotaste en {nombre_actividad}."

def desanotar_socio_actividad(conexion, usuario, nombre_actividad):
    """Desanota al socio de la actividad indicada."""
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return "El socio no existe."
    socio_id = fila[0]

    cursor.execute("SELECT id FROM actividades WHERE nombre = ?", (nombre_actividad,))
    fila = cursor.fetchone()
    if fila is None:
        return f"La actividad {nombre_actividad} no existe."
    actividad_id = fila[0]

    cursor.execute("SELECT 1 FROM socio_actividad WHERE socio_id = ? AND actividad_id = ?",(socio_id, actividad_id))
    if cursor.fetchone() is None:
        return f"No estabas anotado en {nombre_actividad}."

    cursor.execute("DELETE FROM socio_actividad WHERE socio_id = ? AND actividad_id = ?",(socio_id, actividad_id))
    conexion.commit()
    return f"Te desanotaste de {nombre_actividad}."

def listar_actividades_de_socio(conexion, usuario):
    """Devuelve una lista con los nombres de las actividades del socio."""
    cursor = conexion.cursor()
    cursor_nombres = conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return []
    socio_id = fila[0]

    cursor.execute("SELECT actividad_id FROM socio_actividad WHERE socio_id = ?",(socio_id,))

    actividades = []
    fila = cursor.fetchone()
    while fila is not None:
        cursor_nombres.execute("SELECT nombre FROM actividades WHERE id = ?", (fila[0],))
        fila_actividad = cursor_nombres.fetchone()
        actividades.append(fila_actividad[0])
        fila = cursor.fetchone()

    return actividades

def obtener_club(conexion):
    """Devuelve el objeto Club o None si no hay club cargado."""
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, descripcion, ubicacion, presidente, fecha_fundacion FROM clubes LIMIT 1")
    fila = cursor.fetchone()
    if fila is None:
        return None
    nombre, descripcion, ubicacion, presidente, fecha_fundacion = fila
    from modelo.club import Club
    return Club(nombre, descripcion, ubicacion, presidente, fecha_fundacion)