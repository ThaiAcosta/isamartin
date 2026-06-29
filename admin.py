class Administrador:
    def __init__(self,nombre,usuario,contrasenia):
        self.nombre = nombre
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        
    def get__usuario(self):
        return self.__usuario
    
    def set__usuario(self, __usuario_nuevo):
        self.__usuario = __usuario_nuevo
        
    def get_contrasenia(self):
        return self.__contrasenia
    
    def set_contrasenia(self, __contrasenia_nueva):
        self.__contrasenia = __contrasenia_nueva