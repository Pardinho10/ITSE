"""Desafío 17
    Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en dicha frase.
"""

import continuar
while True:
    frase = input('Ingrse una frase a analizar\n').lower().strip()
    tupVoc = []
    contVoc = 0
    for letra in frase:
        if letra in ('a', 'e', 'i', 'o', 'u'):
            contVoc += 1
            print(f'Se econtro la vocal: {letra} y es la vocal numero {contVoc} encontrada \n')
    print(F'Total de vocales encontradas: {contVoc}')
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break