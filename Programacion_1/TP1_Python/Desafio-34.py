"""Desafío 34
    Calcular el dato estadístico mediana de una lista dada. Si la lista es de longitud impar, retorna el valor mediana de la misma. Si la lista es de longitud par, retorna el promedio de los dos valores mediana. Si la lista está vacía lanzar una excepción ValueError.
"""
import continuar
import random


#FUNCION PRINCIPAL
def main():
    lista_med, N = generar()
    lista_med_ord = ordenar(lista_med)    
    mit = len(lista_med_ord)/2
    print(mit)    
    print(f'Lista generada ---> {lista_med}')
    print(f'Lista generada y ordenada ---> {lista_med_ord}')
    mitad(N, lista_med_ord)

#GENERAR LISTA CON ELEMENTOS ALEATORIOS
def generar():
    lista_med = []
    N = int(input('Ingrese la cantidad de valores que se guardaran en la lista\n')) 
    for i in range(N):
        numero = random.randint(0,100)        
        lista_med.append(numero)
    return lista_med, N

#FUNCION QUE ORDENA LA LISTA EN FORMA ASCENDENTE
def ordenar(lista_med):
    lista_med_ord = sorted(lista_med)
    return lista_med_ord

#FUNCION QUE CALCULA LA MEDIANA DE UNA LISTA
def mitad(N, lista_med_ord):
    if N % 2 == 0:
        print('La longitud es par')
        med1 = lista_med_ord[int(len(lista_med_ord)/2) - 1]
        med2 = lista_med_ord[int(len(lista_med_ord)/2)]
        prom_med = (med1 + med2) / 2
        print(f'La mediana del la lista es: {prom_med}')
    else:
        print('La longitud es impar')
        mediana = int(len(lista_med_ord)/2)
        print(f'La mediana del la lista es: {lista_med_ord[mediana]}')

while True:
    main()
    if not continuar.continuarGen():
        print('=============FIN DEL PROGRAMA==============')
        break
