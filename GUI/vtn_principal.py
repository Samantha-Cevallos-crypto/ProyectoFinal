# Proyecto Segundo Parcial - GUI con Base de Datos
# Asignatura: Programación Orientada a Objetos
# Archivo generado a partir de vtn_principal.ui (Qt Designer)
# NOTA: Si vuelves a editar el .ui en Qt Designer, puedes regenerar este archivo con:
#   pyside6-uic vtn_principal.ui -o vtn_principal.py

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QComboBox, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QStatusBar, QWidget)


class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(673, 409)

        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")

        # ---- Buscar por cédula ----
        self.lbl_buscarced = QLabel(self.centralwidget)
        self.lbl_buscarced.setObjectName(u"lbl_buscarced")
        self.lbl_buscarced.setGeometry(QRect(120, 30, 131, 16))

        self.txt_buscarced = QLineEdit(self.centralwidget)
        self.txt_buscarced.setObjectName(u"txt_buscarced")
        self.txt_buscarced.setGeometry(QRect(260, 30, 161, 22))
        self.txt_buscarced.setMaxLength(10)

        self.btn_buscar = QPushButton(self.centralwidget)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setGeometry(QRect(440, 30, 93, 28))

        # ---- Nombre ----
        self.lbl_nombre = QLabel(self.centralwidget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(120, 60, 131, 16))

        self.txt_nombre = QLineEdit(self.centralwidget)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(260, 60, 281, 22))
        self.txt_nombre.setMaxLength(100)

        # ---- Apellido ----
        self.lbl_apellido = QLabel(self.centralwidget)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(120, 90, 131, 16))

        self.txt_apellido = QLineEdit(self.centralwidget)
        self.txt_apellido.setObjectName(u"txt_apellido")
        self.txt_apellido.setGeometry(QRect(260, 90, 281, 22))
        self.txt_apellido.setMaxLength(100)

        # ---- Cédula ----
        self.lbl_cedula = QLabel(self.centralwidget)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(120, 120, 131, 16))

        self.txt_cedula = QLineEdit(self.centralwidget)
        self.txt_cedula.setObjectName(u"txt_cedula")
        self.txt_cedula.setGeometry(QRect(260, 120, 281, 22))
        self.txt_cedula.setMaxLength(10)

        # ---- Email ----
        self.lbl_email = QLabel(self.centralwidget)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(120, 150, 55, 16))

        self.txt_email = QLineEdit(self.centralwidget)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(260, 150, 281, 21))
        self.txt_email.setMaxLength(150)

        # ---- Servicio (combo) ----
        self.lbl_servicio = QLabel(self.centralwidget)
        self.lbl_servicio.setObjectName(u"lbl_servicio")
        self.lbl_servicio.setGeometry(QRect(120, 180, 61, 16))

        self.cb_servicio = QComboBox(self.centralwidget)
        self.cb_servicio.addItem("SELECCIONAR")
        self.cb_servicio.addItem("Acceso Libre")
        self.cb_servicio.addItem("Spinning")
        self.cb_servicio.addItem("Personal Training")
        self.cb_servicio.addItem(u"Membresía Anual")
        self.cb_servicio.setObjectName(u"cb_servicio")
        self.cb_servicio.setGeometry(QRect(260, 180, 281, 22))

        # ---- Descripción ----
        self.lbl_descrip = QLabel(self.centralwidget)
        self.lbl_descrip.setObjectName(u"lbl_descrip")
        self.lbl_descrip.setGeometry(QRect(120, 210, 81, 16))

        self.txt_descrip = QLineEdit(self.centralwidget)
        self.txt_descrip.setObjectName(u"txt_descrip")
        self.txt_descrip.setGeometry(QRect(260, 210, 281, 21))
        self.txt_descrip.setMaxLength(150)

        # ---- Precio ----
        self.lbl_precio = QLabel(self.centralwidget)
        self.lbl_precio.setObjectName(u"lbl_precio")
        self.lbl_precio.setGeometry(QRect(120, 240, 55, 16))

        self.txt_precio = QLineEdit(self.centralwidget)
        self.txt_precio.setObjectName(u"txt_precio")
        self.txt_precio.setGeometry(QRect(260, 240, 281, 20))
        self.txt_precio.setMaxLength(10)

        # ---- Botones de acción ----
        self.btn_guardar = QPushButton(self.centralwidget)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(130, 280, 75, 31))

        self.btnActualizar = QPushButton(self.centralwidget)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(220, 280, 93, 31))

        self.btnEliminar = QPushButton(self.centralwidget)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setGeometry(QRect(330, 280, 93, 31))

        self.btn_limpiar = QPushButton(self.centralwidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(440, 280, 81, 31))

        vtn_principal.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(vtn_principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 673, 18))
        vtn_principal.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(vtn_principal)
        self.statusbar.setObjectName(u"statusbar")
        vtn_principal.setStatusBar(self.statusbar)

        QWidget.setTabOrder(self.txt_buscarced, self.txt_nombre)
        QWidget.setTabOrder(self.txt_nombre, self.txt_apellido)
        QWidget.setTabOrder(self.txt_apellido, self.txt_cedula)
        QWidget.setTabOrder(self.txt_cedula, self.txt_email)
        QWidget.setTabOrder(self.txt_email, self.txt_descrip)
        QWidget.setTabOrder(self.txt_descrip, self.txt_precio)
        QWidget.setTabOrder(self.txt_precio, self.btn_guardar)
        QWidget.setTabOrder(self.btn_guardar, self.btn_limpiar)

        self.retranslateUi(vtn_principal)
        QMetaObject.connectSlotsByName(vtn_principal)

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"Registro de Servicios - Gimnasio", None))
        self.lbl_buscarced.setText(QCoreApplication.translate("vtn_principal", u"BUSCAR POR CEDULA:", None))
        self.btn_buscar.setText(QCoreApplication.translate("vtn_principal", u"BUSCAR", None))
        self.lbl_nombre.setText(QCoreApplication.translate("vtn_principal", u"NOMBRE:", None))
        self.lbl_apellido.setText(QCoreApplication.translate("vtn_principal", u"APELLIDO:", None))
        self.lbl_cedula.setText(QCoreApplication.translate("vtn_principal", u"CEDULA:", None))
        self.lbl_email.setText(QCoreApplication.translate("vtn_principal", u"EMAIL:", None))
        self.lbl_servicio.setText(QCoreApplication.translate("vtn_principal", u"SERVICIO:", None))
        self.lbl_descrip.setText(QCoreApplication.translate("vtn_principal", u"DESCRIPCION:", None))
        self.lbl_precio.setText(QCoreApplication.translate("vtn_principal", u"PRECIO:", None))
        self.btn_guardar.setToolTip(QCoreApplication.translate("vtn_principal", u"guardar datos del usuario", None))
        self.btn_guardar.setText(QCoreApplication.translate("vtn_principal", u"GUARDAR", None))
        self.btnActualizar.setText(QCoreApplication.translate("vtn_principal", u"ACTUALIZAR", None))
        self.btnEliminar.setText(QCoreApplication.translate("vtn_principal", u"ELIMINAR", None))
        self.btn_limpiar.setToolTip(QCoreApplication.translate("vtn_principal", u"borrar el formulario", None))
        self.btn_limpiar.setText(QCoreApplication.translate("vtn_principal", u"LIMPIAR", None))
