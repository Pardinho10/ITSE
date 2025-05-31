"""Desafío 27
    Solicitar al usuario que ingrese los nombres de los estudiantes de primer año,
    finalizando al ingresar “S”. Luego, solicitar al usuario que ingrese los nombres de los
    estudiantes de segundo año, finalizando al ingresar “S”.
    A continuación informar:
    * la lista de todos los nombres de los estudiantes de primer año y de segundo año,
    sin repeticiones.
    * La lista de todos los nombres de los estudiantes de primer año y de segundo
    año que se repiten.
    * la lista de todos los nombres de los estudiantes de primer año que no se repiten
    en segundo año.
"""

primer_año = []
segundo_año = []
repetidos = []
no_repetidos = []
nombre = ""
while nombre != 'S':
    nombre = input('Ingrese el nombre de los estudiantes de primer año o (S) para terminar\n')
    if nombre != 'S':
        primer_año.append(nombre)
nombre = ""
while nombre != 'S':
    nombre = input('Ingrese el nombre de los estudiantes de segundo año o (S) para terminar\n')
    if nombre != 'S':
        segundo_año.append(nombre)
print(f'Los alumnos de primer año son: --> {primer_año}')
print(f'Los alumnos de segundo año son: --> {segundo_año}')

#Recorremos ambas listas para enocntrar los repetidos

for i in primer_año:
    for j in segundo_año:
        if i == j:
            repetidos.append(i)
for j in primer_año:
    if j not in repetidos:
        no_repetidos.append(j)
print(f'Los alumnos que se repinten en ambos años son ----> {repetidos}')
print(f'Los alumnos de primer año que no se repiten en segundo son ----> {no_repetidos}')