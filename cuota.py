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
        print("La cuota de", self.periodo, "se registro como pagada.")
        
    def verificar_vencimiento(self):
        fecha_actual = date.today()
        if fecha_actual > self.fecha_vencimiento:
            print("La cuota de", self.periodo, "está vencida.")
            return True
        else:
            print("La cuota de", self.periodo, "todavía no está vencida.")
            return False
        
    def actualizar_estado(self):
        fecha_actual = date.today()

        if fecha_actual > self.fecha_vencimiento:
            self.__estado = "Vencida"
            print("La cuota de", self.periodo, "se encuentra vencida.")
        else:
            print("La cuota de", self.periodo, "sigue", self.__estado)
            
    def dias_para_vencimiento(self):
        fecha_actual = date.today()
        dias = (self.fecha_vencimiento - fecha_actual).days
        if dias > 0:
            print("Faltan", dias, "dias para el vencimiento de la cuota.")
        elif dias == 0:
            print("La cuota vence hoy.")
        else:
            print("La cuota está vencida hace", abs(dias), "dia.")
            
    def renovar_cuota(self, nuevo_periodo, nueva_fecha_vencimiento):
        self.periodo = nuevo_periodo
        self.fecha_vencimiento = nueva_fecha_vencimiento
        self.__estado = "Pendiente"
        print("La cuota fue renovada para el período", nuevo_periodo)

cuota1 = Cuota("Pendiente", date(2026, 8, 10), "agosto")
cuota1.registrar_cuota_pagada()
cuota1.verificar_vencimiento()
cuota1.dias_para_vencimiento()
cuota1.renovar_cuota("septiembre", date(2026, 9, 10))
cuota1.actualizar_estado()