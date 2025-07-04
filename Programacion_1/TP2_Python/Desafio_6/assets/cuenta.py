import continuar
from funcionesUtiles import es_flotante, es_entero, es_cadena

class Cuenta():
    def __init__(self, titular = '', cantidad = 0, tipo_cuenta = 0):
        self._titular = titular
        self._cantidad = cantidad
        self._tipo_cuenta = tipo_cuenta

    @property
    def titular(self):
        return self._titular
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @property
    def tipo_cuenta(self):
        return self._tipo_cuenta
    
    @titular.setter
    def titular(self, nuevo_titular):
        self._titular = nuevo_titular

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    @tipo_cuenta.setter
    def tipo_cuenta(self, nuevo_tipo):
        self._tipo_cuenta = nuevo_tipo


    def __str__(self):
        return f'{self.cantidad}'