"""Desafío 1
    Solicitar al usuario que ingrese su número de cliente. Si el número es el 1000, imprimir
    "Ganaste un premio"."""


band = True
while band == True:

    numCli = int(input(f'====Ingrsa tu número de cliente, para verificar si eres Ganador ====\n'))
    if numCli == 1000:
        print(f'Eres el cliente {numCli}, GANASTE UN PREMIO!!!\n')
    else:
        print(f'Eres el cliente {numCli}, Sigue participando\n')
    continuar = input('Deseas continuar (si/no)\n').lower()
    if continuar == 'no':
        band = False
        print('================Hasta el proximo sorteo================')
