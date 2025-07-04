from assets.funcionesUtiles import es_cadena, es_entero, es_positivo
class Persona():
    def __init__(self, nombre=None, apellido='', edad='', dni=None, sexo=''):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__DNI = dni
        self.__sexo = sexo
    #METODOS GETTERS Y SETTER CON DECORADORES (ATRIBUTOS PRIVADOS)
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

    @property
    def sexo(self):
        return self.__sexo

    
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

    @sexo.setter
    def sexo(self, sexo):
        if not isinstance(sexo, str):
            raise TypeError('El sexo de la persona debe ser una cadena de texto')
        if len(sexo.strip()) != 1:
            raise ValueError('El sexo de la persona debe tener un unico carater')
        self.__sexo = sexo

    #INGRESO DE DATOS DE LA PERSONA CON VALIDACION
    def ingresar_datos_persona(self, mensaje):
        print(f'{mensaje}')
        while True:
            nombre = input('Ingrse el nombre de la persona\n')
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

        while True:
            sexo = input('Ingrese el sexo de la persona [ V | M ]\n')
            if es_cadena(sexo):
                try:
                    self.sexo = sexo
                    break
                except ValueError as e:
                    print(f'Error : {e}')
            else:
                print('El sexo ingresado es invalido. Solo se permiten letras y espacios internos')

        