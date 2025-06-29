""" Desafío 3
    Desarrollar un programa en el cual el Usuario ingrese dos valores enteros
    por teclado. Utilizar el método __init__. Incluir el calculo de la suma, resta, 
    multiplicación y división. 
    Utilizar un método para cada una de las operaciones. Nombrar a la clase Calculadora. 
"""

import continuar
import funcionesUtiles

class Calculadora():
    def __init__(self):
        self._numero_1 = None
        self._numero_2 = None

    @property
    def numero_1(self):
        return self._numero_1
    
    @numero_1.setter
    def numero_1(self, numero1):
        self._numero_1 = numero1

    @property
    def numero_2(self):
        return self._numero_2
    
    @numero_2.setter
    def numero_2(self, numero2):
        self._numero_2 = numero2

    def suma(self):
        suma = self.numero_1 + self.numero_2
        return suma
    
    def resta(self):
        resta =  self.numero_1 - self.numero_2
        return resta
    
    def multiplicacion(self):
        multi = self.numero_1 * self.numero_2
        return multi
    
    def division(self):
        if self.numero_2 != 0:
            divi = self.numero_1 / self.numero_2
            return divi
        else:
            print('Error: division entre cero no es permitida')

    def validar_valores(self, mensaje):
        while True:
            valor = input(mensaje)
            if funcionesUtiles.es_flotante(valor) or funcionesUtiles.es_entero(valor):                
                print('Valor correcto')
                return valor
                break                  
            else:
                print('El dato ingresado debe ser un número')

    def ingresar_valores(self):
        self.numero_1 = float(self.validar_valores('Ingrese el primer digito\n'))
        self.numero_2 = float(self.validar_valores('Ingrese el segundo digito\n'))

    @staticmethod
    def menu():
        print('===========================')
        print('********CALCULADORA********')
        print('===========================')
        print('1 - SUMA')
        print('2 - RESTA')
        print('3 - MULTIPLICACIÓN')
        print('4 - DIVISIÓN')
        print('S o 0 - SALIR')

def desafio_3():
    calcu = Calculadora()
    Calculadora.menu()
    opc = input('Seleccione una operación\n').strip()
     
    calcu.ingresar_valores()
    match opc:
        case '1':
            resultado = calcu.suma()
            print(f'El resultado de la suma es: ---> {resultado}')            
        case '2':
            resultado = calcu.resta()
            print(f'El resultado de la resta es: ---> {resultado}')   
        case '3':
            resultado = calcu.multiplicacion()
            print(f'El resultado del producto es: ---> {resultado}')   
        case '4':
            resultado = calcu.division()
            print(f'El resultado del cociente es: ---> {resultado}')  
        case 's' | '0':
            print('Saliendo del programa...')
            return
        case _:
            print('Error, opcin no validad')

while True:
    desafio_3()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break
   