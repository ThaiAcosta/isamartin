from club import Club

class Clublosnoaceptados(Club):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion, actividades):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []
        self.actividades = actividades
        
    def get_socios(self):
        return self.__socios
    
    def set_socios(self, __socios):
        self.__socios = __socios
        