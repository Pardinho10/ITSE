"""Desafío 25
    Dada una lista no vacía de números enteros, cada numero aparece dos veces, excepto
    uno de ellos. El algoritmo debe encontrar cual de ellos no se repite.
"""

numeros = [2,45, 23, 4, 76, 12, 45, 23, 76, 2, 12]
print(f'Dada la siguiente lista ---> {numeros}')
print('Encontrar el numero que no se repite\n')
band = False
if len(numeros) != 0:
    for i in numeros:
        if numeros.count(i) == 1:
             print(f'El número que se repite 1 vez es el {i}') 
        else:
            print(f'El número {i} se repite 2 veces')
else:
    print('La lista no debe estar vacia\n')