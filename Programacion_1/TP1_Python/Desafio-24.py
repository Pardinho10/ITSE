"""Desafío 25
    Dada una lista no vacía de números enteros, cada numero aparece dos veces, excepto
    uno de ellos. El algoritmo debe encontrar cual de ellos no se repite.
"""

numeros = [2,45, 23, 4, 76, 12, 45, 23, 76, 2, 12]
print(f'Dada la siguiente lista ---> {numeros}')
print('Encontrar el numero que no se repite\n')

if len(numeros) != 0:
    for i in numeros:
        for x in numeros:
            print(f'el valor de i: {i} y el valor de x: {x}')
else:
    print('La lista no debe estar vacia\n')