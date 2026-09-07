from datetime import date

class Club:
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        self.__presidente = presidente
        self.__fecha_fundacion = fecha_fundacion
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        
    def mostrar_info(self):
        return f'el nombre de mi club es {self.nombre} y es un lugar {self.descripcion} nos ubicamos en {self.ubicacion} nuestro presidente es {self.__presidente} y nos fundamos en {self.__fecha_fundacion}'  
        
    def get_presidente(self):
        return self.__presidente
    
    def set_presidente(self, presidente):
        self.__presidente = presidente
        
    def get_fecha_fundacion(self):
        return self.__fecha_fundacion
    
    def set_fecha_fundacion(self, fecha_fundacion):
        self.__fecha_fundacion = fecha_fundacion
        
    def es_historico(self):
        anio_actual = date.today().year
        antiguedad = anio_actual - self.__fecha_fundacion
        
        if antiguedad > 50:
            return True
        else:
            return False
        
    def mostrar_antiguedad(self):
        anio_actual = date.today().year
        antiguedad = anio_actual - self.__fecha_fundacion
        return f'La antigüedad del club es de {antiguedad} años.'