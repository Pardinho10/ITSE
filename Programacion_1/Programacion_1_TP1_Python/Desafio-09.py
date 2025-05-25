"""Desafío 9
    Desarrollar un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
"""

import continuar
while True:
    año = input('Ingrese un año a analizar (1 - 9999)\n')
    if año.isdigit():
        año_int = int(año)
        if 1 <= año_int <= 9999:
            if año_int % 4 == 0 and (año_int % 100 != 0 or año_int % 400 == 0):
                print(f'{año_int} es un año bisiesto')
            else:
                print(f'{año_int} no es un año bisiesto')
        else:
            print('El año ingresado esta fuera de rango (debe estar entre 1 y 9999)\n ')
    else:
        print('Debe ingresar un número entero')
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA==============')
        break