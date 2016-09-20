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
        contra = querys.execute('SELECT passwd FROM Administradores WHERE usuario=?', (autUsuario,))
        COLUMN = 0
        column = [elt[COLUMN] for elt in contra]
        if column == [passwdaut]:
            return True
        else:
            return False
def siExisteEntrada(id_empleado):
    checkEntrada = querys.execute('SELECT count() FROM Temporal WHERE id_empleado=?', (id_empleado,))
    COLUMN = 0
    column = [elt[COLUMN] for elt in checkEntrada]
    prueba = column[0]
    return prueba!=0
