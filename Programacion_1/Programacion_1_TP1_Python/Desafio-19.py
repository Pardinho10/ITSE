"""Desafío 19
    Desarrollar un programa que muestre la sumatoria de todos los múltiplos de 3
    encontrados entre el 0 y el 100.
"""

sum = 0
for i in range (0, 101):
    if i % 3 == 0:
        sum += i
        print(f'{i} es multiplo de 3')
    else:
        print(f'{i} no es multiplo de 3')
print(f'La sumatoria de los números de 0 a 100 multiplos de 3 es: {sum}')