"""Desafío 32
    Desarrollar la función potencia sin utilizar los operadores de multiplicación o división.
"""
import continuar

#SOLICITA AL USUARIO UN ENTERO Y LO RETORNA
def pedir_numero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.lstrip('-').isdigit():
            return int(entrada)
        else:
            print('Por favor ingrese un número válido')

#FUNCION QUE VERIFICA QUE LOS VALORES SEAN POSITIVOS
def es_positivo(num1, num2):
    return num1 >= 0 and num2 >= 0

#FUNCION QUE REALZA LA POTENCIA DE 2 NÚMEROS SIN OPERANDOS DE MULTIPLICACION
def potencia(base, exponente):
    cont1 = 1
    auxiliar = base
    if base != 0 and exponente != 0:
        while cont1 < exponente:    
            auxiliar = multiSuma(base, auxiliar)        
            cont1 += 1
        return auxiliar
    else:
        return potCero(exponente)
    
#FUNCION MULTIPLICACIÓN SIN SUMAS
def multiSuma (base, auxiliar):    
    cont = 1
    suma  = 0
    while cont < auxiliar:    
        suma = suma + base
        cont += 1       
    return suma + base

#FUNCION POTENCIAS CON BASE Y/O EXPONENTE CERO
def potCero(exponente):
    if exponente == 0:
        return 1
    else:
        return 0

#FUNCION PRINCIPAL
def main():
    while True:
        base = pedir_numero('Ingrese el número que representa la base de la potencia\n')
        exponente = pedir_numero('Ingrese el número que representa el exponente de la potencia\n')
        if es_positivo(base, exponente):
            resultado_pot = potencia(base, exponente)
            print(f'\n{base} elevado a la {exponente} es --->  {resultado_pot}')
            break
        else:
            print('Ambos números deben ser positivos. Intente nuevamente\n')


while True:
    #LLAMADO A LA FUNCION PRINCIPAL
    main()
    if not continuar.continuarNum():
        print('=============FIN DEL PROGRAMA==============')
        break
