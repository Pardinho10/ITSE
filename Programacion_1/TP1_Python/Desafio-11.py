"""Desafío 11
Imprimir todos los dígitos enteros, del 0 al 9, utilizando una repetición"""

print('===WHILE===')
i = 0
while 0 <= i <= 9:
    print(f'{i}')
    i += 1

print('===FOR===')
for i in range(10):
    print(f'{i}')