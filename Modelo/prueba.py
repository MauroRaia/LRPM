import sys
from PyQt4 import QtCore, QtGui, QtSql
import sqlite3
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout, QTableView
from PyQt4.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.userLine = QLineEdit()
        self.userLine.setObjectName("user")
        self.userLine.setText("Usuario")

        self.passwdLine = QLineEdit()
        self.passwdLine.setObjectName("passwd")
        self.passwdLine.setText("Contrasenia")

        self.idLine = QLineEdit()
        self.idLine.setObjectName("id_user")
        self.idLine.setText("ID del usuario")

        self.pb = QPushButton()
        self.pb.setObjectName("agregar")
        self.pb.setText("Agregar")

        self.layout = QFormLayout()
        self.layout.addWidget(self.userLine)
        self.layout.addWidget(self.passwdLine)
        self.layout.addWidget(self.pb)
        self.layout.addWidget(self.idLine)
        self.layout.addWidget(view)


        self.setLayout(self.layout)
        self.connect(self.pb, SIGNAL("clicked()"),self.button_click)
        self.setWindowTitle("Prueba")

    def button_click(self):

        id_user = int(self.idLine.text())
        user = str(self.userLine.text())
        passwd= str(self.passwdLine.text())
        querys.execute('drop table empleados')
        #querys.execute('insert into empleados values (?, ?, ?)', (id_user, user, passwd))
        database.commit()


def initializeModel(model):
    model.setTable('empleados')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "Usuario")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Contrasenia")

if __name__ == '__main__':

    #Seteo la base de datos en QtSql para poder mostrarla como un objeto de la
    #clase TableModel
    app = QtGui.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('fichadas.db')

    #Seteo base de datos con Sqlite3 para trabajar con las querys. Da cancer
    #trabajar con las querys de QtSql, mas facil con este
    database = sqlite3.connect('fichadas.db')
    querys = database.cursor()

    model = QtSql.QSqlTableModel()
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: initializeModel(model))
    timer.start(500)

    #Seteo el objeto TableModel a una TableView, que abre una ventana ya
    #configurada para mostrar una tabla
    view = QtGui.QTableView()
    view.setModel(model)
    view.setWindowTitle("Pruebas de view de DB")

    form = Form()
    form.show()
    sys.exit(app.exec_())
