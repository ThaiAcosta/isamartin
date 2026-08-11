from socio import Socio
from datetime import date


class Administrador(Socio):
    def __init__(self, nombre, usuario, contrasenia, fecha_incripcion, estado):
        super().__init__(fecha_incripcion, estado, usuario, contrasenia)
        self.nombre = nombre
        self.socios = []  # lista de socios del club

    def agregar_socio(self, socio):
        self.socios.append(socio)
        print("Socio", socio.get__usuario(), "agregado al club")

    def listar_socios(self):
        if not self.socios:
            print("No hay socios registrados en el club")
            return

        print("Listado de socios del club:")
        for socio in self.socios:
            print("- Usuario:", socio.get__usuario(), "| Estado:", socio.estado, "| Fecha inscripción:", socio.fecha_incripcion)

    def reactivar_socio(self, socio):
        if socio.estado == "Suspendido":
            socio.estado = "Activo"
            print("El socio", socio.get__usuario(), "ha sido REACTIVADO por el administrador", self.nombre)
        else:
            print("El socio", socio.get__usuario(), "no está suspendido, no requiere reactivación")

    def suspender_socio(self, socio, motivo):
        if socio.estado == "Activo":
            socio.estado = "Suspendido"
            print("El socio", socio.get__usuario(), "ha sido SUSPENDIDO por el administrador", self.nombre, "- Motivo:", motivo)
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
          
socio1 = Socio(date(2023, 5, 15), "Activo", "el_tio_charly", "clave123")
socio2 = Socio(date(2024, 1, 10), "Activo", "marina_trini", "clave456")

admin1 = Administrador("Ana", "admin_ana", "adminpass", date(2020, 1, 1), "Activo")
admin1.verificar_acceso("admin_ana", "adminpass")
admin1.agregar_socio(socio1)
admin1.agregar_socio(socio2)
admin1.listar_socios()