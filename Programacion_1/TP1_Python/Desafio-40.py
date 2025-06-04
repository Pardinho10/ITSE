"""Desafío 40
Desarrollar un algoritmo en donde se informe el volumen, en litros, de un contenedor de tipo prisma rectangular, esfera o cilíndrico.
Para realizar dichos cálculos se requerirá al usuario que primero seleccione el tipo de contenedor ingresando la opción correspondiente y luego se pidan los datos requeridos para el cálculo de ese contenedor en particular.
Tips: se sugiere, que se presente un Menú de Opciones que luzca de la siguiente
forma:
 Menú de Opciones
-----------------------------------------------------------
1 - Calcular volumen contenedor prisma rectangular
2 - Calcular volumen contenedor esférico
3 - Calcular volumen contenedor cilíndrico
s - Salir"""

import continuar
import math

# FUNCIÓN PARA CALCULAR VOLUMEN DE UN PRISMA RECTANGULAR
def volumen_prisma():
    print('\nPRISMA RECTANGULAR')
    largo = float(input('Ingrese el largo (en metros): '))
    ancho = float(input('Ingrese el ancho (en metros): '))
    alto = float(input('Ingrese la altura (en metros): '))
    volumen_m3 = largo * ancho * alto
    volumen_litros = volumen_m3 * 1000  # 1 m³ = 1000 litros
    print(f'VOLUMEN: {volumen_litros:.2f} litros\n')

# FUNCIÓN PARA CALCULAR VOLUMEN DE UNA ESFERA
def volumen_esfera():
    print('\nESFERA')
    radio = float(input('Ingrese el radio (en metros): '))
    volumen_m3 = (4 / 3) * math.pi * radio**3
    volumen_litros = volumen_m3 * 1000
    print(f'VOLUMEN: {volumen_litros:.2f} litros\n')

# FUNCIÓN PARA CALCULAR VOLUMEN DE UN CILINDRO
def volumen_cilindro():
    print('\nCILINDRO')
    radio = float(input('Ingrese el radio de la base (en metros): '))
    altura = float(input('Ingrese la altura (en metros): '))
    volumen_m3 = math.pi * radio**2 * altura
    volumen_litros = volumen_m3 * 1000
    print(f'VOLUMEN: {volumen_litros:.2f} litros\n')

# FUNCIÓN QUE MUESTRA EL MENÚ Y LLAMA A LA OPCIÓN SELECCIONADA
def menu():
    while True:
        print('==============================')
        print('     MENÚ DE OPCIONES')
        print('==============================')
        print('1 - Calcular volumen contenedor prisma rectangular')
        print('2 - Calcular volumen contenedor esférico')
        print('3 - Calcular volumen contenedor cilíndrico')
        print('s - Salir')
        print('------------------------------')

        opcion = input('Seleccione una opción: ').lower()

        if opcion == '1':
            volumen_prisma()
        elif opcion == '2':
            volumen_esfera()
        elif opcion == '3':
            volumen_cilindro()
        elif opcion == 's':
            print('FIN DEL PROGRAMA')
            break
        else:
            print('Opción inválida. Intente nuevamente.\n')

# PROGRAMA PRINCIPAL
while True:
    menu()
    if not continuar.continuarGen():
        print('=============FIN DEL PROGRAMA==============')
        break
