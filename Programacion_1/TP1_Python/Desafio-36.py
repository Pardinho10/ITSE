"""Desafío 36
    Desarrollar la función cuadrado_perfecto que reciba un numero entero positivo en una
    variable de nombre numero. Luego la función debe retornar la lista de los numero
    cuadrado perfectos que no sean números pares.
"""

import continuar
import funcionesUtiles

#FUNCION PRINCIPAL
def main():
    num = input('Ingrese un número entero positivo\n')
    if funcionesUtiles.es_entero(num) and int(num) > 0:
        numero = int(num)
        cuadrado_perfecto(numero)

def cuadrado_perfecto(numero):
    lista_result = []
    for i in range(numero):
        cuadrado = i**2
        if cuadrado % 2 != 0:
            lista_result.append(cuadrado) 
        if cuadrado > numero:
            break
    print(f'La lista con los cuadrados perfectos hasta el {numero} ---> {lista_result}')

while True:
    #LLAMADO A LA FUNCION PRINCIPAL
    main()
    if not continuar.continuarGen():
        print('=============FIN DEL PROGRAMA==============')
        break