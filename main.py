# Proyecto Segundo Parcial - GUI con Base de Datos
# Asignatura: Programación Orientada a Objetos
# Jornada: Matutina / Vespertina  # <-- ajustar según corresponda
# Grupo: 2
# Integrantes:
# - Cevallos Mendoza Samantha Nikole
# - Laura Fernanda Guillén Vargas
# - Cristhian Isaac Estrella Espinoza
# - Evelyn Noemi Burbano Mora
# - Janeth Maria Verdezoto García
#
# Punto de entrada de la aplicación: lanza la ventana principal.

import sys

from PySide6.QtWidgets import QApplication

from servicio.persona import PersonaServicio

app = QApplication(sys.argv)
vtn_principal = PersonaServicio()
vtn_principal.show()
sys.exit(app.exec())
