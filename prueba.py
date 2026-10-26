from datetime import date
from pathlib import Path
from base_datos.base_datos import conectar, crear_tablas, guardar_club, guardar_actividad, guardar_socio, guardar_cuota, listar_cuotas_de_socio, buscar_socio_por_usuario, anotar_socio_actividad, desanotar_socio_actividad, listar_actividades_de_socio, obtener_club
from modelo.socio import Socio
from modelo.cuota import Cuota
from modelo.club import Club
from modelo.actividad import Actividad
from modelo.socio import Socio
from servicios.servicio_autenticacion import autenticar

RUTA = Path(__file__).parent / "club.db"

conexion = conectar(str(RUTA))
crear_tablas(conexion)

club = Club("Madrid", "deportivo", "Buenos Aires", "Juan Pérez", 1950)
actividad = Actividad("bailar", "lunes", "18:00")
socio = Socio("Isabel Martín", 25, "DNI", 12345678, "Argentina", "socio", date.today(), "Activo", "isa", "1234")
cuota = Cuota("Pendiente", date(2026, 11, 10), "Noviembre")

guardar_cuota(conexion, "isa", cuota)
print(guardar_club(conexion, club))
print(guardar_actividad(conexion, actividad))
print(guardar_socio(conexion, socio))
print(listar_cuotas_de_socio(conexion, "isa"))
print(buscar_socio_por_usuario(conexion, "isa"))
print(anotar_socio_actividad(conexion, "isa", "bailar"))
print(listar_actividades_de_socio(conexion, "isa"))
print(desanotar_socio_actividad(conexion, "isa", "bailar"))
print(listar_actividades_de_socio(conexion, "isa"))
print(obtener_club(conexion))
autenticar("isaa", "zelly")
print("los atributos de isa son", socio)
