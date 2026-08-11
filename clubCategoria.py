from club import Club

class Clublosavengers(Club):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []
        self.actividades = []
        
    def get_socios(self):
        return self.__socios
    
    def set_socios(self, __socios):
        self.__socios = __socios
    print("-------------------------------------------------------------------------------------------------------------")

    def registrar_socio(self, nombre, activo = True):
        socio = {"nombre" : nombre, "activo" : activo}
        self.__socios.append(socio)
        
    def eliminar_socio(self, nombre):
        for socio in self.__socios:
            if socio["nombre"] == nombre:
                self.__socios.remove(socio)
                print("Socio eliminado")
                
    def buscar_socio(self, nombre):
        for socio in self.__socios:
            if socio["nombre"] == nombre:
                print("Socio encontrado:", socio["nombre"])
    
    def cantidad_socios(self):
        return len(self.__socios)

    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)
        
    def mostrar_actividades(self):
        print(self.actividades)
        
    def eliminar_actividad(self, actividad):
        self.actividades.remove(actividad)
        print("se ha eliminado la actividad ", actividad)
        
    def porcentaje_activos(self):
        activos = 0

        for socio in self.__socios:
            if socio["activo"] == True:
                activos = activos + 1

        porcentaje = (activos * 100) / len(self.__socios)

        print("El porcentaje de socios activos es:", porcentaje, "%")
        
madrid = Clublosavengers("Madrid", "lugar amplio de 200 personas", "Malaga, España", "Messi", 2024)

madrid.registrar_socio("isaias", True)
madrid.registrar_socio("martin", True)
madrid.registrar_socio("brenda", False)
madrid.porcentaje_activos()
madrid.buscar_socio("isaias")
madrid.agregar_actividad("beber")
madrid.agregar_actividad("bailar")
madrid.mostrar_actividades()
madrid.eliminar_actividad("bailar")
madrid.mostrar_actividades()
madrid.eliminar_socio("isaias")
