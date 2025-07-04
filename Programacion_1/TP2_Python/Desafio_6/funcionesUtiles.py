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
    return num1 > 0 

#FUNCION QUE VERIFICA SI TENEMOS UA CADENA
def es_cadena(valor):
    valor = valor.strip()
    return valor.replace(' ', '').isalpha() and len(valor) > 0
