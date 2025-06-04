"""Desafío 28
Encriptar un mensaje utilizando el método de “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “HOLA” se transforma en “JQNC”.
Si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”."""

import continuar

# SOLICITA AL USUARIO UN MENSAJE PARA ENCRIPTAR
def solicitar_mensaje():
    return input('INGRESE EL MENSAJE A ENCRIPTAR:\n')


# SOLICITA EL VALOR DE CORRIMIENTO Y LO VALIDA
def solicitar_corrimiento():
    while True:
        try:
            c = int(input('INGRESE LA CANTIDAD DE POSICIONES PARA CORRER LAS LETRAS:\n'))
            if c >= 0:
                return c % 26  # AJUSTA EL VALOR ENTRE 0 Y 25
            else:
                print('EL VALOR DEBE SER POSITIVO.')
        except ValueError:
            print('DEBE INGRESAR UN NÚMERO ENTERO.')


# DEFINICIÓN DEL ABECEDARIO (SOLO LETRAS INGLESAS, SIN Ñ)
def cifrado_cesar(mensaje, corrimiento):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''

    # RECORRE CADA CARÁCTER DEL MENSAJE
    for letra in mensaje:
        if letra.lower() in abecedario:
            # OBTIENE EL ÍNDICE DE LA LETRA Y CALCULA EL NUEVO ÍNDICE CON CORRIMIENTO
            indice_actual = abecedario.index(letra.lower())
            nuevo_indice = (indice_actual + corrimiento) % 26
            nueva_letra = abecedario[nuevo_indice]

            # RESPETA LAS MAYÚSCULAS
            if letra.isupper():
                resultado += nueva_letra.upper()
            else:
                resultado += nueva_letra
        else:
            # SI NO ES UNA LETRA, LA AGREGA SIN CAMBIOS
            resultado += letra

    return resultado

# FUNCIÓN PRINCIPAL
def main():
    mensaje = solicitar_mensaje()
    corrimiento = solicitar_corrimiento()

    mensaje_encriptado = cifrado_cesar(mensaje, corrimiento)

    print('\nMENSAJE ENCRIPTADO:')
    print(mensaje_encriptado)


# BUCLE PRINCIPAL
while True:
    main()
    if not continuar.continuarGen():
        print('========FIN DEL PROGRAMA=======')
        break
