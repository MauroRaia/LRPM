from time import *
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
        self.ventana.box_vv.setHidden(True)

    def show_sv(self):
        self.ventana.box_fv.setHidden(True)
        self.ventana.box_sv.setHidden(False)
        self.ventana.box_tv.setHidden(True)
        self.ventana.box_cv.setHidden(True)
        self.ventana.box_qv.setHidden(True)
        self.ventana.box_vv.setHidden(True)

    def show_tv(self):
        self.ventana.box_fv.setHidden(True)
        self.ventana.box_sv.setHidden(True)
        self.ventana.box_tv.setHidden(False)
        self.ventana.box_cv.setHidden(True)
        self.ventana.box_qv.setHidden(True)
        self.ventana.box_vv.setHidden(True)

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
        self.ventana.box_vv.setHidden(True)

    def show_vv(self):
        self.ventana.box_fv.setHidden(True)
        self.ventana.box_sv.setHidden(True)
        self.ventana.box_tv.setHidden(True)
        self.ventana.box_cv.setHidden(True)
        self.ventana.box_qv.setHidden(True)
        self.ventana.box_vv.setHidden(False)

    def disconnect(self):
        self.ventana.displayUserAdmin.clear()
        self.ventana.displayPassAdmin.clear()
        self.ventana.displayUserAdmin.insert("Usuario")
        self.ventana.displayPassAdmin.insert("passwd")
        self.show_fv()

    def autenticateA(self):
        user = str(self.ventana.displayUserAdmin.text())
        passwd = str(self.ventana.displayPassAdmin.text())
        contra = querys.execute('SELECT passwd FROM Administradores WHERE usuario=?', (user,))
        COLUMN = 0
        column = [elt[COLUMN] for elt in contra]
        if column == [passwd]:
            self.show_sv()


    def autenticateE(self):
        user = str(self.ventana.displayUserEmpleado.text())
        passwd = str(self.ventana.displayPassEmpleado.text())
        if autenticarEmpleado(user, passwd):
            ident = querys.execute('SELECT id_empleado FROM Empleados WHERE usuario=?', (user,))
            COLUMN = 0
            column = [elt[COLUMN] for elt in ident]
            timenow = strftime("%H:%M:%S", localtime())
            year = strftime("%Y", localtime())
            month = strftime("%m", localtime())
            day = strftime("%d", localtime())
            id_empleado = column[0]
            if siExisteEntrada(id_empleado):
                querys.execute('UPDATE Temporal SET salida=? WHERE id_empleado=?', (timenow, id_empleado))
                database.commit()
                self.show_sv()
            else:
                querys.execute('INSERT INTO Temporal(id_empleado, year, month, day, entrada) VALUES (?, ?, ?, ?, ?)', (id_empleado, year, month, day, timenow))
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
        self.ventana.displayUserFEmpleado.clear()
        self.ventana.displayPassFEmpleado.clear()
        self.ventana.displayDniEmpleado.clear()
        self.ventana.displayNombreEmpleado.clear()
        self.ventana.displayApellidoEmpleado.clear()
        self.ventana.displayUserFEmpleado.insert("Usuario")
        self.ventana.displayPassFEmpleado.insert("Passwd")
        self.ventana.displayDniEmpleado.insert("Dni")
        self.ventana.displayNombreEmpleado.insert("Nombre")
        self.ventana.displayApellidoEmpleado.insert("Apellido")
        self.show_sv()

    def agregarAdministrador(self):
        usuario = str(self.ventana.displayUserFAdmin.text())
        passwd = str(self.ventana.displayPassFAdmin.text())
        nombre = str(self.ventana.displayNombreAdmin.text())
        apellido = str(self.ventana.displayApellidoAdmin.text())
        dni = int(self.ventana.displayDniAdmin.text())
        querys.execute('INSERT INTO Administradores(nombre, apellido, dni, usuario, passwd) VALUES (?, ?, ?, ?, ?)', (nombre, apellido, dni, usuario, passwd))
        database.commit()
        self.ventana.displayUserFAdmin.clear()
        self.ventana.displayPassFAdmin.clear()
        self.ventana.displayDniAdmin.clear()
        self.ventana.displayNombreAdmin.clear()
        self.ventana.displayApellidoAdmin.clear()
        self.ventana.displayUserFAdmin.insert("Usuario")
        self.ventana.displayPassFAdmin.insert("Passwd")
        self.ventana.displayDniAdmin.insert("Dni")
        self.ventana.displayNombreAdmin.insert("Nombre")
        self.ventana.displayApellidoAdmin.insert("Apellido")
        self.show_sv()

    def validar(self):
        querys.execute('INSERT INTO Fichadas SELECT * FROM Temporal')
        querys.execute('DELETE FROM Temporal')
        database.commit()


    def busqueda(self):
        querys.execute('DELETE FROM BusquedaF')
        database.commit()
        value = str(self.ventana.comboBox.currentText())
        desde = str(self.ventana.displayDesde.text())
        hasta = str(self.ventana.displayHasta.text())
        self.ventana.displayDesde.clear()
        self.ventana.displayHasta.clear()
        print value
        print desde
        print hasta
        querys.execute('INSERT INTO BusquedaF SELECT * FROM Fichadas WHERE {campo} BETWEEN ? AND ?'.format(campo=value), (desde, hasta))
        database.commit()

    def atrasBusqueda(self):
        querys.execute("DELETE FROM BusquedaF")
        database.commit()
        self.ventana.displayDesde.clear()
        self.ventana.displayHasta.clear()
        self.ventana.displayDesde.insert("Desde")
        self.ventana.displayHasta.insert("Hasta")
        self.show_sv()



#SELECT * FROM myTable WHERE myNumber >= 1 AND myNumber <= 100, (campo, valor1, campo, valor2)