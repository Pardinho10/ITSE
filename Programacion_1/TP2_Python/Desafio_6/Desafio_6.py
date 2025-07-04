""" Desafío 6
    Desarrollar un programa que conste de una clase Cuenta y dos subclases PlazoFijo
    y CajaAhorro. Definir los atributos titular, cantidad, tipo de cuenta y métodos para
    consultar los datos en la clase Cuenta. La clase CajaAhorro hereda los datos y consulta 
    el tipo de cuenta. La clase PlazoFijo tendrá atributos propios, plazo e interés. 
    Tendrá métodos para obtener el importe del interés (cantidad * interés / 100), datos del titular, 
    plazo, interés, tipo de cuenta y total de interés. Instanciar al menos dos objeto de cada subclase. 
"""
import continuar
from assets.cuenta import Cuenta
    
def desafio_6():
    cuenta = Cuenta()
    print(cuenta)
    
while True:
    desafio_6()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break

