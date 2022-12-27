import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print('Es hora de irse')
else:
    print(f'quedan {18-int(hora)} horas y {59-int(minutos)} minutos para irse para casa')