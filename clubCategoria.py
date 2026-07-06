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
    
    def registrar_socio(self, socio):
        self.__socios.append(socio)
    
    def cantidad_socios(self):
        return len(self.__socios)

    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)
        
    def mostrar_actividades(self):
        print(self.actividades)
        
madrid = Clublosavengers("Madrid", "lugar amplio de 200 personas", "Malaga, España", "Messi", 2024)

madrid.registrar_socio("isaias")
madrid.cantidad_socios()
madrid.agregar_actividad("bailar")
madrid.agregar_actividad("beber")
madrid.mostrar_actividades()
