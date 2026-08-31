from socio import Socio
from datetime import date
from clubCategoria import ClubCategoria

class Administrador(Socio):
    def __init__(self, nombre, usuario, contrasenia, fecha_incripcion, estado, categoria, edad, tipo_identificacion, identificacion, nacionalidad):
        super().__init__(fecha_incripcion, estado, usuario, contrasenia, nombre, edad, tipo_identificacion, identificacion, nacionalidad)
        self.categoria = categoria

    def agregar_socio(self, socio):
        self.categoria.registrar_socio(socio)
        print("Socio", socio.get__usuario(), "agregado al club")

    def listar_socios(self):
        if not self.categoria.get_socios():
            print("No hay socios registrados en el club")
            return

        print("Listado de socios del club:")
        for socio in self.categoria.get_socios():
            print("- Usuario:", socio.get__usuario(), "| Estado:", socio.estado, "| Fecha inscripción:", socio.fecha_incripcion)

    def reactivar_socio(self, socio):
        if socio.estado == "Suspendido":
            socio.estado = "Activo"
            print("El socio", socio.get__usuario(), "ha sido REACTIVADO por el administrador", self.nombre_completo)
        else:
            print("El socio", socio.get__usuario(), "no está suspendido, no requiere reactivación")

    def suspender_socio(self, socio, motivo):
        if socio.estado == "Activo":
            socio.estado = "Suspendido"
            print("El socio", socio.get__usuario(), "ha sido SUSPENDIDO por el administrador", self.nombre_completo, "- Motivo:", motivo)
        else:
            print("El socio", socio.get__usuario(), "ya se encuentra suspendido")
            
    def verificar_acceso(self, usuario, contrasenia):
        if usuario == self.get__usuario() and contrasenia == self.get__contrasenia():
            print("Acceso correcto de admin.")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False
    print("---------------------------------------------------------------------------------------------")  
          
socio1 = Socio(date(2023, 5, 15), "Activo", "el_tio_charly", "clave123", "Carlos Gómez", 40, "DNI", "25333444", "Argentina")
socio2 = Socio(date(2024, 1, 10), "Activo", "marina_trini", "clave456", "Marina Pérez", 28, "DNI", "35555666", "Argentina")

categoria1 = ClubCategoria("Madrid", "lugar amplio de 200 personas", "Malaga, España", "Messi", 2024)
admin1 = Administrador("Ana Gómez", "admin_ana", "adminpass", date(2020, 1, 1), "Activo", categoria1, 35, "DNI", "28777888", "Argentina")
admin1.verificar_acceso("admin_ana", "adminpass")
admin1.agregar_socio(socio1)
admin1.agregar_socio(socio2)
admin1.listar_socios()