import funcionesUtiles

#FUNCION QUE NOS MUESTRA EL TITULO DEL DESAFIO
def titulo():
    print('=======================================================================')
    print('Desafio 1:')
    print('Informar los números múltiplos de 3 o 5 de un conjunto de números.')
    print('=======================================================================')

#FUNCION QUE GENERA "N" PRIMEROS NUMEROS DE LA SERIE DE FIBONACCI
def generar_fibo():
    a = 0
    b = 1
    siguiente = 0
    cont = 1
    serie_fibo_str = []
    serie_fibo = []
    n = input('Ingrese la cantidad de valores de la serie Fibo\n').strip()
    if funcionesUtiles.es_entero(n):
        cantidad = int(n)
        if funcionesUtiles.es_positivo(cantidad) and cantidad <= 25:
            while cont <= cantidad:
                serie_fibo.append(a)
                serie_fibo_str.append(str(a))
                siguiente = a + b
                a = b
                b = siguiente
                cont += 1
            return '  '. join(serie_fibo_str), serie_fibo            
        else:
            return [], []           
    else:
        return None, None    

#FUNCION QUE MUESTRA LA SERIE DE FIBONACCI
def mostrar_serie_fibo(lista_fibo_str, lista_fibo):
    match lista_fibo_str:
        case []:
            print('El número ingresado debe ser positivo (mayor a 0 y menor a 25) \n')
        case None:
            print('Caracter invalido, debe ingresar un nuemro natural positivo')
        case _:
            print(f"Primeros {len(lista_fibo)} números de la Serie de Fibonacci: --->  {lista_fibo_str}")

#FUNCION BUSCA MULTIPLOS Y GENERA NUEVA LISTA CON ELLOS
def multiplos_fibo(lista_fibo):
    lista_multiplos = []
    for numero in lista_fibo:
        if numero % 3 == 0 or numero % 5 == 0:
            lista_multiplos.append(str(numero))
    return '  '.join(lista_multiplos)

#FUNCION QUE MUESTRA LA LISTA GENERADA CON LOS MULTIPLOS DE 3 || 5
def mostrar_mutiplos_fibo(lista_fibo_multiplos):
    print(f'Listado de numero de la serie multiplos de 3 o 5 ---> {lista_fibo_multiplos}')