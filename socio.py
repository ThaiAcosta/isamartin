from datetime import date

class Socio:
    def __init__(self, fecha_incripcion, estado, usuario, contrasenia ):
        self.fecha_incripcion = fecha_incripcion
        self.estado = estado
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        if cuota:
            self.cuotas = cuota
        else:
            self.cuotas = []
    
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
            
    def mostrar_cuotas_pendientes(self):
        cantidad_pendientes = 0
        for cuota in self.cuotas:
            if cuota.get("estado") == "Pendiente":
                cantidad_pendientes += 1
        print("El socio", self.__usuario, "tiene", cantidad_pendientes, "cuota(s) pendiente(s) de pago.")
        return cantidad_pendientes
    
    def verificar_vencimiento_cuotas(self):
        fecha_actual = date.today()
        for cuota in self.cuotas:
            if cuota.get("estado") == "Pendiente":
                if fecha_actual > cuota.get("fecha_vencimiento"):  # NUEVO: uso de "fecha_vencimiento"
                    print("La cuota número", cuota.get("numero"), "está VENCIDA.")
                else:
                    print("La cuota número", cuota.get("numero"), "todavía no venció.")
            else:
                print("La cuota número", cuota.get("numero"), "ya está pagada.")
            
fecha_antigua = date(2023, 5, 15)
cuotas_socio1 = [
    {"numero": 1, "estado": "Pagada"},
    {"numero": 2, "estado": "Pendiente"},
    {"numero": 3, "estado": "Pendiente"},
]
socio1 = Socio(fecha_antigua, "Activo", "tio charly", "clave123")
socio1.evaluar_suspension()
socio1.mostrar_cuotas_pendientes()
socio1.verificar_vencimiento_cuotas()