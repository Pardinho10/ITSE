"""Desafío 4
    Solicitar al usuario que ingrese un número de día de la semana e imprimir un mensaje con su nombre correspondiente. Considerar que la semana comienza el domingo. Si el  día ingresado no es correcto, imprimir un mensaje de error. Ejemplo: el número 2 corresponde al Lunes.
"""

dias_semana = ['Sábado','Domingo', 'Lunes', 'Martes', 'Miercoles','Jueves', 'Viernes' ]
while True:
    encontrado = False
    num_dia = int(input('Ingrese el un numero de día de la semana (1-7)\n'))
    for i in range(len(dias_semana)):        
        if num_dia == i:
            print(f'el dia elegido es: {dias_semana[i]}')
            encontrado = True
    if encontrado == False:
        print('No se encontro el dia correspondiente\nSe ha ingresado un valor incorrecto')
    while True:
        conti  = input('Desea ingresar nuevamente un número? (si|no)\n').lower().strip()
        if conti == 'no':
            print('=======FIN DEL PROGRAMA=======')
            exit()
        elif conti == 'si':
            break
        else:
            print('Ingresaste una opción incorrecta')