"""Desafío 5
    Desarrollar un programa que, dado un número entero, muestre su valor absoluto. Nota:
    un valor absoluto siempre es positivo.
"""
def continuar():
    while True:
        conti  = input('Desea ingresar nuevamente un número? (si|no)\n').lower()
        if conti == 'no':
            print('=======FIN DEL PROGRAMA=======')
            exit()
        elif conti == 'si':
            break
        else:
            print('Ingresaste una opción incorrecta')

while True:
    numero = int(input('Ingrese un número entero (puede ser -/+)\n'))
    val_abs = numero * (-1)
    print(f'Se ingreso el numero {numero}')
    print(f'Su valor absoluto es: {val_abs}\n')
    continuar()

