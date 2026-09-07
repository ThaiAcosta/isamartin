from datetime import date
from persona import Persona

class Socio(Persona):
    def __init__(self, fecha_incripcion, estado, usuario, contrasenia, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):
        super().__init__(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad)
        self.fecha_incripcion = fecha_incripcion
        self.estado = estado
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        self.cuotas = []
        self.clubes = []
    
    def get__usuario(self):
        return self.__usuario
    
    def set__usuario(self, __usuario_nuevo):
        self.__usuario = __usuario_nuevo

    def get__contrasenia(self):
        return self.__contrasenia
    
    def set__contrasenia(self, __contrasenia_nueva):
        self.__contrasenia = __contrasenia_nueva
        
    def asociar_club(self, club):
        self.clubes.append(club)
        
    def mostrar_clubes(self):
        return f'Clubes del socio: {self.clubes}'
        
    def eliminar_club(self, club):
        if club in self.clubes:
            self.clubes.remove(club)
            return f'se ha eliminado el club {club}'
        else:
            return f'El club {club} no está asociado a este socio'
         
    def evaluar_suspension(self):
        fecha_actual = date.today()
        dias_transcurridos = (fecha_actual - self.fecha_incripcion).days
        
        if dias_transcurridos > 365:
            self.estado = "Suspendido"
            return f'El socio {self.__usuario} ha sido SUSPENDIDO. Días desde inscripción: {dias_transcurridos}'
        else:
            return f'El socio {self.__usuario} continúa ACTIVO. Días desde inscripción: {dias_transcurridos}'
            
    def reactivar_socio(self):
        if self.estado == "Suspendido":
            self.estado = "Activo"
            return f'El socio {self.__usuario} ha sido reactivado.'
        else:
            return f'El socio no está suspendido.'
            
    def generar_cuota(self, numero, periodo, fecha_vencimiento):
        cuota = {
            "numero": numero,
            "periodo": periodo,
            "estado": "Pendiente",
            "fecha_vencimiento": fecha_vencimiento
        }
        self.cuotas.append(cuota)
        
    def pagar_cuota(self, numero):
        for cuota in self.cuotas:
            if cuota["numero"] == numero:
                if cuota["estado"] == "Pendiente":
                    cuota["estado"] = "Pagada"
                    return f'La cuota {numero} fue pagada.'
                else:
                    return f'La cuota {numero} ya estaba pagada.'
        return f' La cuota {numero} no existe.'
    
    def tiene_deudas(self):
        for cuota in self.cuotas:
            if cuota["estado"] == "Pendiente":
                return True
            else:
                return False
        
    def mostrar_cuotas_pendientes(self):
        cantidad_pendientes = 0
        for cuota in self.cuotas:
            if cuota.get("estado") == "Pendiente":
                cantidad_pendientes += 1
        return cantidad_pendientes
    
    def verificar_vencimiento_cuotas(self):
        fecha_actual = date.today()
        for cuota in self.cuotas:
            if cuota.get("estado") == "Pendiente":
                if cuota.get("fecha_vencimiento") != None:
                    if fecha_actual > cuota.get("fecha_vencimiento"):
                        return f'La cuota número {cuota.get("numero")} está VENCIDA.'
                    else:
                        return f'La cuota número {cuota.get("numero")} todavía no venció.'
            else:
                return f'La cuota número {cuota.get("numero")} ya está pagada'
            
    def verificar_acceso(self, usuario, contrasenia):
        if usuario == self.__usuario and contrasenia == self.__contrasenia:
            return True
        else:
            return False