"""Desafío 33
    Desarrollar una función que reciba como entrada una lista y retorne otra lista con los números sumados más uno
"""
import continuar

#FUNCION QUE VALIDA ENTEROS (POSITIVOS  Y NEGATIVOS)
def es_entero(valor):
    return valor.lstrip('-').isdigit() and valor != '-'

#FUNCION QUE CREA UNA NUEVA LISTA CON LOS ELEMENTOS DE LA PRIMRA SUMADOS 1
def lista_mas_uno(lista_num):
    lista_num_mas1 = []
    for x in lista_num:
        numero_mas_uno = x + 1
        lista_num_mas1.append(numero_mas_uno)
    return lista_num_mas1

#FUNCION PRINCIPAL
def main():
    lista_num = []
    N = int(input('Ingrese la cantidad de valores que se guardaran en la lista\n')) 

    for i in range(N):
        numero = input('Ingrese valores que seran guardados en la lista\n')
        if es_entero(numero):
            lista_num.append(int(numero))
        else:
            print('El valor ingresado no es un numero entero valido\n')

    print(f'Lista oroginal ---> {lista_num}')
    lista_final = lista_mas_uno(lista_num)
    print(f'Lista modificada con elementos sumados más 1 ---> {lista_final}')

while True:
    #LLAMADO A LA FUNCION PRINCIPAL
    main()
    if not continuar.continuarGen():
        print('=============FIN DEL PROGRAMA==============')
        break


