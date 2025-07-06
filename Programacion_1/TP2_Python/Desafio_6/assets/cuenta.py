class Cuenta():
    def __init__(self, titular = '', cantidad = 0, tipo_cuenta = 0):
        self.__titular = titular
        self.__cantidad = cantidad
        self.__tipo_cuenta = tipo_cuenta

    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @property
    def tipo_cuenta(self):
        return self.__tipo_cuenta
    
    @titular.setter
    def titular(self, titular):
        if not isinstance(titular, str) or len(titular.strip()) < 3:
            raise ValueError('El titular debe ser una cadena válida con al menos 3 caracteres.')
        self.__titular = titular

    @cantidad.setter
    def cantidad(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad < 0:
            raise ValueError('La cantidad debe ser un número positivo.')
        self.__cantidad = cantidad

    @tipo_cuenta.setter
    def tipo_cuenta(self, tipo):
        if tipo.lower() not in ['caja ahorro', 'plazo fijo']:
            raise ValueError("Tipo de cuenta debe ser 'caja ahorro' o 'plazo fijo'")
        self.__tipo_cuenta = tipo.lower()


    def mostrar_datos(self):
        return f'Titular: {self.titular} | Saldo en Cuenta: ${self.cantidad:.2f} | Tipo de Cuenta: {self.tipo_cuenta}'
