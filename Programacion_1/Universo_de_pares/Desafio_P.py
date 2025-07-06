from assets.Simulador import Simulador
from assets.Universo import Universo

def parcial():
    universo1 = Universo()
    simu = Simulador(universo1)
    simu.iniciar()

if __name__ == "__main__":
    parcial()
