import continuar

def genera_lista():
    ciclo = int(input('Ingrese la cantidad de personas\n'))
    lista_personas = []
    for i in range(ciclo):
        nombre = input('Ingrese nombre de la persona\n')
        edad = int(input('Ingrse la edad de la persona\n'))
        lista_personas.append((nombre, edad))
    return lista_personas

def mostrar_personas(lista):
    for (nombre, edad) in lista:
        print(f'Nombre: {nombre} y su edad: {edad}')

def separa_listas(lista):
    list_nom = []
    list_edad = []
    suma_ed = 0
    for (nombre, edad) in lista:
        list_nom.append(nombre)
        list_edad.append(edad)
        suma_ed = suma_ed + edad
    prom = suma_ed / len(lista)
    a = ' - '.join(list_nom)
    print(a)
    b = '-'.join(str(edad) for edad in list_edad)
    print(b)
    print(f'El promedio de edades es ----> {prom}')


def main():
    lista_personas = genera_lista()
    #print(lista_personas)    
    mostrar_personas(lista_personas)
    separa_listas(lista_personas)
    

while True:
    main()

    if not continuar.continuarGen():
        print('FIN DEL PROGRAMA')
        break