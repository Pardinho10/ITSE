"""Desafío 23
Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos
equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y
los otros 5 son sus “oficiales”. La regla más importante del juego es que sólo se
comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.
Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una vez que se llegó a la “z”:(índice de la letra a correr+corrimiento) % 27.
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación."""

import continuar

def main():
    print('Este programa encriptará 5 mensajes usando el cifrado César.\n')
    corrimiento = solicitar_corrimiento()
    print(f'\nCorrimiento seleccionado: {corrimiento} posiciones\n')

    for i in range(1, 6):
        mensaje = input(f'Ingrese el mensaje secreto para el oficial {i}:\n')
        mensaje_encriptado = cifrado_cesar(mensaje, corrimiento)
        print(f'Mensaje encriptado: {mensaje_encriptado}\n')


def solicitar_corrimiento():
    while True:
        try:
            c = int(input('Ingrese el valor de corrimiento (entero positivo):\n'))
            if c >= 0:
                return c % 27  # evitar corrimientos mayores a 27
            else:
                print('Debe ser un número positivo.')
        except ValueError:
            print('Error: debe ingresar un número entero válido.')


def cifrado_cesar(mensaje, corrimiento):
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'  # 27 letras
    encriptado = ''

    for caracter in mensaje:
        if caracter.lower() in abecedario:
            minuscula = caracter.islower()
            index = abecedario.index(caracter.lower())
            nuevo_index = (index + corrimiento) % 27
            nueva_letra = abecedario[nuevo_index]
            encriptado += nueva_letra if minuscula else nueva_letra.upper()
        else:
            encriptado += caracter  # dejar espacios, signos, números, etc.

    return encriptado


# Programa principal
while True:
    main()    
    if not continuar.ccontinuarGen():
        print('========FIN DEL PROGRAMA=======')
        break
