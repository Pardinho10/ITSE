""" Desafío 5
    En un Banco tienen clientes que pueden hacer depósitos y extracciones de dinero. 
    El Banco requiere también al final del día calcular la cantidad de dinero que se ha
    depositado. Se deberán instanciar dos clases, la clase Cliente y la clase Banco.
    La clase Cliente tendrá los atributos nombre, cantidad y los métodos __init__,
    depositar, extraer, get_total. La clase Banco tendrá como atributos 3 objetos 
    de la clase Cliente y los métodos __init__, operar y deposito_total.
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
        monto = float(input('Ingrese el monto a depositar\n'))
        if isinstance(monto, float):
            if monto >= 0 and monto <= 999999:
                self.cantidad = self.cantidad + monto
            else:
                print('El monto no es correcto, no debe ser negativo ni mayor a 999999')
        else:
            print('Error: El monto debe ser un valor númerico')

    def extraer(self):
        print(f'Monto inicial: {self.cantidad}')
        monto = float(input('Ingrese el monto a extraer\n'))
        if isinstance(monto, float):
            if monto >= 0 and monto <= 999999:
                self.cantidad = self.cantidad - monto
            else:
                print('El monto no es correcto, no debe ser negativo ni mayor a 999999')
        else:
            print('Error: El monto debe ser un valor númerico')

    def get_total(self):
        print(f'Monto actual en Caja de Ahorro: ${self.cantidad}')

    @staticmethod
    def menu_cliente():
        print('==================================')
        print('**** ACTUALZIACION DE CLIENTE ****')
        print('==================================')
        print('1 - DEPOSITAR')
        print('2 - EXTRAER')
        print('3 - MOSTRAR SALDO EN CAJA DE AHORRO')
        print('S o 0 - SALIR')

    def operar_cliente(self):
        while True:
            Cliente.menu_cliente()
            print(f'Nombre del Cliente: {self.nombre}')
            opc = input('Seleccione una operación\n').strip()
            match opc:             
                case '1':
                    self.depositar()
                case '2':
                    self.extraer()
                case '3':
                    self.get_total()
                case 's' | '0':
                    print('Saliendo del programa...')
                    return
                case _:
                    print('Error, opcion no valida')
    
    def datos_iniciales(self):
        self.nombre = input('Ingresa tu nombre\n').strip().capitalize()
        self.cantidad = float(input('Ingrese monto actual depositado en Caja de Ahorro\n'))

    def __str__(self):
        print('======DATOS INICIALES DEL CLIENTE======')
        return f'Nombre del Cliente: {self.nombre} | Monto inicial: ${self.cantidad}'
        
class Banco():
    def __init__(self, clientes = None):
        self.clientes = clientes if clientes is not None else []

    def cargar_clientes(self):
        for i in range(3):
            cliente = Cliente()
            cliente.datos_iniciales()
            self.clientes.append(cliente)
            print(cliente)
            

    def operaciones_cliente(self):
        self.mostrar_info_clientes()
        opc = int(input('Seleccione un cliente para realizar operaciones\n').strip())
        for i, cli in enumerate(self.clientes, 1):
            if opc == i:
                cli.operar_cliente()

    def mostrar_info_clientes(self):
        if not self.clientes:
            print("No hay clientes cargados.")
            return

        print('===========================')
        print('N°   NOMBRE CLIENTE  SALDO CANJA DE AHORRO')
        print('===========================')
        for i, cli in enumerate(self.clientes, 1):
           print(f'{i:<5}{cli.nombre:<18}${cli.cantidad:.2f}')

    def deposito_total(self):
        sum_depositos = 0
        for i in self.clientes:
            sum_depositos = i.cantidad + sum_depositos
        return sum_depositos
    
    def get_total_clientes(self, suma):
        print(f'Monto actual total en Cajas de Ahorro: ${suma}')

    @staticmethod
    def menu_banco():
        print('===========================')
        print('******* BANCO ITSE ********')
        print('===========================')
        print('1 - CARGAR DATOS DE CLENTES')
        print('2 - OPERACIONES CLENTES')
        print('3 - MOSTRAR INFORMACION DE CLIENTES')
        print('4 - MOSTRAR DEPOSITO TOTAL')
        print('S o 0 - SALIR')

    def operar_banco(self):
        while True:
            Banco.menu_banco()
            opc = input('Seleccione una operación\n').strip()
            match opc:
                case '1':
                    self.cargar_clientes()   
                case '2':
                    self.operaciones_cliente()
                case '3':
                    self.mostrar_info_clientes()
                case '4':
                    sum_depositos = self.deposito_total()
                    self.get_total_clientes(sum_depositos)
                case 's' | '0':
                    print('Saliendo del programa...')
                    return
                case _:
                    print('Error, opcion no valida')


def desafio_5():
    banco = Banco()
    banco.operar_banco()

while True:
    desafio_5()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break