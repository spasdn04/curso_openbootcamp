#Pedimos al usuario que introduzca los paises separados por una coma
paises = str(input('Nombra paises separados por una coma: '))

#Separamos los paises por la coma y formamos una lista con ellos
paises = paises.split(',')

#Filtramos los paises para que no haya repetidos
paso_1 = set(paises)

#Capitalizamos para darle un mejor formato a la salida
paso_2 = []
for i in paso_1:
    paso_2.append(i.capitalize())

#Ordenamos alfabeticamente los países e imprimimos en la terminal la lista final
paso_2.sort()
print(paso_2)
