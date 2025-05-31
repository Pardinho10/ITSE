"""Desafío 39
    Desarrollar un algoritmo en donde se requiera al usuario que ingrese un texto largo y luego a ese mismo dato se le cuenten la cantidad de ocurrencias de cada una de las vocales. Tener en cuenta que cada vocal puede presentarse en mayúscula, minúscula o acentuada, de tal manera que se obtenga la siguiente información:
    cantidad de ocurrencias de la vocal a: ...
    cantidad de ocurrencias de la vocal e: ...
    cantidad de ocurrencias de la vocal i: ...
    cantidad de ocurrencias de la vocal o: ...
    cantidad de ocurrencias de la vocal u: ...
    cantidad total de vocales: ...
"""
import continuar
import unicodedata

#PERMITE EL INGRESO DE UNA CADENA Y LA NORMALIZA
def crear_cadena(mensaje):
    cadena = input(mensaje).lower().strip()
    cadena_normalizada = unicodedata.normalize('NFD', cadena)
    cadena_sin_acentos = ''.join(c for c in cadena_normalizada if unicodedata.category(c) != 'Mn')
    return cadena_sin_acentos

#CUENTA CANTIDAD DE VOCALES Y CONSONANTES
def cuenta_vocal(cadena):
    contA = contE = contI = contO = contU = cont_consonantes = 0
    for i in cadena:
        match i:
            case 'a':
                contA += 1
            case 'e':
                contE += 1
            case 'i':
                contI += 1
            case 'o':
                contO += 1
            case 'u':
                contU += 1
            case _:
                if i.isalpha(): # DEVUELEVE TRUE SI SE TRATA DE UNA LETRA NO VOCAL
                    cont_consonantes += 1
    contTotVoc = contA + contE + contI + contO + contU
    return contA, contE, contI, contO, contU, contTotVoc, cont_consonantes        

#FUNCION PRINCIPAL
def main():
    cadena = crear_cadena('Ingrese un texto largo\n')
    contA, contE, contI, contO, contU, contTotVoc, cont_consonantes  = cuenta_vocal(cadena)
    print(f'cantidad de ocurrencias de la vocal a: {contA}')
    print(f'cantidad de ocurrencias de la vocal e: {contE}')
    print(f'cantidad de ocurrencias de la vocal i: {contI}')
    print(f'cantidad de ocurrencias de la vocal o: {contO}')
    print(f'cantidad de ocurrencias de la vocal u: {contU}')
    print(f'cantidad total de vocales: {contTotVoc}')
    print(f'cantidad consonantes: {cont_consonantes}')

while True:
    main()
    if not continuar.continuarGen():
        print('=============FIN DEL PROGRAMA==============')
        break