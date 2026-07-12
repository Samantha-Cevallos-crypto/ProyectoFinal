# Integrantes:
# -Cevallos Mendoza Samantha
# - Apellido Nombre
# - Apellido Nombre
# - Apellido Nombre

# ─────────────────────────────────────────────
# IMPORTACIÓN DE LA CLASE PADRE
# ─────────────────────────────────────────────
from servicio_gimnasio import ServicioGimnasio


# ─────────────────────────────────────────────
# Clase Hija: MembresiaMensual
# ─────────────────────────────────────────────
class MembresiaMensual(ServicioGimnasio):

    def __init__(self, codigo, nombre, descripcion,
                 precio, duracion_meses, promocion):

        # Herencia de la clase padre
        super().__init__(codigo, nombre, descripcion, precio)

        # Atributos propios
        self.__duracion_meses = duracion_meses
        self.__promocion = promocion

    # ─────────────────────────────────────────
    # GETTERS
    # ─────────────────────────────────────────
    @property
    def duracion_meses(self):
        return self.__duracion_meses

    @property
    def promocion(self):
        return self.__promocion

    # ─────────────────────────────────────────
    # SETTERS
    # ─────────────────────────────────────────
    @duracion_meses.setter
    def duracion_meses(self, meses):

        if meses <= 0:
            raise ValueError("La duración debe ser mayor a cero")

        self.__duracion_meses = meses

    @promocion.setter
    def promocion(self, promocion):

        if promocion < 0:
            raise ValueError("La promoción no puede ser negativa")

        self.__promocion = promocion

    # ─────────────────────────────────────────
    # Método polimórfico
    # ─────────────────────────────────────────
    def calcular_costo(self):

        descuento = self.precio * (self.__promocion / 100)

        total = (self.precio - descuento) * self.__duracion_meses

        return total

    # ─────────────────────────────────────────
    # Método polimórfico
    # ─────────────────────────────────────────
    def generar_reporte(self):

        print("══════ MEMBRESÍA MENSUAL ══════")
        print(f"Código            : {self.codigo}")
        print(f"Nombre            : {self.nombre}")
        print(f"Descripción       : {self.descripcion}")
        print(f"Precio mensual    : ${self.precio:.2f}")
        print(f"Duración          : {self.__duracion_meses} meses")
        print(f"Promoción         : {self.__promocion}%")
        print(f"Costo total       : ${self.calcular_costo():.2f}")
        print("═══════════════════════════════")

    # ─────────────────────────────────────────
    # Método __str__
    # ─────────────────────────────────────────
    def __str__(self):

        return (f"MembresiaMensual("
                f"{self.codigo}, "
                f"{self.nombre}, "
                f"${self.precio:.2f}, "
                f"{self.__duracion_meses} meses)")