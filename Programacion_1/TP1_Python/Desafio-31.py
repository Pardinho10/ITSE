"""Desafío 31
    Dado un numero entero informar la suma de sus dígitos.
"""
import continuar
while True:
    numero = input("Ingrese un numero \n")
    sumDig = 0
    if numero.lstrip('-').isdigit():
        for i in numero.lstrip('-'):
            sumDig = sumDig + int(i)
            print(i)
        print(f" El numero {numero} es de tipo {type(numero)} tiene {len(numero.lstrip('-'))} digitos y La suma de estos es: {sumDig}")
    else:
        print('No se ingreso un número')
    if not continuar.continuarNum():
        print('===========FIN DEL PROGRAMA==============')
        break 