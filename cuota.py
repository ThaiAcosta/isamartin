class Cuota:
    def __init__(self,estado,fecha_vencimiento,periodo):
        self.__estado = estado
        self.fecha_vencimiento =fecha_vencimiento
        self.periodo = periodo
        
    def get__estado(self):
        return self.__estado
    
    def set__estado(self, __estado_nuevo):
        self.__estado = __estado_nuevo