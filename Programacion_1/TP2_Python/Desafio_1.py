""" Desafío 1
    Desarrollar un programa que defina el Tipo de Dato Abstracto (TDA) Estudiante 
    que tenga como atributos el nombre y nota de evaluación. Incluir los métodos para 
    inicialización y consulta de sus atributos y consulta si ha aprobado o no ha aprobado la evaluación.
"""
import continuar
import funcionesUtiles
class Estudiante():
    def __init__(self):
        self._nombre = None
        self._nota = None

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre ):
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, nota ):
        self._nota = nota

    def ingresar_datos_estudiante(self):
        nombre_est = input('Ingrese el nombre del estudiante\n').capitalize()
        self.nombre = nombre_est
        while True:
            nota_est = input('Ingrese la nota del estudiante\n')
            if funcionesUtiles.es_flotante(nota_est) or funcionesUtiles.es_entero(nota_est):
                if funcionesUtiles.es_positivo(float(nota_est)):
                    if 0 <= float(nota_est) <= 10:
                        self.nota = float(nota_est)
                        break
                    else:
                        print('Nota fuera de rango')
                else:
                    print('La nota debe ser un número positivo')
            else:
                print('La nota debe ser un valor numérico')

    def alumno_aprobado(self):
        if self.nota is not None and self.nota >= 6:
            print(f'El alumno {self.nombre} ha aprobado con {self.nota} puntos')
        elif self.nota is not None:
            print(f'El alumno {self.nombre} ha desaprobado con {self.nota} puntos')

def mostrar_lista_alumno(lista_alumnos):
    print('=======================================================================')
    print('=========================LISTADO DE ALUMNOS============================')
    print('I |    ALUMNO      | NOTA')
    print('=======================================================================')
    for i, lista in enumerate(lista_alumnos, 1):
        print(f'{i} | {lista.nombre:^20s} | {lista.nota}')


def desafio_1():
    lista_alumnos = []
    N = int(input('Ingrese la cantidad de alumnos que se guardaran en la lista\n'))
    for i in range(N) :
        alumno = Estudiante()
        alumno.ingresar_datos_estudiante()
        alumno.alumno_aprobado()
        lista_alumnos.append(alumno)
    return lista_alumnos

while True:
    lista_alumnos = desafio_1()
    if not continuar.continuarGen():
        mostrar_lista_alumno(lista_alumnos)
        print('===========FIN DEL PROGRAMA===========')
        break
    



