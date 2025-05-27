"""Desafío 22
    Desarrollar un programa que permita al usuario ingresar 6 números enteros, que
    pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números
    negativos y el promedio de los positivos.
    No olvides que no es posible dividir por cero, por lo que es necesario evitar que el
    programa arroje un error si no se ingresaron números positivos.
"""
import continuar

while True:
    cont = 1
    sumP = 0
    sumN = 0
    contP = 0
    promP = 0.0
    bandN = False
    N = int(input('Ingrese la cantidad de números a analizar\n'))

    for i in range(N):
        numero = int(input('Ingrese un número (Positivo | Negativo)\n'))
        print(numero)
        print(i)
        if numero > 0:
            contP = contP + 1
            sumP = sumP + numero
        elif numero < 0:
            bandN = True
            sumN = sumN + numero
        else:
            print('Se ingreso un valor 0')
    if N > 0:
        if contP > 0:
            promP = sumP / contP
            print(f'Promedio de números positivos: {promP}')
        else:
            print('No se ingresaron números positivos')
        if bandN == True:
            print(f'La suma de los números negativos es: {sumN}')
        else:
            print('No se ingresaron números negativos')
    if not continuar.continuarNum():
        print('===========FIN DEL PROGRAMA===========')
        break
