from datetime import date
from pathlib import Path
from base_datos.base_datos import conectar, crear_tablas, guardar_socio, guardar_cuota, listar_cuotas_de_socio
from modelo.socio import Socio
from modelo.cuota import Cuota

RUTA = Path(__file__).parent / "club.db"

conexion = conectar(str(RUTA))
crear_tablas(conexion)

# carlos = Socio(
#     "Carlos Ramos ", 30, "DNI", "40322345", "Argentina",
#     "socio", date(2026, 1, 1), "Activo", "carlos", "clave123"
# )
# guardar_socio(conexion, carlos)
# print("Otro socio guardado.")

# isa = Socio(
#     "Isaias Acosta ", 16, "DNI", "55555555", "Argentina",
#     "admin", date(2024, 10, 1), "Activo", "isaa", "zelly"
# )
# guardar_socio(conexion, isa)
# print("Otro socio guardado.")

# martin = Socio(
#     "Martin Laurencio ", 16, "DNI", "22222222", "Argentina",
#     "socio", date(2025, 8, 1), "Activo", "martin", "aitana"
# )
# guardar_socio(conexion, martin)
# print("Otro socio guardado.")

# donella = Socio(
#     "Donella Perez ", 18, "DNI", "66666666", "Argentina",
#     "admin", date(2026, 9, 12), "Activo", "donee", "larubia"
# )
# guardar_socio(conexion, donella)
# print("Otro socio guardado.")

# trini = Socio(
#     "Trinidad Bendita ", 17, "DNI", "33333333", "Argentina",
#     "socio", date(2026, 7, 4), "Activo", "trinii", "676767"
# )
# guardar_socio(conexion, trini)
# print("Otro socio guardado.")

# mari = Socio(
#     "Marina Civiok ", 18, "DNI", "44444444", "Argentina",
#     "socio", date(2026, 4, 7), "Activo", "marii", "isaaaa"
# )
# guardar_socio(conexion, mari)
# print("Otro socio guardado.")

cuota_isa = Cuota(
    "Pendiente", date(2027, 2, 14), "Agosto" 
)
guardar_cuota(conexion, "isaa", cuota_isa)
listar_cuotas_de_socio(conexion, "isaa")
print("cuota guardada")
conexion.close()