""" Desafío 2
    Desarrollar un programa que cargue los datos de un triángulo. Implementar 
    una clase con los métodos para inicializar sus atributos, consultar la magnitud 
    del tamaño del lado mayor y consultar el tipo de triángulo que es
    (equilátero, isósceles o escaleno). 
"""

import continuar
import funcionesUtiles

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


    def tipo_triangulo(self):
        a, b, c = self.lado1, self.lado2, self.lado3
        if a != b and a != c and b != c:
            print('El triangulo es de Escaleno')
        elif a == b == c:
            print('El tringulo es Equilatero')
        else:
            print('El trinagulo es Isoceles')


    def lado_mayor(self):
        a, b, c = self.lado1, self.lado2, self.lado3
        if a > b and a > c:
            print(f'{self.lado1} es el lado mayor')
        elif b > a and b > c:
            print(f'{self.lado2} es el lado mayor')
        elif c > a and c > b: 
            print(f'{self.lado3} es el lado mayor')


    def desigualdad_triangular(self):
        a, b, c = self.lado1, self.lado2, self.lado3
        return (a + b > c) and (a + c > b) and (b + c > a)


    def validar_lados(self, mensaje):
        while True:
            lado = input(mensaje)
            if funcionesUtiles.es_flotante(lado) or funcionesUtiles.es_entero(lado):
                if funcionesUtiles.es_positivo(float(lado)):
                    print('Valor conrrecto')
                    return lado
                    break
                else:
                    print('El valor de cada lado debe ser un numero positivo')
            else:
                print('El valor de cada lado debe ser un número')


    def ingresar_lados(self):
        while True:
            self.lado1 = float(self.validar_lados('Ingrese el valor del primer lado del triángulo\n'))
            self.lado2 = float(self.validar_lados('Ingrese el valor del segundo lado del triángulo\n'))
            self.lado3 = float(self.validar_lados('Ingrese el valor del tercero lado del triángulo\n'))

            if self.desigualdad_triangular():
                print('Es un tringulo')
                break
            else:
                print('Error: Los numeros ingresados no cumplen la desigualdad triangular')
                

    def __str__(self):
        return f'Triángulo de lados: {self.lado1}, {self.lado2}, {self.lado3}'
        

def desafio_2():
    trinagulo1 = Triangulo()
    trinagulo1.ingresar_lados()
    trinagulo1.lado_mayor()
    trinagulo1.tipo_triangulo()
    print(trinagulo1)
    

while True:
    desafio_2()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break