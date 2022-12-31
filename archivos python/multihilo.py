import _thread
import time

def HoraActual(nombre_thread, tiempo_de_espera):
    time.sleep(tiempo_de_espera)
    
    print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')

_thread.start_new_thread(HoraActual, ('thread uno', 0))
_thread.start_new_thread(HoraActual, ('thread dos', 0))

    
import logging

logging.basicConfig(level=logging.WARNING)
logging.warning('hace calor')
logging.info('arrancando programa')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mifuncion(x):
    if x % 2 == 0:
        return True
    return False
 
resultado = filter(lambda x: x % 2 == 0, numeros)

def cuadrado(x):
    return x * x

print(list(map(cuadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(list(resultado)) 