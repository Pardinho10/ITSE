#@title Ejemplo de encapsulamiento
#Clase Persona
class Persona():
    def __init__(self, nombre, edad):
        self._nombre =  nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @nombre.deleter
    def nombre(self):
        del self._nombre
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if 0 > nueva_edad:
            raise ValueError('Edad no válida. Debe ser un número positivo')
        self.__edad = nueva_edad

    @edad.deleter
    def edad(self):
        del self.__edad

#Instancia de Persona
persona = Persona('Luciano', 21)

#Acceso y actualiación de atributos de la instancia
print(f'Persona: {persona.nombre:<10s} | Edad: {persona.edad}')
persona.nombre = 'Maria'
try:
    persona.edad = -13
except:
    print("Ingresaste un número Negativo")
print(f'Persona: {persona.nombre:<10s} | Edad: {persona.edad}')

#@title ejemplo de abstracción
#Clase Empleado
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
    
    def calcular_salario_neto(self):
        #Se calcula el salario de un empleado
        pass

    def imprimir_informacion(self):
        #Se impirme la información del empleado
        pass

    @classmethod
    def desde_cadena(cls, cadena):
        nombre, edad, salario = cadena.split(',')
        return cls(nombre, int(edad), float(salario))
    @staticmethod
    def validar_salario(salario):
        return salario >= 0


#Instancias de la clase Empleado
empleado1 = Empleado('Ariel', 23000)
empleado2 = Empleado('Cecilia', 32400)

#Accedemos a metodos y atributos de los objetos de tipo Empleado
print(f'Empleado: {empleado1.nombre:<10s} | Salario: {empleado1.salario}')
print(f'Empleado: {empleado2.nombre:<10s} | Salario: {empleado2.salario}') 