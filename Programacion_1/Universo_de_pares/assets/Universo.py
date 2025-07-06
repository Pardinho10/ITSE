import random
class Universo():
    def __init__(self, filas = 0, columnas = 0):
        self.__filas = filas
        self.__columnas = columnas
        self.matriz = []

    @property
    def filas(self):
        return self.__filas
    
    @property
    def columnas(self):
        return self.__columnas 
    
    @filas.setter
    def filas(self, nueva_fila):
        self.__filas = nueva_fila

    @columnas.setter
    def columnas(self, nueva_columns):
        self.__columnas = nueva_columns

    def titulo(self):
        print('================================')    
        print('Un Universo de números pares')
        print('================================')    

    def generar_matriz(self):
        self.matriz = [[random.randint(1, 100) for _ in range(self.columnas)] for _ in range(self.filas)]

    def mostrar_matriz(self):
        for fila in self.matriz:
            print(fila)

    def equilibrio(self):
        for fila in self.matriz:
            for num in fila:
                if num %2 != 0:
                    return False
        return True

    def convertir_impares(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j] % 2 != 0:
                    self.matriz[i][j] = random.randint(0, 99)

    def ingrese_valores(self):
        self.columnas = int(input('Ingrese el numero de columnas\n'))
        self.filas = int(input('Ingrese el numero de filas\n'))
        self.generar_matriz()
        
