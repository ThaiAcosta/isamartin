from datetime import date

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
        
    def evaluar_suspension(self):
        fecha_actual = date.today()
        dias_transcurridos = (fecha_actual - self.fecha_incripcion).days
        
        if dias_transcurridos > 365:
            self.estado = "Suspendido"
            print("El socio", self.__usuario, "ha sido SUSPENDIDO. Días desde inscripción:", dias_transcurridos)
        else:
            print("El socio", self.__usuario, "continúa ACTIVO. Días desde inscripción:", dias_transcurridos)
            
            
fecha_antigua = date(2020, 5, 15)
socio1 = Socio(fecha_antigua, "Activo", "carlos99", "clave123")
socio1.evaluar_suspension()