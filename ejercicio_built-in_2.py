#Importamos las librerías necesarias
import functools

#Pedimos al usuario que ingrese los numeros separados con una coma
numeros = str(input('dar numeros separados por una coma: '))

#Creamos una lista con la entrada de los numeros
numeros_lista = []
numeros_lista = numeros.split(',')

#Los convertimos los elementos tipo 'str' en tipo 'int'
for number in range(len(numeros_lista)):
    numeros_lista[number] = int(numeros_lista[number])

#Definimos los numeros impares usando filter
impares = list(filter(lambda x: x % 2 != 0, numeros_lista))

#Calculamos la suma usando la funcion reduce, que esta en el modulo functools
resultado = functools.reduce(lambda a, b: a + b, impares)

#Imprimimos por pantalla el resultado final
print(resultado)