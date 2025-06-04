import continuar

def generar_lista():
    n = int(input('Ingrese cantidad de números a caragr en la lista\n'))
    lista_n = []
    for i in range(n):
        numero = int(input('Ingrese un número a almacenar\n'))
        lista_n.append(numero)
    return lista_n

def mostrar_lista_ordenada(lista_numeros):
    lista_numeros.sort()
    auzx = ' | '.join(str(numero) for numero in lista_numeros)
    print(f'{auzx}')

def mostrar_lista_indice(lista_numeros):
    for indice, numero in enumerate(lista_numeros):
        print(f'El numero {numero} esta en la posicion: {indice}')

def calculos(lista):
    suma_n = 0
    cont_par = 0
    cont_im = 0
    for i in lista:
        if i % 2 == 0:
            cont_par += 1
        else:
            cont_im += 1
        suma_n = suma_n + i

    if len(lista) > 0:
        promedio = suma_n / len(lista)
        return promedio, cont_im, cont_par
    else:
        print('No ingresaste valores')
    
def mayor_valor(lista_numeros):
    mayor = -9999
    for numero in lista_numeros:
        if numero > mayor:
            mayor = numero
    return mayor

def main():
    lista_numeros = generar_lista()
    mostrar_lista_ordenada(lista_numeros)
    promedio, cont_im, cont_par = calculos(lista_numeros)
    print(f'El promedio de los números es: ---> {promedio}')
    print(f'La cantida de pares es: ---> {cont_par}')
    print(f'La cantida de impares es: ---> {cont_im}')
    mas_grande = mayor_valor(lista_numeros)
    print(f'El número mas grande la lista es: ----> {mas_grande}')
    mostrar_lista_indice(lista_numeros)

while True:
    main()
    if not continuar.continuarGen():
        print('===FIN DEL PROGRAMA==')
        break