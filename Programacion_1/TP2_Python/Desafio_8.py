""" Desafío 8
    Desarrollar una clase Rectangulo que contenga una base y 
    una altura y un método que retorne el área del rectángulo. 
"""

import continuar
from funcionesUtiles import es_flotante, es_entero

class Rectangulo():
    def __init__(self, base = 0, altura = 0):
        self.__base = base
        self.__altura = altura
    @property
    def base(self):
        return self.__base
    @property
    def altura(self):
        return self.__altura
    
    @base.setter
    def base(self, nueva_base):
        self.__base = nueva_base

    @altura.setter
    def altura(self, nueva_altura):
        self.__altura = nueva_altura

    def area(self):
        area = self.base * self.altura
        return area

    def perimetro(self):
         peri = (self.base * 2) + (self.altura * 2)
         return peri

    @staticmethod
    def menu():
        print('======================================')
        print('********OPERACIONES RECTANGULO********')
        print('======================================')
        print('1 -CARGAR DATOS INICIALES')
        print('2 -CALCULAR AREA')
        print('3 -CALCULAR PERIMETRO')
        print('S o 0 - SALIR')


    def validar_valores(self, mensaje):
        while True:
            valor = input(mensaje)
            if not (es_flotante(valor) or es_entero(valor)):
                raise TypeError('El valor ingresado debe ser númerico')
            return float(valor)


    def datos_iniciales(self):
        try:
            self.base = self.validar_valores('Ingrese el valor de base para calcular\n')
            self.altura = self.validar_valores('Ingrese el valor de altura para calcular\n')
        except (ValueError, TypeError) as e:
                    print(f'Error: {e}')

    def get_resultado(self, resultado, mensaje):
        print(f'El {mensaje} es: ---> {resultado}')

    def operar(self):
        while True:
            Rectangulo.menu()
            opc = input('Seleccione una operación\n').strip().lower()
            match opc:
                case '1':
                    self.datos_iniciales()
                case '2':
                    resultado = self.area()
                    self.get_resultado(resultado, 'área del rectangulo')
                case '3':
                    resultado = self.perimetro()
                    self.get_resultado(resultado, 'perimetro del rectangulo')
                case 's' | '0':
                    print('Saliendo del programa...')
                    return
                case _:
                    print('Error, opcion no valida')   



def desafio_8():
    rect = Rectangulo()
    rect.operar()

while True:
    desafio_8()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break  