# Integrantes:
# - Cevallos Mendoza Samantha nikole
# - Laura Fernanda Guillén Vargas
# - Cristhian Isaac Estrella Espinoza
# - Evelyn Noemi Burbano Mora
# -Janeth Maria Verdezoto García

# ─────────────────────────────────────────────
# Clase Adicional 1: Socio
# Representa a un miembro registrado en el
# gimnasio y el servicio al que está inscrito.
# ─────────────────────────────────────────────
from servicio_gimnasio import ServicioGimnasio


class Socio:
    """
    Representa a un socio/miembro del gimnasio.
    Tiene encapsulamiento completo con @property y @setter.
    Contiene una referencia a un ServicioGimnasio activo.
    """

    def __init__(self, codigo_socio, nombre, email, telefono,
                 servicio: ServicioGimnasio):
        # Validaciones
        if not codigo_socio:
            raise ValueError("El código de socio no puede estar vacío.")
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if not email or "@" not in email:
            raise ValueError("El email ingresado no es válido.")
        if not telefono:
            raise ValueError("El teléfono no puede estar vacío.")
        if not isinstance(servicio, ServicioGimnasio):
            raise TypeError("El servicio debe ser una instancia de ServicioGimnasio.")

        # Atributos privados encapsulados
        self.__codigo_socio = codigo_socio
        self.__nombre       = nombre
        self.__email        = email
        self.__telefono     = telefono
        self.__servicio     = servicio   # Composición: Socio tiene un ServicioGimnasio

    # ── Getters ──────────────────────────────
    @property
    def codigo_socio(self):
        return self.__codigo_socio

    @property
    def nombre(self):
        return self.__nombre

    @property
    def email(self):
        return self.__email

    @property
    def telefono(self):
        return self.__telefono

    @property
    def servicio(self):
        return self.__servicio

    # ── Setters con validación ────────────────
    @codigo_socio.setter
    def codigo_socio(self, codigo):
        if not codigo:
            raise ValueError("El código de socio no puede estar vacío.")
        self.__codigo_socio = codigo

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    @email.setter
    def email(self, email):
        if not email or "@" not in email:
            raise ValueError("El email ingresado no es válido.")
        self.__email = email

    @telefono.setter
    def telefono(self, telefono):
        if not telefono:
            raise ValueError("El teléfono no puede estar vacío.")
        self.__telefono = telefono

    @servicio.setter
    def servicio(self, servicio):
        if not isinstance(servicio, ServicioGimnasio):
            raise TypeError("El servicio debe ser una instancia de ServicioGimnasio.")
        self.__servicio = servicio

    # ── Métodos propios ───────────────────────
    def mostrar_info(self):
        """Muestra la información completa del socio y su servicio activo."""
        print("══════ DATOS DEL SOCIO ══════")
        print(f"  Código      : {self.__codigo_socio}")
        print(f"  Nombre      : {self.__nombre}")
        print(f"  Email       : {self.__email}")
        print(f"  Teléfono    : {self.__telefono}")
        print(f"  Servicio    : {self.__servicio.nombre}")
        print(f"  Precio/mes  : ${self.__servicio.precio:.2f}")
        print("═════════════════════════════")

    def cambiar_servicio(self, nuevo_servicio: ServicioGimnasio):
        """Permite al socio cambiar su servicio activo."""
        if not isinstance(nuevo_servicio, ServicioGimnasio):
            raise TypeError("El servicio debe ser una instancia de ServicioGimnasio.")
        self.__servicio = nuevo_servicio
        print(f"  Servicio actualizado para {self.__nombre}: "
              f"ahora en '{nuevo_servicio.nombre}'.")

    # ── Representación en texto ───────────────
    def __str__(self):
        return (f"Socio("
                f"codigo={self.__codigo_socio}, "
                f"nombre={self.__nombre}, "
                f"email={self.__email}, "
                f"servicio={self.__servicio.nombre})")