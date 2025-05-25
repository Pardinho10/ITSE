"""Desafío 2
    Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. No considerar el caso en que ambos números son iguales."""
band = True
while band == True:
    print('\n== Ingresá 2 nuúmeros, veamos cual es el menor de ambos == \n')
    num1 = int(input('Ingrese el primer numero\n'))
    num2 = int(input('Ingrese el segundo numero\n'))

    if num1 < num2:
        menor = num1
    else:
        menor = num2
    print(f'\nNumeros que ingresaste: {num1} y {num2}')
    print(f'El menor de los números ingresados es: {menor}')
    conti = input('Deseas cargar números nuevamente (si/no)\n').lower()
    if conti == 'no':
        band = False
        print('==== FIN DEL PROGRAMA ====')