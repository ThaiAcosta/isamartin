from datetime import date
class Cuota:
    def __init__(self,estado,fecha_vencimiento,periodo):
        self.__estado = estado
        self.fecha_vencimiento =fecha_vencimiento
        self.periodo = periodo
        
    def get__estado(self):
        return self.__estado
    
    def set__estado(self, __estado_nuevo):
        self.__estado = __estado_nuevo
        
    def registrar_cuota_pagada(self):
        self.__estado = "Pagada"
        return f'La cuota de {self.periodo} se registro como pagada.'
        
    def verificar_vencimiento(self):
        fecha_actual = date.today()
        if fecha_actual > self.fecha_vencimiento:
            return True
        else:
            return False
        
    def actualizar_estado(self):
        fecha_actual = date.today()

        if fecha_actual > self.fecha_vencimiento:
            self.__estado = "Vencida"
            return f'La cuota de {self.periodo} se encuentra vencida.'
        else:
            return f'La cuota de {self.periodo} sigue {self.__estado}'
            
    def dias_para_vencimiento(self):
        fecha_actual = date.today()
        dias = (self.fecha_vencimiento - fecha_actual).days
        if dias > 0:
            return f'Faltan {dias} dias para el vencimiento de la cuota.'
        elif dias == 0:
            return f'La cuota vence hoy.'
        else:
            return f'La cuota está vencida hace {abs(dias)} dia.'
            
    def renovar_cuota(self, nuevo_periodo, nueva_fecha_vencimiento):
        self.periodo = nuevo_periodo
        self.fecha_vencimiento = nueva_fecha_vencimiento
        self.__estado = "Pendiente"
        return f'La cuota fue renovada para el período {nuevo_periodo}'