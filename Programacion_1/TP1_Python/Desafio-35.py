"""Desafío 35
    Intercambia los valores de dos variables de tipo entero sin utilizar una tercera variable.
"""
import continuar
import funcionesUtiles

while True:
    n1 =  input('Ingresar el primer número\n')
    n2 =  input('Ingresar el segundo número\n')
    print(f'el primer valor ingresado es -> {n1}, el segundo es -> {n2}')
    if funcionesUtiles.es_entero(n1) and funcionesUtiles.es_entero(n2):  
        num1 = int(n1)    
        num2 = int(n2)
        num1 = num1^num2 
        num2 = num1^num2 # (num1^num2) ^ num2 -> num1
        num1 = num1^num2 # (num1^num2) ^ num1 -> num2

        print(f'el primer valor ingresado es -> {num1}, el segundo es -> {num2}')
    else:
        print('Se deben ingresar numeros enteros unicamente')
    if not continuar.continuarGen():
        print('=============FIN DEL PROGRAMA==============')
        break

