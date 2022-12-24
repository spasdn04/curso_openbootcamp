class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f'el alumno {nombre} tiene de nota un {nota}')
        
    def aprobrar(self):
        if self.nota >= 5:
            print(f'{self.nombre} ha aprobado con {self.nota}')
        else:
            print(f'{self.nombre} ha suspendido con {self.nota}')
        
alumno1 = Alumno('pepito', 4)
alumno1.aprobrar()