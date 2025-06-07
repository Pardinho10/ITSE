# mi_biblioteca.py

# -----------------------
# FUNCIONES MATEMÁTICAS
# -----------------------

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# Desarrollar un programa que muestre la sumatoria de todos los números entre el 0 y el 30.
suma = 0
for i in range(31):
    suma += i
  
print(f"el resultado de la sumatoria es: {suma}")

# Suma sin sumar
def suma_sin_suma(a, b):
    while b != 0:

        carry = a & b
        a = a ^ b
        b = carry << 1

    return a

# Suma de dígitos de un mismo numero.

def suma_dig(num):
    suma = 0
    while num != 0:
        dig = num % 10
        suma += dig
        num //= 10
    return suma

# Función potencia sin utilizar los operadores de multiplicación o división.

num1 = int(input('Ingrese la base de la potencia\n'))
num2 = int(input('Ingrese el exponente de la potencia\n'))

def potencia():
    cont = 1
    aux = num1
    while cont < num2:    
        aux = multiSuma(num1, aux) 
        
        cont += 1
    print(f'{num1} elevado a la {num2} es --->  {aux}')
#Multiplicacion con sumas
def multiSuma (num1, aux):    
    cont = 1
    suma  = 0
    print(f' el nume1 -> {num1}, y el aux -> {aux}')
    while cont < aux:    
        suma = suma + num1
        cont += 1
       
    return suma + num1
#multiSuma(num1, num2)
potencia()

# Suma 1 a cada numero de una lista
def sumar_uno(lista):
    resultado = []
    for numero in lista:
        resultado.append(numero + 1)
    return resultado

numeros = [1, 2, 3, 4, 5]
resultado = sumar_uno(numeros)
print("Lista original:", numeros)
print("Lista con los números sumados más uno:", resultado)

# calcular la mediana o media
def mediana(lista):
    if not lista:
        raise ValueError("La lista está vacía")

    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)

    # Calcular la mediana
    if n % 2 == 1:
        # impar
        return lista_ordenada[n // 2]
    else:
        # par
        return (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2

# Intercambio de valores (temp)
a = 5
b = 10

temp = a
a = b
b = temp

print(a, b)  # 10 5

# Detección de un valor (flag)
numeros = [2, 4, 6, 8, 10]
flag = False

for n in numeros:
    if n == 6:
        flag = True
        break

if flag:
    print("El número 6 está en la lista.")
else:
    print("No se encontró el número.")

# Contar cuántos números positivos hay (contador)
numeros = [-2, 5, 3, -1, 0, 4]
contador = 0

for n in numeros:
    if n > 0:
        contador += 1

print(f"Hay {contador} números positivos.")

# Sumar todos los valores de una lista (acumulador)

numeros = [3, 5, 7, 2]
acumulador = 0

for n in numeros:
    acumulador += n

print(f"La suma total es {acumulador}.")

# Cuadrado perfecto
def cuadrado_perfecto(numero):
    cuadrados_perfectos = []

    if numero <= 0:
        return cuadrados_perfectos

    # Cuadrados perfectos no pares
    i = 1
    while i * i <= numero:
        if i * i % 2 != 0:
            cuadrados_perfectos.append(i * i)
        i += 1

    return cuadrados_perfectos

# Ejemplo de uso
numero = 20
print("Cuadrados perfectos que no son números pares hasta", numero, ":")
print(cuadrado_perfecto(numero))

# Calcular volumenes
import math

def volumen_prisma_rectangular():
    largo = float(input("Ingrese el largo del prisma (en metros): "))
    ancho = float(input("Ingrese el ancho del prisma (en metros): "))
    alto = float(input("Ingrese el alto del prisma (en metros): "))
    volumen_m3 = largo * ancho * alto
    volumen_litros = volumen_m3 * 1000
    print(f"El volumen del prisma rectangular es: {volumen_litros:.2f} litros\n")

def volumen_esfera():
    radio = float(input("Ingrese el radio de la esfera (en metros): "))
    volumen_m3 = (4/3) * math.pi * (radio ** 3)
    volumen_litros = volumen_m3 * 1000
    print(f"El volumen de la esfera es: {volumen_litros:.2f} litros\n")

def volumen_cilindro():
    radio = float(input("Ingrese el radio de la base del cilindro (en metros): "))
    altura = float(input("Ingrese la altura del cilindro (en metros): "))
    volumen_m3 = math.pi * (radio ** 2) * altura
    volumen_litros = volumen_m3 * 1000
    print(f"El volumen del cilindro es: {volumen_litros:.2f} litros\n")

def mostrar_menu():
    print("Menú de Opciones----------------------------------------------------------")
    print("1 - Calcular volumen contenedor prisma rectangular")
    print("2 - Calcular volumen contenedor esférico")
    print("3 - Calcular volumen contenedor cilíndrico")
    print("s - Salir")

# -----------------------
# FUNCIONES DE TEXTO
# -----------------------

def contar_palabras(texto):
    return len(texto.split())

def texto_en_mayusculas(texto):
    return texto.upper()

def texto_en_minusculas(texto):
    return texto.lower()

def capitalizar_texto(texto):
    return texto.capitalize()

# -----------------------
# FUNCIONES DE VALIDACIÓN
# -----------------------

def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

# -----------------------
# FUNCIONES PARA LISTAS
# -----------------------

def ordenar_lista(lista, descendente=False):
    return sorted(lista, reverse=descendente)

def eliminar_duplicados(lista):
    return list(set(lista))

def buscar_en_lista(lista, elemento):
    return elemento in lista

# -----------------------
# FUNCIONES DE IMPRESIÓN
# -----------------------

def mostrar_lista_en_columnas(lista):
    for i, item in enumerate(lista):
        print(f"{i + 1}. {item}")

def imprimir_separador(titulo=""):
    print("=" * 40)
    if titulo:
        print(f"{titulo}")
        print("=" * 40)

# -----------------------
# FUNCIONES DE ARCHIVOS
# -----------------------

def guardar_texto(nombre_archivo, contenido):
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)

def leer_texto(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Archivo no encontrado."
    
#------------------------
# FIBONACCI
#------------------------
fibonacci = [0, 1] 

for i in range(2, 100):  
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2] ) 

print("Los primeros 10 números de la sucesión de Fibonacci son:")
for num in fibonacci:
    print(num, end="-")

#------------------------
# ANIO BISIESTO
#------------------------
def es_bis(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

#------------------------
# USAR BREAK
#------------------------
segundo_anio = []
print("Ingrese los nombres de los estudiantes de segundo anio (ingrese S para finalizar): \n")
while True:
    nombre = input()
    if nombre == "S":
        break
    segundo_anio.append(nombre)

#------------------------
# CIFRADO DE CESAR
#------------------------
def cifrado_cesar(mensaje, corrimiento):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    return ''.join(
        alfabeto[(alfabeto.index(caracter) + corrimiento) % len(alfabeto)] if caracter in alfabeto else caracter
        for caracter in mensaje.upper()
    )
