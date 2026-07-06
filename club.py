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
    
    def set_presidente(self, fecha_fundacion):
        self.__fecha_fundacion = fecha_fundacion
        
club1 = Club("Madrid","chico, de 50 personas max","Malaga, España", "Ronaldo", 1998 )
club1.mostrar_info()
