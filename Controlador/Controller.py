from time import gmtime, strftime
import sys
sys.path.append('../Modelo')
from querys import *
import sqlite3

database = sqlite3.connect('fichadas.db')
querys = database.cursor()

class Controller():

    def __init__(self, una_ventana):
        self.ventana = una_ventana

    #funciones Vistas
    def show_fv(self):
        self.ventana.box_fv.setHidden(False)
        self.ventana.box_sv.setHidden(True)
        self.ventana.box_tv.setHidden(True)
        self.ventana.box_cv.setHidden(True)
        self.ventana.box_qv.setHidden(True)

    def show_sv(self):
        self.ventana.box_fv.setHidden(True)
        self.ventana.box_sv.setHidden(False)
        self.ventana.box_tv.setHidden(True)
        self.ventana.box_cv.setHidden(True)
        self.ventana.box_qv.setHidden(True)

    def show_tv(self):
        self.ventana.box_fv.setHidden(True)
        self.ventana.box_sv.setHidden(True)
        self.ventana.box_tv.setHidden(False)
        self.ventana.box_cv.setHidden(True)
        self.ventana.box_qv.setHidden(True)

    def show_cv(self):
        self.ventana.box_fv.setHidden(True)
        self.ventana.box_sv.setHidden(True)
        self.ventana.box_tv.setHidden(True)
        self.ventana.box_cv.setHidden(False)
        self.ventana.box_qv.setHidden(True)

    def show_qv(self):
        self.ventana.box_fv.setHidden(True)
        self.ventana.box_sv.setHidden(True)
        self.ventana.box_tv.setHidden(True)
        self.ventana.box_cv.setHidden(True)
        self.ventana.box_qv.setHidden(False)

    def autenticateA(self):
        user = str(self.ventana.displayUserAdmin.text())
        passwd = str(self.ventana.displayPassAdmin.text())
        contra = querys.execute('SELECT passwd FROM Administradores WHERE usuario=?', (user,))
        COLUMN = 0
        column = [elt[COLUMN] for elt in contra]
        if column == [passwd]:
            self.show_sv()
            print "si"
        else:
            print user
            print passwd

    def autenticateE(self):
        user = str(self.ventana.displayUserEmpleado.text())
        passwd = str(self.ventana.displayPassEmpleado.text())
        if autenticarEmpleado(user, passwd):
            ident = querys.execute('SELECT id_empleado FROM Empleados WHERE usuario=?', (user,))
            COLUMN = 0
            column = [elt[COLUMN] for elt in ident]
            timenow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            querys.execute('INSERT INTO Temporal(id_usuario, entrada) VALUES (?, ?)', (column[0], timenow))
            database.commit()
            self.show_sv()

    def agregarEmpleado(self):
        usuario = str(self.ventana.displayUserFEmpleado.text())
        passwd = str(self.ventana.displayPassFEmpleado.text())
        nombre = str(self.ventana.displayNombreEmpleado.text())
        apellido = str(self.ventana.displayApellidoEmpleado.text())
        dni = int(self.ventana.displayDniEmpleado.text())
        querys.execute('INSERT INTO Empleados(nombre, apellido, dni, usuario, passwd) VALUES (?, ?, ?, ?, ?)', (nombre, apellido, dni, usuario, passwd))
        database.commit()

    def agregarAdministrador(self):
        usuario = str(self.ventana.displayUserFAdmin.text())
        passwd = str(self.ventana.displayPassFAdmin.text())
        nombre = str(self.ventana.displayNombreAdmin.text())
        apellido = str(self.ventana.displayApellidoAdmin.text())
        dni = int(self.ventana.displayDniAdmin.text())
        querys.execute('INSERT INTO Administradores(nombre, apellido, dni, usuario, passwd) VALUES (?, ?, ?, ?, ?)', (nombre, apellido, dni, usuario, passwd))
        database.commit()
        self.show_sv()

    def validar(self):
        querys.execute('INSERT INTO Fichadas SELECT * FROM Temporal')
        querys.execute('DELETE FROM Temporal')
        database.commit()
