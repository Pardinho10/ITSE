class Restaurante():

    def __init__(self, nombre, categoria, precio, año_fundacion):
        # Default PUBLIC
        self.nombre = nombre
        self.categoria = categoria
        # PROTECTED
        self._precio = precio
        # PRIVATE
        self.__año_fundacion = año_fundacion

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre} | Categoria: {self.categoria} | Precio: ${self._precio} | Año de Fundacion: {self.__año_fundacion}')



restaurante1 = Restaurante('Pizzeria Pepito', 'Comida Rapida',50.00, 1998)
restaurante1.mostrar_informacion()
restaurante1._precio = 90 #Se modifica por que es Protected y se puede modificar desde la misma clase
restaurante1.__año_fundacion = 2000 #Private, solo se modifica desde un metodo
restaurante1.categoria = 'Comida Familiar' #Public, se puede modificar desde cualquier lugar de la aplicacion
restaurante1.mostrar_informacion()
restaurante2 = Restaurante('Hamburgesas Pepito', 'Comida Rapida',25.00, 1997)
restaurante2.mostrar_informacion()










""" class Restaurante():
    def agregar_restaurante(self, nombre):
        self.nombre = nombre #Atributo

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

#Instanciar Clase
restaurante = Restaurante()
restaurante.agregar_restaurante('Pizzeria Pepito')
restaurante.mostrar_informacion()

restaurante2 = Restaurante()
restaurante2.agregar_restaurante('Hamburgesas Pepito')
restaurante2.mostrar_informacion()

print(f'{restaurante2.mostrar_informacion}')
print(f'{restaurante2.mostrar_informacion()}')
 """
    