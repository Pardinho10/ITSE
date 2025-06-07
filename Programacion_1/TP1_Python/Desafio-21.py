"""Desafío 21
    Desarrollar un algoritmo que muestre los primeros 100 números de la Sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
"""
import continuar
while True:
    a = 0
    b = 1
    sig = 0
    cont = 1
    serie_fibo = []
    numero = int(input('Ingrese la cantidad de valores de la Serie de Fibonacci que desea ver (Valor Positivo mayor a 0)\n'))
    if numero > 0:
        while cont <= numero:
            serie_fibo.append(str(a))
            sig = a + b
            a = b
            b = sig
            cont += 1
        resultado = ' | '.join(serie_fibo)
        print(f"Primeros {numero} números de la Serie de Fibonacci: --->  {resultado}")
    else:
        print('El número ingresado debe ser positivo y mayor a 0\n')

    if not continuar.continuarNum():
        print('===========FIN DEL PROGRAMA===========')
        break
    