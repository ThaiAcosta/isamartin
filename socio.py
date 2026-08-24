from datetime import date

class Socio:
    def __init__(self, fecha_incripcion, estado, usuario, contrasenia ):
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
        print("Clubes del socio:", self.clubes)
        
    def eliminar_club(self, club):
        self.clubes.remove(club)
        print("se ha eliminado el club", club)
         
    def evaluar_suspension(self):
        fecha_actual = date.today()
        dias_transcurridos = (fecha_actual - self.fecha_incripcion).days
        
        if dias_transcurridos > 365:
            self.estado = "Suspendido"
            print("El socio", self.__usuario, "ha sido SUSPENDIDO. Días desde inscripción:", dias_transcurridos)
        else:
            print("El socio", self.__usuario, "continúa ACTIVO. Días desde inscripción:", dias_transcurridos)
            
    def reactivar_socio(self):
        if self.estado == "Suspendido":
            self.estado = "Activo"
            print("El socio", self.__usuario, "ha sido reactivado.")
        else:
            print("El socio no está suspendido.")
            
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
                    print("La cuota",numero, "fue pagada.")
    
    def tiene_deudas(self):
        for cuota in self.cuotas:
            if cuota["estado"] == "Pendiente":
                print("El socio tiene cuotas sin abonar.")
                return True

        print("El socio no tiene deudas.")
        return False
        
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
                if cuota.get("fecha_vencimiento") != None:
                    if fecha_actual > cuota.get("fecha_vencimiento"):
                        print("La cuota número", cuota.get("numero"), "está VENCIDA.")
                    else:
                        print("La cuota número", cuota.get("numero"), "todavía no venció.")
            else:
                print("La cuota número", cuota.get("numero"), "ya está pagada.")
            
    def verificar_acceso(self, usuario, contrasenia):
        if usuario == self.__usuario and contrasenia == self.__contrasenia:
            print("Acceso correcto.")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False
            
fecha_antigua = date(2023, 5, 15)

socio1 = Socio(fecha_antigua, "Activo", "tio charly", "clave123")
socio1.asociar_club("Malaga")
socio1.asociar_club("Madrid")
socio1.mostrar_clubes()
socio1.eliminar_club("Madrid")
socio1.mostrar_clubes()
socio1.generar_cuota(67, "Agosto", date(2026, 8, 10))
socio1.generar_cuota(76, "Septiembre", date(2026, 9, 10))
socio1.pagar_cuota(67)
socio1.tiene_deudas()
socio1.evaluar_suspension()
socio1.mostrar_cuotas_pendientes()
socio1.verificar_vencimiento_cuotas()
socio1.verificar_acceso("tio charly", "clave123")
socio1.reactivar_socio()