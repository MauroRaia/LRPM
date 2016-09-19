# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore, QtSql
sys.path.append('../Controlador')
from Controller import *


def initializeModel(model):
    model.setTable('Temporal')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "Fecha Entrada")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Fecha Salida")


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.controlador = Controller(self)
        self.init_ui()


    def init_ui(self):
        self.main_grid = QtGui.QGridLayout()

        #Botones
        button_showAgregarEmpleado = QtGui.QPushButton('Agregar Empleado')
        button_showAgregarAdmin = QtGui.QPushButton('Agregar Admin')
        button_login_empleado = QtGui.QPushButton('Login')
        button_submit = QtGui.QPushButton('Submit')
        button_ficharEntrada = QtGui.QPushButton('Fichar Entrada')
        button_login_Admin = QtGui.QPushButton('Login')
        button_validar_horas = QtGui.QPushButton('Validar Horas')

        ##Primera Vista
        self.displayUserAdmin = QtGui.QLineEdit('Usuario')
        self.displayPassAdmin = QtGui.QLineEdit('password')
        self.displayPassAdmin.setEchoMode(2)
        layout_grid_fv = QtGui.QGridLayout()
        layout_grid_fv.addWidget(self.displayUserAdmin)
        layout_grid_fv.addWidget(self.displayPassAdmin)
        layout_grid_fv.addWidget(button_login_Admin)
        self.box_fv = QtGui.QGroupBox()
        self.box_fv.setLayout(layout_grid_fv)
        button_login_Admin.clicked.connect(lambda: self.controlador.autenticateA())

        #Segunda Vista
        layout_grid_sv = QtGui.QGridLayout()
        layout_grid_sv.addWidget(button_ficharEntrada)
        layout_grid_sv.addWidget(button_showAgregarAdmin)
        layout_grid_sv.addWidget(button_showAgregarEmpleado)
        layout_grid_sv.addWidget(button_validar_horas)
        button_ficharEntrada.clicked.connect(self.controlador.show_tv)
        button_showAgregarAdmin.clicked.connect(self.controlador.show_qv)
        button_showAgregarEmpleado.clicked.connect(self.controlador.show_cv)
        self.box_sv = QtGui.QGroupBox()
        self.box_sv.setLayout(layout_grid_sv)
        self.box_sv.setHidden(True)
        model = QtSql.QSqlTableModel()
        timer = QtCore.QTimer()
        timer.timeout.connect(lambda: initializeModel(model))
        timer.start(500)
        view = QtGui.QTableView()
        view.setModel(model)
        view.setWindowTitle("Fichadas del dia")
        layout_grid_sv.addWidget(view)

        ##Tercer Vista
        self.displayUserEmpleado = QtGui.QLineEdit('Usuario')
        self.displayPassEmpleado = QtGui.QLineEdit('password')
        self.displayPassEmpleado.setEchoMode(2)
        layout_grid_tv = QtGui.QGridLayout()
        layout_grid_tv.addWidget(self.displayUserEmpleado)
        layout_grid_tv.addWidget(self.displayPassEmpleado)
        layout_grid_tv.addWidget(button_login_empleado)
        button_login_empleado.clicked.connect(lambda: self.controlador.autenticateE())
        self.box_tv = QtGui.QGroupBox()
        self.box_tv.setLayout(layout_grid_tv)
        self.box_tv.setHidden(True)

        ##Cuarta Vista
        self.displayNombreEmpleado = QtGui.QLineEdit('Nombre')
        self.displayApellidoEmpleado = QtGui.QLineEdit('Apellido')
        self.displayDniEmpleado = QtGui.QLineEdit('DNI')
        self.displayUserFEmpleado = QtGui.QLineEdit('Usuario')
        self.displayPassFEmpleado = QtGui.QLineEdit('Password')
        button_submit.clicked.connect(lambda: self.controlador.agregarEmpleado())
        layout_grid_cv = QtGui.QGridLayout()
        layout_grid_cv.addWidget(self.displayNombreEmpleado)
        layout_grid_cv.addWidget(self.displayApellidoEmpleado)
        layout_grid_cv.addWidget(self.displayDniEmpleado)
        layout_grid_cv.addWidget(self.displayUserFEmpleado)
        layout_grid_cv.addWidget(self.displayPassFEmpleado)
        layout_grid_cv.addWidget(button_submit)
        self.box_cv = QtGui.QGroupBox()
        self.box_cv.setLayout(layout_grid_cv)
        self.box_cv.setHidden(True)

        #Quinta Vista
        self.displayNombreAdmin = QtGui.QLineEdit('Nombre')
        self.displayApellidoAdmin = QtGui.QLineEdit('Apellido')
        self.displayDniAdmin = QtGui.QLineEdit('DNI')
        self.displayUserFAdmin = QtGui.QLineEdit('Usuario')
        self.displayPassFAdmin = QtGui.QLineEdit('password')
        button_submit_admin = QtGui.QPushButton('submit')
        button_submit_admin.clicked.connect(lambda: self.controlador.agregarAdministrador())
        layout_grid_qv = QtGui.QGridLayout()
        layout_grid_qv.addWidget(self.displayNombreAdmin)
        layout_grid_qv.addWidget(self.displayApellidoAdmin)
        layout_grid_qv.addWidget(self.displayDniAdmin)
        layout_grid_qv.addWidget(self.displayUserFAdmin)
        layout_grid_qv.addWidget(self.displayPassFAdmin)
        layout_grid_qv.addWidget(button_submit_admin)
        self.box_qv = QtGui.QGroupBox()
        self.box_qv.setLayout(layout_grid_qv)
        self.box_qv.setHidden(True)

        #Union a grid principal
        self.main_grid.addWidget(self.box_fv, 1, 1, 1, 1)
        self.main_grid.addWidget(self.box_sv, 1, 1, 1, 1)
        self.main_grid.addWidget(self.box_tv, 1, 1, 1, 1)
        self.main_grid.addWidget(self.box_cv, 1, 1, 1, 1)
        self.main_grid.addWidget(self.box_qv, 1, 1, 1, 1)

        self.setLayout(self.main_grid)
        self.setWindowTitle('Montage')
        self.setGeometry(400, 400, 400, 400)
        self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
