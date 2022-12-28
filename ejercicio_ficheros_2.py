#Importamos la librería necesaria
import pickle

#Declaramos una clase Vehículo con ciertos atributos y un __str__ para hacer la lectura mas cómoda de los datos de la clase
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def __str__(self) -> str:
        return f'Soy un vehiculo de la marca {self.marca}, cuyo modelo es {self.modelo} con el color {self.color}'

#Iniciamos una instancia
coche = Vehiculo('bmw', 'm3', 'azul turquesa')

#cargamos los datos en un archivo en binario
f = open('file_car.bin', 'wb')
pickle.dump(coche, f)
f.close()

#leemos el archivo con los datos de la instancia
f = open('file_car.bin', 'rb')
file_car = pickle.load(f)
f.close()

#Imprimimos por pantalla la solución
print(file_car)