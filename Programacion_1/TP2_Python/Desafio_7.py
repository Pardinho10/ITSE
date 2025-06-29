"""  Desafío 7
    Desarrollar una clase Persona. Sus atributos son: nombre, edad y DNI. Incluir los siguientes métodos para la clase:
    * Un constructor, donde los datos pueden estar vacíos.
    * Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
    * Mostrar(): Muestra los datos de la persona.
    * es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad. 
"""
import continuar

class Persona():
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = dni

    @property 
    def nombre(self):
        return self.__nombre        
        
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
        if documento < 0 or documento > 9999999:
            raise ValueError('El DNI debe ser un entero entre 0 y 99999999')
        self.__DNI = documento


    def ingresar_datos_persona(self):
        while True:
            try:
                self.nombre = input('Ingrese el nombre de la persona\n')
                break
            except (TypeError, ValueError) as e:
                print(f"Error: {e}")
        pass

def desafio_7():
    persona = Persona()   
    persona.ingresar_datos_persona()

while True:
    desafio_7()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break