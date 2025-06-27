from abc import ABC, abstractmethod

# ----- ABSTRACCIÓN -----
class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca  # Encapsulamiento: atributo protegido
        self._modelo = modelo

    @property
    def marca(self):  # Property para acceso controlado
        return self._marca

    @abstractmethod
    def describir(self):  # Método abstracto
        pass

    # ----- MÉTODO MÁGICO -----
    def __str__(self):
        return f"{self._marca} {self._modelo}"

# ----- HERENCIA Y POLIMORFISMO -----
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.__num_puertas = num_puertas  # Atributo privado

    # ----- POLIMORFISMO -----
    def describir(self):
        return f"Coche: {self.marca} {self._modelo}, {self.__num_puertas} puertas"

    # ----- MÉTODO MÁGICO -----
    def __add__(self, otro):
        return f"Sumando {self.marca} y {otro.marca}"

# ----- EXCEPCIONES -----
class Taller:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        if not isinstance(vehiculo, Vehiculo):
            raise TypeError("¡Solo se aceptan vehículos!")  # Lanzar excepción
        self.vehiculos.append(vehiculo)

# ----- PROPIEDADES Y ENCAPSULAMIENTO -----
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self._cilindrada = cilindrada

    @property
    def cilindrada(self):
        return f"{self._cilindrada}cc"

    def describir(self):
        return f"Motocicleta: {self.marca} {self._modelo}, {self.cilindrada}"

# ----- PROGRAMA PRINCIPAL -----
if __name__ == '__main__':
    try:
        # Crear instancias
        mi_coche = Coche("Toyota", "Corolla", 4)
        mi_moto = Motocicleta("Honda", "CBR", 600)

        # Taller y excepciones
        taller = Taller()
        taller.agregar_vehiculo(mi_coche)
        taller.agregar_vehiculo(mi_moto)
        # taller.agregar_vehiculo("No es un vehículo")  # ¡Lanza TypeError!

        # Polimorfismo en acción
        for vehiculo in taller.vehiculos:
            print(vehiculo.describir())

        # Métodos mágicos
        print(mi_coche)  # Usa __str__
        print(mi_coche + mi_moto)  # Usa __add__

    except Exception as e:
        print(f"Error: {e}")