def año_bisiesto():
    año = int(input('introduce el año a determinar: '))
    
    if año % 100 == 0 and año % 400 == 0:
        print(f'el año {año} es bisiesto y secular')

    elif año % 4 == 0 and año % 100 != 0:
        print(f'el año {año} es bisiesto y no secular')

    else:
        print(f'el año {año} no es bisiesto')
        
año_bisiesto()