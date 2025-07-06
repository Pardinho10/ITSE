from assets.cuenta import Cuenta
class PlazoFijo(Cuenta):
    def __init__(self, titular='', cantidad=0.0, plazo=0, interes=0.0):
        super().__init__(titular, cantidad, 'plazo fijo')
        self.__plazo = plazo
        self.__interes = interes

    @property
    def plazo(self):
        return self.__plazo

    @plazo.setter
    def plazo(self, plazo):
        if not isinstance(plazo, int) or plazo <= 0:
            raise ValueError('El plazo debe ser un número entero positivo.')
        self.__plazo = plazo

    @property
    def interes(self):
        return self.__interes

    @interes.setter
    def interes(self, interes):
        if not isinstance(interes, (int, float)) or interes <= 0:
            raise ValueError('El interés debe ser un número positivo.')
        self.__interes = interes

    def calcular_interes(self):
        return self.cantidad * self.interes / 100

    def mostrar_datos_completos(self):
        total = self.cantidad + self.calcular_interes()
        return (
            f'Titular: {self.titular} | Cantidad: ${self.cantidad:.2f} | '
            f'Plazo: {self.plazo} días | Interés: {self.interes}% | '
            f'Total con Interés: ${total:.2f}'
        )