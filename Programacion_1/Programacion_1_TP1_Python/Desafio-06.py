"""Desafío 6
    Solicitar al usuario que ingrese los nombres de dos personas, los cuales se
    almacenarán en dos variables. A continuación, imprimir “coincidencia” si los nombres
    de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Si
    no es así, imprimir “no hay coincidencia”.
"""
import continuar

while True:
    nombreA = input('Ingrese el primer nombre\n').lower().strip()
    nombreB = input('Ingrese el segundo nombre\n').lower().strip()
    print(len(nombreB))
    print(len(nombreA))      
    if nombreB[0] == nombreA[0] and nombreB[-1] == nombreA[-1]:
        print(f'Coincidencia!!\n')
        primera = nombreA[0] + ' - ' + nombreB[0]
        segunda = nombreA[-1] + ' - ' + nombreB[-1]
        print(f'Las primeras y ultimas letras de ambas palabras coinciden : {primera} y {segunda}')
    elif nombreB[0] == nombreA[0]:
        primera = nombreA[0] + ' - ' + nombreB[0]
        print(f'Las primeras letras de ambas palabras son iguales: {primera}')
    else:
        segunda = nombreA[-1] + ' - ' + nombreB[-1]
        print(f'Las ultimas letras de ambas palabras son iguales: {segunda}')
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA==============')
        break



