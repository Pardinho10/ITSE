"""Desafío 24
    Desarrollar un programa que permita al usuario ingresar dos años y luego imprima
    todos los años en ese rango, que sean bisiestos y múltiplos de 10. Nota: para que un
    año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
"""

import continuar

while True:
    año1 = input('Ingrese el primer año a analizar (número entre 1 y 9999)\n')
    año2 = input('Ingrese el segundo año a analizar (número entre 1 y 9999)\n')
    if año1.isdigit() and año2.isdigit() :
        año_int1 = int(año1)
        año_int2 = int(año2)
        if 1 <= año_int1 <= 9999 and 1 <= año_int2 <= 9999:
            for año_entre in range(año_int1, año_int2+1):
                if (año_entre % 4 == 0 and (año_entre % 100 != 0 or año_entre % 400 == 0)) and año_entre % 10 == 0:
                    print(f'{año_entre} es año bisiesto y multiplo de 10\n')
                else:
                    print(f'{año_entre} es un año común\n')
        else:
            print('El año ingresado esta fuera de rango (debe ser un valor entre 1 y 9999)\n ')
    else:
        print('Los valores ingresados deben ser números enteros\n')

    if not continuar.continuarNum():
        print('===========FIN DEL PROGRAMA===========')
        break