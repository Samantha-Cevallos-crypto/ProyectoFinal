# Integrantes:
# - Cevallos Mendoza Samantha nikole
# - Laura Fernanda Guillén Vargas
# - Cristhian Isaac Estrella Espinoza
# - Evelyn Noemi Burbano Mora
# -Janeth Maria Verdezoto García

# ─────────────────────────────────────────────
# Clase Hija 2: EntrenamientoPersonalizado
# Hereda de ServicioGimnasio.
# Añade entrenador, sesiones y nivel, y sobreescribe
# métodos para aplicar polimorfismo.
# ─────────────────────────────────────────────
from servicio_gimnasio import ServicioGimnasio


class EntrenamientoPersonalizado(ServicioGimnasio):
    """
    Representa un plan de entrenamiento personalizado con entrenador asignado,
    número de sesiones mensuales y nivel de dificultad.
    """

    NIVELES_VALIDOS = ("Básico", "Intermedio", "Avanzado")

    def __init__(self, codigo, nombre, descripcion, precio,
                 entrenador, sesiones_por_mes, nivel):
        # Herencia: inicializa atributos de la clase padre
        super().__init__(codigo, nombre, descripcion, precio)

        # Validaciones antes de asignar
        if not entrenador:
            raise ValueError("El nombre del entrenador no puede estar vacío.")
        if sesiones_por_mes <= 0:
            raise ValueError("Las sesiones por mes deben ser mayor a 0.")
        if nivel not in self.NIVELES_VALIDOS:
            raise ValueError(f"Nivel inválido. Opciones: {self.NIVELES_VALIDOS}")

        # Atributos propios encapsulados
        self.__entrenador       = entrenador
        self.__sesiones_por_mes = sesiones_por_mes
        self.__nivel            = nivel

    # ── Getters ──────────────────────────────
    @property
    def entrenador(self):
        return self.__entrenador

    @property
    def sesiones_por_mes(self):
        return self.__sesiones_por_mes

    @property
    def nivel(self):
        return self.__nivel

    # ── Setters con validación ────────────────
    @entrenador.setter
    def entrenador(self, entrenador):
        if not entrenador:
            raise ValueError("El nombre del entrenador no puede estar vacío.")
        self.__entrenador = entrenador

    @sesiones_por_mes.setter
    def sesiones_por_mes(self, sesiones):
        if sesiones <= 0:
            raise ValueError("Las sesiones por mes deben ser mayor a 0.")
        self.__sesiones_por_mes = sesiones

    @nivel.setter
    def nivel(self, nivel):
        if nivel not in self.NIVELES_VALIDOS:
            raise ValueError(f"Nivel inválido. Opciones: {self.NIVELES_VALIDOS}")
        self.__nivel = nivel

    # ── Método propio ─────────────────────────
    def precio_por_sesion(self):
        """Calcula el precio unitario por sesión."""
        return self.precio / self.__sesiones_por_mes

    # ── POLIMORFISMO: sobreescritura de mostrar_servicio ──
    def mostrar_servicio(self):
        """
        Sobreescribe el método de la clase base para mostrar
        también los atributos exclusivos del entrenamiento personalizado.
        """
        print("─" * 40)
        print(f"  Código        : {self.codigo}")
        print(f"  Nombre        : {self.nombre}")
        print(f"  Descripción   : {self.descripcion}")
        print(f"  Precio/mes    : ${self.precio:.2f}")
        print(f"  Entrenador    : {self.__entrenador}")
        print(f"  Sesiones/mes  : {self.__sesiones_por_mes}")
        print(f"  Precio/sesión : ${self.precio_por_sesion():.2f}")
        print(f"  Nivel         : {self.__nivel}")
        print("─" * 40)

    # ── POLIMORFISMO: sobreescritura de calcular_precio_anual ──
    def calcular_precio_anual(self):
        """
        Sobreescribe el método base: precio anual con 5% de descuento
        por fidelidad al contratar el año completo.
        """
        precio_bruto         = self.precio * 12
        descuento_fidelidad  = precio_bruto * 0.05   # 5% por contrato anual
        precio_final         = precio_bruto - descuento_fidelidad
        return precio_final

    # ── Representación en texto ───────────────
    def __str__(self):
        return (f"EntrenamientoPersonalizado("
                f"codigo={self.codigo}, "
                f"nombre={self.nombre}, "
                f"precio=${self.precio:.2f}, "
                f"entrenador={self.__entrenador}, "
                f"sesiones/mes={self.__sesiones_por_mes}, "
                f"nivel={self.__nivel})")