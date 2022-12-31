file = open('file.txt', 'a')
file = open('file.txt', 'a')

lineas = ['linea 1', 'linea 2', 'linea 3', 'linea 4', 'esto funciona']

for linea in lineas:
    if not linea.endswith('\n'):
        linea = linea + '\n'   
    file.write(linea)
    
file.close()

file = open('file.txt', 'r')

print(file.read())
file.close()