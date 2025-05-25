"""Desafío 3
    Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor.
    Considerar el caso en que ambos números son iguales."""

band = True
while band == True:
    igual = False
    print('\n== Ingresá 2 nuúmeros, veamos cual es el menor de ambos ==')
    num1 = int(input('Ingrese el primer numero\n'))
    num2 = int(input('Ingrese el segundo numero\n'))
    if num1 != num2:
        if num1 < num2:
            menor = num1
        else:
            menor = num2
    else:
        igual = True
    print(f'\nNumeros que ingresaste: {num1} y {num2}')
    if igual == True:
        print('Los números son iguales')
    else:
        print(f'El menor de los números ingresados es: {menor}\n')
    continuar = input('Desea ingresar números nuevamente? (si|no) \n')

    if continuar == 'no':
        band = False
        print('==== FIN DEL PROGRAMA ====')


