"""Desafío 15
    Desarrollar un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. En cada iteración, solicitar al usuario que ingrese un número. Al finalizar, mostrar la suma de todos los números ingresados.
"""

N = int(input('Ingrese la cantidad de números a iterar\n'))
suma = 0;
for i in range(N):
    numero = int(input('Ingrese un número\n'));
    suma  = suma + numero;
print(f'La suma de los número ingresados es: {suma}');