""" Desafío 6
    Desarrollar un programa que conste de una clase Cuenta y dos subclases PlazoFijo
    y CajaAhorro. Definir los atributos titular, cantidad, tipo de cuenta y métodos para
    consultar los datos en la clase Cuenta. La clase CajaAhorro hereda los datos y consulta 
    el tipo de cuenta. La clase PlazoFijo tendrá atributos propios, plazo e interés. 
    Tendrá métodos para obtener el importe del interés (cantidad * interés / 100), 
    datos del titular, plazo, interés, tipo de cuenta y total de interés.
    Instanciar al menos dos objeto de cada subclase. 
"""
from assets.cuenta import Cuenta
from assets.CajaAhorro import CajaAhorro
from assets.PlazoFijo import PlazoFijo
    
def desafio_6():
    print('=== CUENTAS DE CAJA DE AHORRO ===')
    caja1 = CajaAhorro('Jorge Pardo', 15000)
    caja2 = CajaAhorro('Ana Garcia', 8000)
    print(caja1.mostrar_datos())
    caja1.mostrar_tipo_cuenta()
    print(caja2.mostrar_datos())
    caja2.mostrar_tipo_cuenta()

    print('\n=== CUENTAS DE PLAZO FIJO ===')
    plazoF1 = PlazoFijo('Carlos Cervantes', 10000, 90, 12.5)
    plazoF2 = PlazoFijo('Lucía Calderón', 20000, 180, 10.0)
    print(plazoF1.mostrar_datos_completos())
    print(plazoF2.mostrar_datos_completos())

desafio_6()

 