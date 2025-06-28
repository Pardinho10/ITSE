""" Desafío 2
    Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar sus atributos, consultar la magnitud del tamaño del lado mayor y consultar el tipo de triángulo que es (equilátero, isósceles o escaleno). 
"""
class Triangulo():
    def __init__(self):
        self._lado1 = None
        self._lado2 = None
        self._lado3 = None

    @property
    def lado1(self):
        return self._lado1
    
    @lado1.setter
    def lado1(self, lado):
        self._lado1 = lado

    @property
    def lado2(self):
        return self._lado2
    
    @lado2.setter
    def lado2(self, lado):
        self._lado2 = lado

    @property
    def lado3(self):
        return self._lado3
    
    @lado3.setter
    def lado3(self, lado):
        self._lado3 = lado
    
    def validar_lado(self, mensaje):
         while True:
            lado = input(mensaje)
           


    def ingresar_lados(self):
        l1 = self.validar_lado('Ingrese el primer lado del triangulo')
        