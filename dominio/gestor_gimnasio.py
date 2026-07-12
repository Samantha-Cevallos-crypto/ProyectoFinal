# Integrantes:
# - Cevallos Mendoza Samantha nikole
# - Laura Fernanda Guillén Vargas
# - Cristhian Isaac Estrella Espinoza
# - Evelyn Noemi Burbano Mora
# -Janeth Maria Verdezoto García

# ─────────────────────────────────────────────
# Clase Adicional 2: GestorGimnasio
# Administra el catálogo de servicios y la lista
# de socios registrados en el gimnasio.
# ─────────────────────────────────────────────
from servicio_gimnasio import ServicioGimnasio
from socio import Socio


class GestorGimnasio:
    """
    Gestor central del gimnasio.
    Administra servicios y socios, y genera reportes globales.
    Aplica encapsulamiento con atributos privados.
    """

    def __init__(self, nombre_gimnasio):
        if not nombre_gimnasio:
            raise ValueError("El nombre del gimnasio no puede estar vacío.")

        self.__nombre_gimnasio = nombre_gimnasio
        self.__servicios: list[ServicioGimnasio] = []   # Catálogo de servicios
        self.__socios:    list[Socio]             = []   # Lista de socios

    # ── Getters ──────────────────────────────
    @property
    def nombre_gimnasio(self):
        return self.__nombre_gimnasio

    @property
    def servicios(self):
        return list(self.__servicios)   # Copia defensiva

    @property
    def socios(self):
        return list(self.__socios)      # Copia defensiva

    # ── Setter ───────────────────────────────
    @nombre_gimnasio.setter
    def nombre_gimnasio(self, nombre):
        if not nombre:
            raise ValueError("El nombre del gimnasio no puede estar vacío.")
        self.__nombre_gimnasio = nombre

    # ── Gestión de servicios ──────────────────
    def agregar_servicio(self, servicio: ServicioGimnasio):
        """Agrega un servicio al catálogo del gimnasio."""
        if not isinstance(servicio, ServicioGimnasio):
            raise TypeError("Solo se pueden agregar instancias de ServicioGimnasio.")
        self.__servicios.append(servicio)
        print(f"  ✔ Servicio '{servicio.nombre}' agregado al catálogo.")

    def eliminar_servicio(self, codigo: str):
        """Elimina un servicio del catálogo por su código."""
        for s in self.__servicios:
            if s.codigo == codigo:
                self.__servicios.remove(s)
                print(f"  ✔ Servicio '{s.nombre}' eliminado del catálogo.")
                return
        print(f"  ✗ No se encontró un servicio con código '{codigo}'.")

    def buscar_servicio(self, codigo: str):
        """Devuelve el servicio con el código indicado, o None si no existe."""
        for s in self.__servicios:
            if s.codigo == codigo:
                return s
        return None

    # ── Gestión de socios ─────────────────────
    def registrar_socio(self, socio: Socio):
        """Registra un nuevo socio en el gimnasio."""
        if not isinstance(socio, Socio):
            raise TypeError("Solo se pueden registrar instancias de Socio.")
        self.__socios.append(socio)
        print(f"  ✔ Socio '{socio.nombre}' registrado correctamente.")

    def dar_de_baja_socio(self, codigo_socio: str):
        """Da de baja a un socio por su código."""
        for s in self.__socios:
            if s.codigo_socio == codigo_socio:
                self.__socios.remove(s)
                print(f"  ✔ Socio '{s.nombre}' dado de baja.")
                return
        print(f"  ✗ No se encontró un socio con código '{codigo_socio}'.")

    # ── Reportes ──────────────────────────────
    def mostrar_catalogo(self):
        """Muestra todos los servicios disponibles."""
        print(f"\n{'═'*45}")
        print(f"  CATÁLOGO DE SERVICIOS — {self.__nombre_gimnasio}")
        print(f"{'═'*45}")
        if not self.__servicios:
            print("  (Sin servicios registrados)")
        for s in self.__servicios:
            s.mostrar_servicio()

    def mostrar_socios(self):
        """Muestra todos los socios registrados."""
        print(f"\n{'═'*45}")
        print(f"  SOCIOS REGISTRADOS — {self.__nombre_gimnasio}")
        print(f"{'═'*45}")
        if not self.__socios:
            print("  (Sin socios registrados)")
        for s in self.__socios:
            s.mostrar_info()

    def calcular_ingresos_totales(self):
        """
        Calcula los ingresos mensuales sumando el precio del servicio
        de cada socio activo → uso de polimorfismo.
        """
        total = sum(s.servicio.precio for s in self.__socios)
        print(f"\n  Ingresos mensuales estimados ({self.__nombre_gimnasio}): "
              f"${total:.2f}")
        return total

    def reporte_precios_anuales(self):
        """
        Genera un reporte con el precio anual de cada servicio del catálogo.
        Llama a calcular_precio_anual() → POLIMORFISMO en acción.
        """
        print(f"\n{'═'*45}")
        print(f"  PRECIOS ANUALES — {self.__nombre_gimnasio}")
        print(f"{'═'*45}")
        for s in self.__servicios:
            anual = s.calcular_precio_anual()   # Polimorfismo
            print(f"  {s.nombre:<25} → ${anual:.2f} / año")

    # ── Representación en texto ───────────────
    def __str__(self):
        return (f"GestorGimnasio("
                f"nombre={self.__nombre_gimnasio}, "
                f"servicios={len(self.__servicios)}, "
                f"socios={len(self.__socios)})")