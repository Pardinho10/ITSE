"""Desafío 8
    Desarrollar un programa que solicite al usuario una letra y, si es una vocal, muestre el
    mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa
    un dato de más de un carácter, informar que no se puede procesar.
"""

import continuar

while True:
    letra = input('Ingrese una letra\n')
    if len(letra) == 1 and not letra.isdigit():
        if letra in ('a', 'e', 'i', 'o', 'u'):
            print(f'La letra ingresada ({letra}) es una vocal\n')
        else:
            print(f'La letra ingresada ({letra}) NO es una vocal\n')
    elif letra.isdigit():
        print('El dato ingresado no debe ser un número, no puede procesarse')
    else:
        print(f'El dato ingresado posee {len(letra)} caracteres, no puede procesarse\n')
    if not continuar.continuarGen():
        break