from assets.cuenta import Cuenta

class CajaAhorro(Cuenta):
    def __init__(self, titular='', cantidad=0.0):
        super().__init__(titular, cantidad, 'caja ahorro')

    def mostrar_tipo_cuenta(self):
        print(f'Cuenta de tipo: {self.tipo_cuenta}')