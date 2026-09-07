from datetime import date

class Persona:
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad ):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.__tipo_identificacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad
        
    def get_tipo_identificacion(self):
            return self.__tipo_identificacion
    
    def set_tipo_identificacion(self, nuevo_tipo_identificacion):
        self.__tipo_identificacion = nuevo_tipo_identificacion
        
    def get_identificacion(self):
        return self.__identificacion
    
    def set_identificacion(self, nueva_identificacion):
        self.__identificacion = nueva_identificacion
        
    def get_nacionalidad(self):
        return self.__nacionalidad
    
    def set_nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad
        
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
    def mostrar_anio_donde_legalizo(self):
        anio_actual = date.today().year
        anio_nacimiento = anio_actual - self.edad
        anio_mayor = anio_nacimiento + 18
        
        if self.es_mayor_de_edad():
            return f'{self.nombre_completo} es mayor de edad desde el año {anio_mayor}'
        else:
            return f'{self.nombre_completo} cumplirá la mayoría de edad en el año {anio_mayor}'
    
    def verificar_identificacion(self):
        if self.__identificacion != "":
            return True
        else:
            return False