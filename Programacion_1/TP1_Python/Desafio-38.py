"""Desafío 38
    Desarrollar un algoritmo en donde se requiera al usuario que ingrese un nombre y luego a ese mismo dato se lo presente, separado por un espacio en blanco, 30 veces repetido en una misma línea de la pantalla.
"""

import continuar

def main():
    nombre = input('Ingrese una nombre de persona\n').strip()
    print(f'El nombre ingresado es: ---> {nombre}')
    x = " ".join([nombre] * 30)
    print(f'El nombre multplicado por 30 es: ---> {x} ')


while True:
    main()
    if not continuar.continuarGen():
        print('=============FIN DEL PROGRAMA==============')
        break
