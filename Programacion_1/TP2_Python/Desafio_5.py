""" Desafío 5
    En un Banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El Banco requiere también al final del día calcular la cantidad de dinero que se ha depositado. Se deberán instanciar dos clases, la clase Cliente y la clase Banco. La clase Cliente tendrá los atributos nombre, cantidad y los métodos __init__, depositar, extraer, get_total. La clase Banco tendrá como atributos 3 objetos de la clase Cliente y los métodos __init__, operar y deposito_total.
 """
import continuar

class Cliente():
    def __init__(self,nombre = None, cantidad = None):
        self.__nombre = nombre
        self.__cantidad = cantidad

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @cantidad.setter
    def cantidad(self, cantidad):
        if isinstance(cantidad, float):
            if cantidad >= 0 and cantidad <= 999999:
                self.__cantidad = cantidad
            else:
                print('El monto no es correcto, no debe ser negativo ni mayor a 999999')
        else:
            print('Error: El monto debe ser un valor númerico')


    def depositar(self):
        print(f'Monto inicial: {self.cantidad}')
        monto = float(input('Ingrese el monto a depositar'))
        if isinstance(monto, float):
            if monto >= 0 and monto <= 999999:
                self.cantidad = self.cantidad + monto
            else:
                print('El monto no es correcto, no debe ser negativo ni mayor a 999999')
        else:
            print('Error: El monto debe ser un valor númerico')

    def extraer(self):
        print(f'Monto inicial: {self.cantidad}')
        monto = float(input('Ingrese el monto a extraer'))
        if isinstance(monto, float):
            if monto >= 0 and monto <= 999999:
                self.cantidad = self.cantidad - monto
            else:
                print('El monto no es correcto, no debe ser negativo ni mayor a 999999')
        else:
            print('Error: El monto debe ser un valor númerico')

    def get_total(self):
        print(f'El saldo actual en tu cuenta es {self.cantidad}')

    @staticmethod
    def menu():
        print('===========================')
        print('********BANCO IRANÍ********')
        print('===========================')
        print('1 - CARGAR DATOS')
        print('2 - DEPOSITAR')
        print('3 - EXTRAER')
        print('4 - MOSTRAR CANTIDAD')
        print('S o 0 - SALIR')

    def operar(self):
        while True:
            Cliente.menu()
            opc = input('Seleccione una operación\n').strip()
            match opc:
                case '1':
                    self.datos_iniciales()
                    print(self)                
                case '2':
                    self.depositar()
                case '3':
                    self.extraer()
                case '4':
                    self.get_total()
                case 's' | '0':
                    print('Saliendo del programa...')
                    return
                case _:
                    print('Error, opcion no valida')
    
    def datos_iniciales(self):
        self.nombre = input('Ingresa tu nombre\n').strip().capitalize()
        self.cantidad = float(input('Ingresa cantidad existente en la cuenta\n'))

    def __str__(self):
        print('======DATOS INICIALES DEL CLIENTE======')
        return f'Nombre del Cliente: {self.nombre} | Monto inicial: {self.cantidad}'
        
# class Banco():




def desafio_5():
    sergio = Cliente()
    sergio.operar()

while True:
    desafio_5()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break