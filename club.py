from datetime import date

class Club:
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        self.__presidente = presidente
        self.__fecha_fundacion = fecha_fundacion
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        
    def mostrar_info(self):
        print("el nombre de mi club es",self.nombre ,"y es un lugar",self.descripcion,"nos ubicamos en",self.ubicacion, " nuestro presidente es",self.__presidente, "y nos fundamos en",self.__fecha_fundacion)
        
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
        print("La antigüedad del club es de", antiguedad, "años.")
        
club1 = Club("Madrid","chico, de 50 personas max","Malaga, España", "Ronaldo", 1998 )
club1.mostrar_info()
print("¿Es histórico?:", club1.es_historico())
club1.mostrar_antiguedad()
club2 = Club("Malaga","grande, de 250 personas max","Madrid, España", "Messi", 1894 )
club2.mostrar_info()
club2.mostrar_antiguedad()
print("¿Es histórico?:", club2.es_historico())