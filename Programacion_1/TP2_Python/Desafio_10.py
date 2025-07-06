import unittest

# ===============================
#       CLASES DE VEHÍCULOS
# ===============================

class Vehiculo:
    def __init__(self, nombre):
        self.nombre = nombre

    def mover(self):
        return f"El vehículo {self.nombre} se está moviendo."


class VehiculoTerrestre(Vehiculo):
    def __init__(self, nombre, ruedas):
        super().__init__(nombre)
        self.ruedas = ruedas

    def mover(self):
        return f"El vehículo terrestre {self.nombre} se mueve con {self.ruedas} ruedas."


class Auto(VehiculoTerrestre):
    def __init__(self, nombre, color):
        super().__init__(nombre, 4)
        self.color = color

    def mover(self):
        return f"El auto {self.color} {self.nombre} se desplaza por la carretera."


class AutoRojo(Auto):
    def __init__(self):
        super().__init__("Auto Rojo", "rojo")


class AutoAmarillo(Auto):
    def __init__(self):
        super().__init__("Auto Amarillo", "amarillo")


class Bicicleta(VehiculoTerrestre):
    def __init__(self):
        super().__init__("Bicicleta", 2)

    def mover(self):
        return "La bicicleta se mueve pedaleando."


class Barco(Vehiculo):
    def __init__(self):
        super().__init__("Barco")

    def mover(self):
        return "El barco navega por el agua."


# ===============================
#         TEST UNITARIO
# ===============================

class TestVehiculos(unittest.TestCase):

    def test_auto_rojo(self):
        auto = AutoRojo()
        self.assertEqual(auto.mover(), "El auto rojo Auto Rojo se desplaza por la carretera.")

    def test_auto_amarillo(self):
        auto = AutoAmarillo()
        self.assertEqual(auto.mover(), "El auto amarillo Auto Amarillo se desplaza por la carretera.")

    def test_bicicleta(self):
        bici = Bicicleta()
        self.assertEqual(bici.mover(), "La bicicleta se mueve pedaleando.")

    def test_barco(self):
        barco = Barco()
        self.assertEqual(barco.mover(), "El barco navega por el agua.")

    def test_vehiculo_base(self):
        veh = Vehiculo("Genérico")
        self.assertEqual(veh.mover(), "El vehículo Genérico se está moviendo.")

    def test_vehiculo_terrestre(self):
        moto = VehiculoTerrestre("Moto", 2)
        self.assertEqual(moto.mover(), "El vehículo terrestre Moto se mueve con 2 ruedas.")


# ===============================
#          EJECUCIÓN
# ===============================

if __name__ == '__main__':
    unittest.main()
