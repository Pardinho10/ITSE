import random
#FUNCION QUE VALIDA ENTEROS (POSITIVOS  Y NEGATIVOS)
def es_entero(valor):
    return valor.lstrip('-').isdigit() and valor != '-'

#FUNCION QUE VERIFICA QUE LOS VALORES SEAN POSITIVOS
def es_positivo(num1, num2):
    return num1 >= 0 and num2 >= 0

#FUNCION MULTIPLICACIÓN SIN SUMAS
def multiSuma (num1, auxiliar):    
    cont = 1
    suma  = 0
    while cont < auxiliar:    
        suma = suma + num1
        cont += 1       
    return suma + num1

def generaLisNum():
    lista_num = []
    N = int(input('Ingrese la cantidad de valores que se guardaran en la lista\n'))
    for i in range(N):
        numero = input('Ingrese valores que seran guardados en la lista\n')
        if es_entero(numero):
            lista_num.append(int(numero))
        else:
            print('El valor ingresado no es un numero entero valido\n')

#GENERAR LISTA CON ELEMENTOS ALEATORIOS
def generarLisAlea():
    lista_med = []
    N = int(input('Ingrese la cantidad de valores que se guardaran en la lista\n')) 
    for i in range(N):
        numero = random.randint(0,100)        
        lista_med.append(numero)
    return lista_med, N