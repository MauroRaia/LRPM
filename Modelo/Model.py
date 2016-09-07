import sys
from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout, QTableView
from PyQt4.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.userLine = QLineEdit()
        self.userLine.setObjectName("user")
        self.userLine.setText("Usuario")

        self.passwdLine = QLineEdit()
        self.passwdLine.setObjectName("passwd")
        self.passwdLine.setText("Contrasenia")

        self.pb = QPushButton()
        self.pb.setObjectName("agregar")
        self.pb.setText("Agregar")

        layout = QFormLayout()
        layout.addWidget(self.userLine)
        layout.addWidget(self.passwdLine)
        layout.addWidget(self.pb)
        layout.addWidget(projectView)

        self.setLayout(layout)
        self.connect(self.pb, SIGNAL("clicked()"),self.button_click)
        self.setWindowTitle("Prueba")

    def button_click(self):

        user = str(self.userLine.text())
        passwd= str(self.passwdLine.text())
        query = QtSql.QSqlQuery()
        query.exec_("insert into empleados values(01, " + user + ", " + passwd + ")")
        print user + " " + passwd

def initializeModel(model):
    model.setTable('empleados')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")

def createView(title, model):
    view = QtGui.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def update():
    projectModel.setQuery("select * from empleados",db)

if __name__ == '__main__':

   query = QtSql.QSqlQuery()
   app = QtGui.QApplication(sys.argv)
   app.setQuitOnLastWindowClosed(False)
   db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('fichadas.db')
   model = QtSql.QSqlTableModel()
   delrow = -1
   initializeModel(model)

   projectModel = QSqlQueryModel()
   update()
   projectView = QTableView()
   projectView.setModel(projectModel)

   timer = QTimer()
   timer.timeout.connect(update)
   timer.start(1000)

   form = Form()
   form.show()
   sys.exit(app.exec_())
