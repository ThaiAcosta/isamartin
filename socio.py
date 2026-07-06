class Socio:
    def __init__(self, fecha_incripcion, estado, usuario, contrasenia ):
        self.fecha_incripcion = fecha_incripcion
        self.estado = estado
        self.__usuario = usuario
        self.__contrasenia = contrasenia
    
    def get__usuario(self):
        return self.__usuario
    
    def set__usuario(self, __usuario_nuevo):
        self.__usuario = __usuario_nuevo

    def get__contrasenia(self):
        return self.__contrasenia
    
    def set__contrasenia(self, __contrasenia_nueva):
        self.__contrasenia = __contrasenia_nueva