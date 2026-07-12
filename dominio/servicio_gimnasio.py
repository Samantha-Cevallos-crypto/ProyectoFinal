# ─────────────────────────────────────────────
#  Clase Base
# ─────────────────────────────────────────────
class ServicioGimnasio:
    def __init__(self, codigo, nombre, descripcion, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio

    # Getters
    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio(self):
        return self.__precio

    # Setters
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    # Método polimórfico
    def mostrar_servicio(self):
        print("─" * 35)
        print(f"  Código      : {self.__codigo}")
        print(f"  Nombre      : {self.__nombre}")
        print(f"  Descripción : {self.__descripcion}")
        print(f"  Precio      : ${self.__precio:.2f}")
        print("─" * 35)

    def aplicar_descuento(self, porcentaje):
        descuento = self.__precio * (porcentaje / 100)
        self.__precio -= descuento
        print(f"  Descuento del {porcentaje}% aplicado. Nuevo precio: ${self.__precio:.2f}")

    def calcular_precio_anual(self):
        return self.__precio * 12


# ─────────────────────────────────────────────
#  Función que demuestra el polimorfismo
# ─────────────────────────────────────────────
def procesar_servicios(servicios: list):
    print("\n======= CATÁLOGO DE SERVICIOS =======\n")
    for servicio in servicios:
        servicio.mostrar_servicio()          # Polimorfismo: mismo método, distintos objetos

    print("\n======= PRECIO ANUAL POR SERVICIO =======\n")
    for servicio in servicios:
        anual = servicio.calcular_precio_anual()   # Polimorfismo: mismo método en todos
        print(f"  {servicio.nombre:<20} → ${anual:.2f} / año")

    print("\n======= APLICANDO DESCUENTOS =======\n")
    for servicio in servicios:
        servicio.aplicar_descuento(10)       # Polimorfismo: misma llamada, cada objeto reacciona


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":

    s1 = ServicioGimnasio("S001", "Acceso Libre",
                          "Uso ilimitado de máquinas", 30.00)

    s2 = ServicioGimnasio("S002", "Spinning",
                          "Clase de ciclismo indoor", 15.00)

    s3 = ServicioGimnasio("S003", "Personal Training",
                          "Sesión con entrenador", 50.00)

    s4 = ServicioGimnasio("S004", "Membresía Anual",
                          "Acceso completo por 12 meses", 250.00)

    # Lista de objetos de la misma clase → polimorfismo en acción
    catalogo = [s1, s2, s3, s4]
    procesar_servicios(catalogo)