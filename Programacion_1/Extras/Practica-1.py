import random
#FUNCION QUE CARGA VALORES EN LISTAS
def cargar_todo():
    cantidad = int(input('Cuantos nombres quieres ingresar?\n'))
    lista_nombres = []
    lista_notas = []
    
    for i in range(cantidad):
        nombre = input('Ingrese el nombre de una persona\n').capitalize().strip()
        #nota = float(input('Ingrese la nota de la persona\n'))
        lista_nombres.append(nombre)
        nota = round(random.uniform(1, 10), 2)
        lista_notas.append(nota)
    promedio = calcular_promedio(lista_notas, cantidad) 
    return lista_nombres, lista_notas, promedio

#FUNCION QUE CALCULA EL PROMEDIO
def calcular_promedio(lista_notas, cantidad):
    suma = 0
    for i in lista_notas:
        suma += i # suma = suma + nota
    if cantidad > 0:
        promedio = suma / cantidad
        return promedio
    else:
        print('No se ingresaron nombres')

#llamo a la funcion
nombres, notas, prom = cargar_todo()
#print(nombres)
print(f'La lista de nombres es ----> {nombres}')
print(f'La lista de notas es ----> {notas}')
print(f'El promedio es ----> {prom}')
# nombres.insert(1,'Pepa')
# print(nombres)
# nombres.pop(2)
# print(nombres)
# x = nombres.count('Pepa')
# print(x)
