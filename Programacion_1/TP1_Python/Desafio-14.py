"""Desafío 14
    Solicitar al usuario que ingrese un número entero positivo e imprimir todos los números correlativos entre el ingresado por el usuario y uno menos del doble del mismo.
"""
#range(num, num*2) genera los números entre el ingresado por el usuario y uno menos del doble del mismo.

#str(i) for i in range(...) convierte cada número a texto (porque .join() solo funciona con strings).

#" ".join(...) une todos esos textos con un espacio entre ellos.
import continuar

while True:
    num = int(input('Ingrese un número entero positivo\n'))
    if num >= 0:
         print("-".join(str(i) for i in range(num, num*2)))
    else:
          print('El número ingresado no es positivo')
    if not continuar.continuarNum():
            print('===========FIN DEL PROGRAMA==============')
            break