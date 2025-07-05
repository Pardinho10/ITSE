""" Desafío 9
    Desarrollar una clase Circulo que contenga un radio, con 
    un método que retorne el área y otro que retorne el perímetro del Circulo. 
"""
import continuar
import math
from funcionesUtiles import es_flotante, es_entero

class Circulo():
    PI = math.pi
    def __init__(self, rad = 0):
        self.__radio = rad

    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, nuevo_radio):
        if nuevo_radio < 0:
            raise ValueError('El valor ingresado debe ser mayor o igual que 0')
        self.__radio = nuevo_radio


    def area(self):
        area = Circulo.PI * self.radio**2
        return area


    def perimetro(self):
        perimetro = 2 * Circulo.PI * self.radio
        return perimetro
        

    @staticmethod
    def menu():
        print('===================================')
        print('********OPERACIONES CIRCULO********')
        print('===================================')
        print('1 -CARGAR DATOS INICIALES')
        print('2 -CALCULAR AREA')
        print('3 -CALCULAR PERIMETRO')
        print('S o 0 - SALIR')


    def validar_valores(self, mensaje):
        while True:
            rad = input(mensaje)
            if not (es_flotante(rad) or es_entero(rad)):
                raise TypeError('El valor ingresado debe ser númerico')
            return float(rad)


    def datos_iniciales(self):
        try:
            self.radio = self.validar_valores('Ingrese el valor del radio para calcular\n')
        except (ValueError, TypeError) as e:
                    print(f'Error: {e}')


    def get_resultado(self, resultado, mensaje):
        print(f'El {mensaje} es: ---> {resultado}')

    def operar(self):
        while True:
            Circulo.menu()
            opc = input('Seleccione una operación\n').strip().lower()
            match opc:
                case '1':
                    self.datos_iniciales()
                case '2':
                    resultado = self.area()
                    self.get_resultado(resultado, 'área del circulo')
                case '3':
                    resultado = self.perimetro()
                    self.get_resultado(resultado, 'perimetro del circulo')
                case 's' | '0':
                    print('Saliendo del programa...')
                    return
                case _:
                    print('Error, opcion no valida')           


def desafio_9():
    circu = Circulo()
    circu.operar()


while True:
    desafio_9()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break  