import random
#FUNCION QUE VALIDA ENTEROS (POSITIVOS  Y NEGATIVOS)
def es_entero(valor):
    return valor.lstrip('-').isdigit() and valor != '-'

#FUNCION QUE VALIDA FLOTANTES (POSITIVOS  Y NEGATIVOS)
def es_flotante(valor):
    if valor.count('.') != 1:
        return False
    if valor.startswith('-'):
        valor = valor[1:]  # elimina el signo negativo
    parte_entera, parte_decimal = valor.split('.')
    return parte_entera.isdigit() and parte_decimal.isdigit()

#FUNCION QUE VERIFICA QUE EL VALOR SEA POSITIVO
def es_positivo(num1):
    return num1 >= 0 

#======================FECHAS

#SEPARACION DE LA CADENA FECHA
def ingresar_fechas(mensaje):
    fecha = input(mensaje).capitalize().strip()
    dia = fecha.split(', ')[0]
    dia_numero = int(fecha.split(', ')[1].split('/')[0])
    mes = int(fecha.split('/')[1])
    
    if validar_fecha(dia, dia_numero, mes ):        
        return dia, dia_numero, mes 
    else:
        return None

#VALIDACION DE LA FECHA 
def validar_fecha(dia, dia_numero, mes):
    dia_habiles = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    if dia in dia_habiles and (dia_numero > 0 and dia_numero <= 31) and (mes > 0 and mes <= 12):
        print('Fecha valida')
        return True
    elif dia in ('Domingo', 'Sabado'):
        print('Sabado y Domingo son dias no laborables')
    elif dia_numero < 0 or dia_numero > 31:
        print(f'Dia {dia_numero} no es un día de mes valido')
    elif mes < 0 or mes > 12:
        print(f'Mes {mes} no es un mes valido')
    else:
        print('dia invalido')
    return False
#======================FECHAS

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