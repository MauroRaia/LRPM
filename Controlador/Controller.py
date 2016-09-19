from time import gmtime, strftime
import sys
sys.path.append('../Modelo')
from querys import *
import querys

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
        self.ventana.box_fv.setHidden(False)
        self.ventana.box_sv.setHidden(True)
        self.ventana.box_tv.setHidden(True)
        self.ventana.box_cv.setHidden(True)
        self.ventana.box_qv.setHidden(False)

    def autenticateA(self, user, password):
        if autenticarAdmin(user, password):
            self.ventana.show_sv()

    def autenticateE(user, password):
        if autenticarEmpleado(user, password):
            ident = querys.execute('SELECT ID FROM Empleados WHERE usuario=?', (user,))
            COLUMN = 0
            id_usuario = [elt[COLUMN] for elt in ident]
            timenow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            querys.execute('INSERT INTO Temporal VALUES (?, ?)', (id_usuario[0], timenow))
            self.show_sv()

    def agregarEmpleado(usuario, passwd, dni):
        querys.execute('INSERT INTO Empleados VALUES (?, ?, ?, ?, ?)', (usuario, passwd, dni, nombre, apellido))
        database.commit()

    def agregarAdministrador(usuario, passwd, dni, nombre, apellido):
        querys.execute('INSERT INTO Administradores VALUES (?, ?, ?, ?, ?)', (usuario, passwd, dni, nombre, apellido))
        database.commit()

    def validar():
        querys.execute('INSERT INTO Fichadas SELECT * FROM Temporal')
        querys.execute('DELETE FROM Temporal')
        database.commit()
