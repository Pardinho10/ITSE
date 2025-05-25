"""Desafío 18
    Desarrollar un programa que muestre la sumatoria de todos los números entre el 0 y el 30.
"""
print('===========FOR============')
sum = 0
for i in range(31):
    sum = sum + i
print(f'La sumatoria de los números de 0 a 30 es: {sum}')

print('===========WHILE===========')
c = 0
sum = 0
while 0 <= c <= 30:
    sum = sum + c
    c += 1
print(f'La sumatoria de los números de 0 a 30 es: {sum}')
