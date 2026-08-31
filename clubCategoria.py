from club import Club
from socio import Socio
from datetime import date

class ClubCategoria(Club):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []
        self.actividades = []
        
    def get_socios(self):
        return self.__socios
    
    def set_socios(self, __socios):
        self.__socios = __socios
    print("-------------------------------------------------------------------------------------------------------------")

    def registrar_socio(self, socio):
        self.__socios.append(socio)
                
    def eliminar_socio(self, nombre):
        for socio in self.__socios:
            if socio.nombre_completo == nombre:
                self.__socios.remove(socio)
                print("Socio", nombre, "eliminado")
                return
        print("Socio", nombre, "no encontrado en la lista")
                
    def buscar_socio(self, nombre):
        for socio in self.__socios:
            if socio.nombre_completo == nombre:
                print("Socio encontrado:", socio.nombre_completo)
            return
        print("Socio", nombre, "no encontrado")
        
    def cantidad_socios(self):
        return len(self.__socios)

    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)
        
    def mostrar_actividades(self):
        print(self.actividades)
        
    def eliminar_actividad(self, actividad):
        if actividad in self.actividades:
            self.actividades.remove(actividad)
            print("se ha eliminado la actividad", actividad)
        else:
            print("La actividad", actividad, "no existe")
        
    def porcentaje_activos(self):
        if len(self.__socios) == 0:
            print("No hay socios registrados para calcular el porcentaje")
            return
        activos = 0
        
        for socio in self.__socios:
            if socio.estado == "Activo":
                activos = activos + 1

        porcentaje = (activos * 100) / len(self.__socios)
        porcentaje = round(porcentaje, 2)
        print("El porcentaje de socios activos es:", porcentaje, "%")
        
madrid = ClubCategoria("Madrid", "lugar amplio de 200 personas", "Malaga, España", "Messi", 2024)

isaias = Socio(date(2023, 5, 15), "Activo", "isaias", "clave1", "Isaias Torres", 22, "DNI", "40111222", "Argentina")
martin = Socio(date(2023, 6, 10), "Activo", "martin", "clave2", "Martin López", 27, "DNI", "38222333", "Argentina")
brenda = Socio(date(2023, 7, 20), "Suspendido", "brenda", "clave3", "Brenda Ruiz", 31, "DNI", "34333444", "Argentina")

madrid.registrar_socio(isaias)
madrid.registrar_socio(martin)
madrid.registrar_socio(brenda)

madrid.porcentaje_activos()
madrid.buscar_socio("Isaias Torres")
madrid.agregar_actividad("beber")
madrid.agregar_actividad("bailar")
madrid.mostrar_actividades()
madrid.eliminar_actividad("bailar")
madrid.mostrar_actividades()
madrid.eliminar_socio("Isaias Torres")
