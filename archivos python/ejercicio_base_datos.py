#Importamos la librería necesaria
import sqlite3

#Definimos una funcion para iniciar el programa
def main():
    Crear_tabla()
    
    print('Añadir alumnos\nBuscar alumno')
    solicitud = input('Que desea hacer: ')
    
    if solicitud == 'Añadir alumnos':    
        cantidad = int(input('Cuantos alumnos vas a añadir: '))
        for i in range(cantidad):
            print(i)
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            Añadir_alumno(i, nombre, apellido)
            
    elif solicitud == 'Buscar alumno':
        busqueda(nombre=input('Nombre del alumno a buscar: '))
        
    else:
        print('No lo has escrito bien o no hay dicha funcion')

#Creamos una funcion para añadir una tabla de Alumnos
def Crear_tabla():
    conn = sqlite3.connect('mibase.db', isolation_level=None)
    cursor = conn.cursor()
    
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Alumnos (
            id integer,
            nombre text,
            apellido text
        )""")

    cursor.close()
    conn.close()

#Creamos una funcion que introduzca los nuevos alumnos
def Añadir_alumno(id, nombre, apellido):
    conn = sqlite3.connect('mibase.db', isolation_level=None)
    cursor = conn.cursor()
    
    cursor.execute(
                   f'INSERT INTO Alumnos(id, nombre, apellido) VALUES(?, ?, ?)',
                   (id, nombre, apellido)
                   )
    
    cursor.close()
    conn.close()

#Creamos una funcion para buscar y devolver los datos del alumno
def busqueda(nombre):
    conn = sqlite3.connect('mibase.db', isolation_level=None)
    cursor = conn.cursor()
    
    rows = cursor.execute(
        f'SELECT * FROM Alumnos WHERE nombre="{nombre}"'
        )
    
    data = rows.fetchone()
    
    cursor.close()
    conn.close()
    
    if data == None:
        print('No se ha encontrado al alumno buscado')
    return print(data) 

#Instanciamos el programa
if __name__ == '__main__':
    main()
