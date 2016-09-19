import sqlite3

database = sqlite3.connect('fichadas.db')
querys = database.cursor()
#Autenticacion:

def autenticarEmpleado(autUsuario, autPasswd ):
        contra = querys.execute('SELECT passwd FROM Empleados WHERE usuario=?', (autUsuario,))
        COLUMN = 0
        column = [elt[COLUMN] for elt in contra]
        if column == [autPasswd]:
            return True
        else:
            return False

def autenticarAdmin(autUsuario, passwdaut ):
        contra = querys.execute('SELECT passwd FROM Administradores WHERE usuario=?)', (autUsuario,))
        COLUMN = 0
        column = [elt[COLUMN] for elt in contra]
        if column == [passwdaut]:
            return True
        else:
            return False
