"""Desafío 30
    Sumar dos números enteros sin utilizar el operador de suma.
"""
import continuar

def main():
    print('Ingrese dos números enteros para sumarlos sin usar el operador "+"')
    a = int(input('Ingrese el primer número entero:\n'))
    b = int(input('Ingrese el segundo número entero:\n'))

    resultado = suma_sin_mas(a, b)
    print(f'La suma de {a} y {b} es: {resultado}\n')


def suma_sin_mas(a, b):
    # Manejamos números negativos usando complemento a dos en 32 bits
    MAX = 0xFFFFFFFF
    MASK = 0x7FFFFFFF

    while b != 0:
        carry = (a & b) & MAX      # bits donde ambos tienen 1
        a = (a ^ b) & MAX          # suma sin llevar
        b = (carry << 1) & MAX     # llevamos el carry a la izquierda

    # Si el resultado es negativo en 32 bits, lo convertimos
    return a if a <= MASK else ~(a ^ MAX)


#LLAMADO A LA FUNCION PRINCIPAL
while True:
    main()
    if not continuar.continuarGen():
        print('========FIN DEL PROGRAMA=======')
        break

