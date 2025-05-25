"""Desafío 16
    Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).
"""

import continuar
while True:
    frase = input('Ingrse una frase a analizar\n').lower().strip()
    tupVoc = []
    for letra in frase:
        print(letra)
        if letra in ('a', 'e', 'i', 'o', 'u'):
            print(f'Concidencia!! encontramos la vocal:  {letra}')
            tupVoc.append(letra)
    print(F'Listado de vocales encontradas: {tupVoc}')
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break