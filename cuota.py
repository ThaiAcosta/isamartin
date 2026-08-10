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

cuota1 = Cuota("Pendiente", "10/08/2026", "agosto")
cuota1.registrar_cuota_pagada()