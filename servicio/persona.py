# Proyecto Segundo Parcial - GUI con Base de Datos
# Asignatura: Programación Orientada a Objetos
# Integrantes:
# - Cevallos Mendoza Samantha Nikole
# - Laura Fernanda Guillén Vargas
# - Cristhian Isaac Estrella Espinoza
# - Evelyn Noemi Burbano Mora
# - Janeth Maria Verdezoto García
#
# Controlador de la ventana principal: conecta los botones de la GUI
# con las operaciones CRUD reales sobre la base de datos ServicioGimnasio (tabla Servicio).

import re

from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

from GUI.vtn_principal import Ui_vtn_principal
from datos.conexion import ServicioDAO


class PersonaServicio(QMainWindow):
    """
    Clase que genera la lógica de la ventana principal:
    valida los datos ingresados y ejecuta las operaciones CRUD
    (guardar, buscar, actualizar, eliminar, limpiar) contra la base de datos.
    """

    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)

        # --- Conexión de botones ---
        self.ui.btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_buscar.clicked.connect(self.buscar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnEliminar.clicked.connect(self.eliminar)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

        # --- VALIDACIONES INTERACTIVAS (mientras el usuario escribe) ---

        # 1. Cédula: solo números
        regex_cedula = QRegularExpression(r"^[0-9]{0,10}$")
        self.ui.txt_cedula.setValidator(QRegularExpressionValidator(regex_cedula, self))
        self.ui.txt_buscarced.setValidator(QRegularExpressionValidator(regex_cedula, self))

        # 2. Nombre y Apellido: solo letras y espacios
        regex_letras = QRegularExpression(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
        validador_letras = QRegularExpressionValidator(regex_letras, self)
        self.ui.txt_nombre.setValidator(validador_letras)
        self.ui.txt_apellido.setValidator(validador_letras)

        # 3. Precio: solo números y un punto decimal (no permite negativos)
        regex_precio = QRegularExpression(r'^\d*\.?\d*$')
        self.ui.txt_precio.setValidator(QRegularExpressionValidator(regex_precio, self))

        # 4. Email: formato básico en tiempo real
        regex_email = QRegularExpression(r"^[a-zA-Z0-9._%+-]*@?[a-zA-Z0-9.-]*\.?[a-zA-Z]{0,}$")
        self.ui.txt_email.setValidator(QRegularExpressionValidator(regex_email, self))

    # ─────────────────────────────────────────────
    #  Validación general de los campos del formulario
    #  Devuelve (es_valido, datos) — si no es válido, datos es None
    # ─────────────────────────────────────────────
    def _validar_formulario(self):
        cedula = self.ui.txt_cedula.text().strip()
        nombre = self.ui.txt_nombre.text().strip()
        apellido = self.ui.txt_apellido.text().strip()
        email = self.ui.txt_email.text().strip()
        servicio = self.ui.cb_servicio.currentText().strip()
        descripcion = self.ui.txt_descrip.text().strip()
        precio_texto = self.ui.txt_precio.text().strip()

        # 1. Campos obligatorios no vacíos
        if not cedula:
            QMessageBox.warning(self, "Campo requerido", "La cédula no puede estar vacía.")
            return False, None
        if not nombre or not apellido:
            QMessageBox.warning(self, "Campo requerido", "El nombre y apellido son obligatorios.")
            return False, None
        if not email:
            QMessageBox.warning(self, "Campo requerido", "El email es obligatorio.")
            return False, None
        if servicio == "SELECCIONAR" or not servicio:
            QMessageBox.warning(self, "Campo requerido", "Debe seleccionar un servicio.")
            return False, None
        if not descripcion:
            QMessageBox.warning(self, "Campo requerido", "La descripción no puede estar vacía.")
            return False, None
        if not precio_texto:
            QMessageBox.warning(self, "Campo requerido", "El precio no puede estar vacío.")
            return False, None

        # 2. Cédula: exactamente 10 dígitos numéricos
        if not re.match(r"^\d{10}$", cedula):
            QMessageBox.warning(self, "Error de validación", "La cédula debe tener 10 dígitos numéricos.")
            return False, None

        # 3. Email: formato completo válido
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            QMessageBox.warning(self, "Error de validación", "El email ingresado no tiene un formato válido.")
            return False, None

        # 4. Precio: numérico y no negativo
        try:
            precio = float(precio_texto)
        except ValueError:
            QMessageBox.warning(self, "Error de validación", "El precio debe ser un número válido.")
            return False, None

        if precio < 0:
            QMessageBox.warning(self, "Error de validación", "El precio no puede ser negativo.")
            return False, None

        datos = {
            "cedula": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "servicio": servicio,
            "descripcion": descripcion,
            "precio": precio,
        }
        return True, datos

    # ─────────────────────────────────────────────
    #  GUARDAR (INSERT)
    # ─────────────────────────────────────────────
    def guardar(self):
        es_valido, datos = self._validar_formulario()
        if not es_valido:
            return

        try:
            ServicioDAO.guardar(**datos)
            QMessageBox.information(self, "Éxito", "El registro se guardó correctamente en la base de datos.")
            self.limpiar()
        except Exception as e:
            mensaje = str(e)
            if "PRIMARY KEY" in mensaje or "UNIQUE" in mensaje.upper() or "duplicate" in mensaje.lower():
                QMessageBox.warning(self, "Registro duplicado", f"Ya existe un registro con la cédula {datos['cedula']}.")
            else:
                QMessageBox.critical(self, "Error de base de datos", f"Ocurrió un error al guardar: {e}")

    # ─────────────────────────────────────────────
    #  BUSCAR (SELECT) — carga el registro en el formulario
    # ─────────────────────────────────────────────
    def buscar(self):
        cedula = self.ui.txt_buscarced.text().strip()
        if not cedula:
            QMessageBox.warning(self, "Campo requerido", "Ingrese una cédula para buscar.")
            return

        try:
            fila = ServicioDAO.buscar_por_cedula(cedula)
        except Exception as e:
            QMessageBox.critical(self, "Error de base de datos", f"Ocurrió un error al buscar: {e}")
            return

        if fila is None:
            QMessageBox.information(self, "Sin resultados", f"No existe ningún registro con la cédula {cedula}.")
            return

        self.ui.txt_cedula.setText(fila["cedula"])
        self.ui.txt_nombre.setText(fila["nombre"])
        self.ui.txt_apellido.setText(fila["apellido"])
        self.ui.txt_email.setText(fila["email"] or "")
        self.ui.txt_descrip.setText(fila["descripcion"] or "")
        self.ui.txt_precio.setText(str(fila["precio"]))

        indice = self.ui.cb_servicio.findText(fila["servicio"])
        self.ui.cb_servicio.setCurrentIndex(indice if indice >= 0 else 0)

    # ─────────────────────────────────────────────
    #  ACTUALIZAR (UPDATE)
    # ─────────────────────────────────────────────
    def actualizar(self):
        es_valido, datos = self._validar_formulario()
        if not es_valido:
            return

        try:
            actualizado = ServicioDAO.actualizar(**datos)
        except Exception as e:
            QMessageBox.critical(self, "Error de base de datos", f"Ocurrió un error al actualizar: {e}")
            return

        if actualizado:
            QMessageBox.information(self, "Éxito", "El registro se actualizó correctamente.")
            self.limpiar()
        else:
            QMessageBox.warning(self, "Sin resultados", f"No existe ningún registro con la cédula {datos['cedula']}.")

    # ─────────────────────────────────────────────
    #  ELIMINAR (DELETE) — con confirmación previa
    # ─────────────────────────────────────────────
    def eliminar(self):
        cedula = self.ui.txt_cedula.text().strip()
        if not cedula:
            QMessageBox.warning(self, "Campo requerido", "Ingrese o busque una cédula antes de eliminar.")
            return

        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro de eliminar el registro con cédula {cedula}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta != QMessageBox.Yes:
            return

        try:
            eliminado = ServicioDAO.eliminar(cedula)
        except Exception as e:
            QMessageBox.critical(self, "Error de base de datos", f"Ocurrió un error al eliminar: {e}")
            return

        if eliminado:
            QMessageBox.information(self, "Éxito", "El registro fue eliminado correctamente.")
            self.limpiar()
        else:
            QMessageBox.warning(self, "Sin resultados", f"No existe ningún registro con la cédula {cedula}.")

    # ─────────────────────────────────────────────
    #  LIMPIAR el formulario
    # ─────────────────────────────────────────────
    def limpiar(self):
        self.ui.txt_buscarced.setText('')
        self.ui.txt_cedula.setText('')
        self.ui.txt_nombre.setText('')
        self.ui.txt_apellido.setText('')
        self.ui.txt_email.setText('')
        self.ui.txt_descrip.setText('')
        self.ui.txt_precio.setText('')
        self.ui.cb_servicio.setCurrentIndex(0)
