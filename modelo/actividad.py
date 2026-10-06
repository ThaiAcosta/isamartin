from datetime import date

class Club:
    def __init__(self, nombre, dia, horario):
        self.nombre = nombre
        self.dia = dia
        self.horario = horario
        
    def info_actividad(self):
        return self.nombre, self.dia, self.horario