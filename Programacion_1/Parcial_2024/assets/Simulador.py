from assets.Universo import Universo
class Simulador():
    def __init__(self, universo, etapa = 0):
        self.universo = universo
        self.etapa = etapa

    def iniciar(self):
        self.universo.titulo()
        self.universo.ingrese_valores()
        print('Universo en Estado Inicial')
        self.universo.mostrar_matriz()

        while not self.universo.equilibrio():
            self.etapa += 1
            print(f'Etapa de simulación: {self.etapa}')
            self.universo.convertir_impares()
            self.universo.mostrar_matriz()

        print('El universo esta equilibrado')


