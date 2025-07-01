"""  Desafío 7
    Desarrollar una clase Persona. Sus atributos son: nombre, edad y DNI. Incluir los siguientes métodos para la clase:
    * Un constructor, donde los datos pueden estar vacíos.
    * Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
    * Mostrar(): Muestra los datos de la persona.
    * es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad. 
"""
import continuar
from funcionesUtiles import es_cadena, es_entero, es_flotante, es_positivo
class Persona():
    def __init__(self, nombre=None, apellido=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__DNI = dni

    @property 
    def nombre(self):
        return self.__nombre     
       
    @property 
    def apellido(self):
        return self.__apellido        
        
    @property 
    def edad(self) :
        return self.__edad
    
    @property 
    def DNI(self): 
        return self.__DNI
    
    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError('El nombre debe ser una cadena de texto')
        if len(nombre.strip()) < 3 or len(nombre.strip()) > 30:
            raise ValueError("El nombre debe tener al menos 3 caracteres y no más de 30")
        self.__nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        if not isinstance(apellido, str):
            raise TypeError('El apellido debe ser una cadena de texto')
        if len(apellido.strip()) < 3 or len(apellido.strip()) > 30:
            raise ValueError("El apellido debe tener al menos 3 caracteres y no más de 30")
        self.__apellido = apellido

    @edad.setter
    def edad(self, edad):
        if not isinstance(edad, int):
            raise TypeError('La edad debe ser un numero entero')
        if edad < 0 or edad > 120:
            raise TypeError('La edad debe ser un entero entre 0 y 120 años')
        self.__edad = edad

    @DNI.setter
    def DNI(self, documento):
        if not isinstance(documento, int):
            raise TypeError ('El DNI debe ser un número entero')
        if documento < 1000000 or documento > 99999999:
            raise ValueError('El DNI debe ser un entero entre 1000000 y 99999999')
        self.__DNI = documento


    def ingresar_datos_persona(self):
        while True:
            nombre = input('Ingrese el nombre de la persona\n')
            if es_cadena(nombre):
                try:
                    self.nombre = nombre
                    break
                except ValueError as e:
                    print(f'Error : {e}')
            else:
                print('El nombre ingresado es invalido. Solo se permiten letras y espacios internos')
                
        while True:
            apellido = input('Ingrese el apellido de la persona\n')
            if es_cadena(apellido):
                try:
                    self.apellido = apellido
                    break
                except ValueError as e:
                    print(f'Error : {e}')
            else:
                print('El apellido ingresado es invalido. Solo se permiten letras y espacios internos')

        while True:
            edad = input('Ingrese la edad de la persona\n')
            if es_entero(edad) and es_positivo(int(edad)):
                try:
                    self.edad = int(edad)
                    break
                except (ValueError, TypeError) as e:
                    print(f'Error: {e}')
            else:
                print('La edad ingresada es incorrecta. Edad debe  ser un número entero.')

        while True:
            dni = input('Ingrese el DNI de la persona\n')
            if es_entero(dni) and es_positivo(int(dni)):
                try:
                    self.DNI = int(dni)
                    break
                except (ValueError, TypeError) as e:
                    print(f'Error: {e}')
            else:
                print('El DNI ingresado es incorrecta. DNI debe ser un número entero.') 

    def mostrar_datos(self):
        print(f'Datos de {self.nombre}')
        print(f'Nombre y apellido: {self.nombre} {self.apellido}')
        print(f'Edad: {self.edad}')
        print(f'DNI: {self.DNI}')

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f'{self.nombre} tiene {self.edad} y es mayor de edad')
        else:
            print(f'{self.nombre} tiene {self.edad} y es menor de edad')            


def desafio_7():
    persona = Persona()   
    persona.ingresar_datos_persona()
    persona.mostrar_datos()
    persona.es_mayor_de_edad()

while True:
    desafio_7()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break