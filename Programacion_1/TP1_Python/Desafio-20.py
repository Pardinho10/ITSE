"""Desafío 20
    Dado un número entero positivo, mostrar su Factorial. El Factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
"""
import continuar

while True:
    numero = int(input('Ingrese un número para calcular su factorial\n'))
    if numero > 0 :
        factorial = numero
        cont = numero
        while cont > 1:
            cont -= 1
            factorial = factorial * cont
        print(f'El factorial del número {numero} es: {factorial} \n')
        if not continuar.continuarNum():
            print('=============FIN DEL PROGRAMA==============')
            break
    else:
        print('el número ingresado debe ser positivo')
        if not continuar.continuarNum():
            print('=============FIN DEL PROGRAMA==============')
            break