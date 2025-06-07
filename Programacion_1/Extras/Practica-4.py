import continuar
import random

def generar_lista():
    ciclo = int(input('Ingrese la cantidad de jugadores\n'))
    lista_jug = []
    for i in range(ciclo):
        jugador = input('Ingrese el nombre del jugador\n')
        puntuacion = random.randint(0, 100)
        lista_jug.append((jugador, puntuacion))
    return lista_jug

def mostrar_lista(lista_j):
    print(f'Lista de jugadores ----> {lista_j}')
    print('JUGADOR | PUNTUACION')
    for jugador, puntuacion in lista_j:
        print(f'{jugador} | {puntuacion}')

def puntajes(lista_j):
    pepito = sorted(lista_j, key=lambda x: x[1])
    print(pepito)
    print(pepito[-3:])
    print(pepito[1:4])
    medio = len(lista_j)
    if medio % 2 == 0:
        media1 = lista_j[medio//2 -1]
        media2 = lista_j[medio//2]
        nombre1, puntos1 = media1 
        nombre2, puntos2 = media2
        mediana = (puntos1 + puntos2) / 2
        print(f'El puntaje del medio surge del promedio de los elementos centrales {mediana}')
    else:
        media2 = lista_j[medio//2]
        print(f'El puntaje del medio es: {media2}')
    

def main():
    lista_jugaderes = generar_lista()
    mostrar_lista(lista_jugaderes)
    puntajes(lista_jugaderes)

while True:
    main()
    if not continuar.continuarGen():
        print('===FIN DEL PROGRAMA==')
        break