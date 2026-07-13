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
    
    def set_socios(self, __tipo_identificacion):
        self.__tipo_identificacion = __tipo_identificacion
        
        
    def get_identificacion(self):
        return self.__identificacion
    
    def set_socios(self, __identificacion):
        self.__identificacion = __identificacion
        
    def get_nacionalidad(self):
        return self.__nacionalidad
    
    def set_socios(self, __nacionalidad):
        self.__nacionalidad = __nacionalidad
        
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
    def mostrar_anio_mayoria_edad(self):
        anio_actual = date.today().year
        anio_nacimiento = anio_actual - self.edad
        anio_mayoria = anio_nacimiento + 18
        
        if self.es_mayor_de_edad():
            print(self.nombre_completo, "es mayor de edad desde el año", anio_mayoria)
        else:
            print(self.nombre_completo, "cumplirá la mayoría de edad en el año", anio_mayoria)
            
persona1 = Persona("Juan Pérez", 25, "DNI", "12345678", "Argentina")
persona1.mostrar_anio_mayoria_edad()