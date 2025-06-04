"""Desafío 29
    Dada un alfanumérico texto y un caracter x, retornar una lista de enteros representando
    la distancia mas corta desde cada caracter en texto hasta la primer ocurrencia del caracter x.
"""
import continuar

def suma_distancia (posicion_carac2, lista_y):
    menor_dist = 99999
    for k in lista_y:
        distancia = abs(posicion_carac2 - k)
        print(f'La distancia entre {posicion_carac2} y {k} es ---> {distancia}')
        if distancia < menor_dist:
            menor_dist = distancia
    print(f"la menor distancia es: {menor_dist}")
    
def main():
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    texto = input('Ingrese un texto\n').lower()
    caract = input('Ingrse un caracter simple').lower()
    lista_y = []
    posicion_caract2 = 0
    print(caract)
    posicion_caract = texto.find(caract)
    print(posicion_caract)
    for i in texto:
        if caract == i:
            posicion_caract2 = alfabeto.find(caract)       
            print(f'La letra {i} esta en la posicion {posicion_caract2} en el alfabeto')
        else:     
            lista_y.append(alfabeto.find(i))         
            #print(f'La letra {i} esta en la posicion {y} en el alfabeto')
    print(lista_y)
    suma_distancia(posicion_caract2, lista_y)

while True:
    main()
    if not continuar.continuarGen():
        print('=============FIN DEL PROGRAMA==============')
        break