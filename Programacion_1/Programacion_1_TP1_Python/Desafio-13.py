"""Desafío 13
    Imprimir los números entre el 5 y el 25, saltando de tres en tres.
"""

print('Listado de números entre 5 y 25 de 3 en 3')
print('=======FOR=========')
for i in range(5, 26, 3): #range(valor inicial, valor final, con paso...)
    print(i)

print('=========WHILE=========')
c = 5
while 5 <= c <= 25:
    print(c)
    c += 3