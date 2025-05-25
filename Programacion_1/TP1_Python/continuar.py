def continuarNum():
    while True:
        conti  = input('Desea ingresar nuevamente un número? (si|no)\n').lower().strip()
        if conti == 'no':
            return False
        elif conti == 'si':
            return True
        else:
            print('Ingresaste una opción incorrecta')

def continuarGen():
    while True:
        conti  = input('Desea continuar? (si|no)\n').lower().strip()
        if conti == 'no':
            return False
        elif conti == 'si':
            return True
        else:
            print('Ingresaste una opción incorrecta')