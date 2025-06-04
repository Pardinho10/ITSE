import continuar
import funcionesUtiles
import random

def cargar_lista():
    N = input('Ingrese la cantidad de alumnos que rindieron el exámen\n')
    lista_alumn_nota = []
    if funcionesUtiles.es_entero(N):
        cantidad = int(N)
        if funcionesUtiles.es_positivo(cantidad):
            i = 1
            while i <= cantidad:
                nombre = input('Ingrese nombre del alumno\n').capitalize().strip()
                nota = round(random.uniform(0,10), 2)
                if nombre and (nota >= 0 and nota <= 10):
                    lista_alumn_nota.append((nombre, nota))
                    i += 1
                else:
                    print('Informacion incorrecta, ingrese los datos nuevamente\n')
            return lista_alumn_nota
        elif cantidad == 0:
            return [] # Lista vacia, sin elementos
    else:
        return None # Valor no valido (simbolo, letra, etc)
    
def mostrar_lista(lista):
    match lista:
        case []:
            print('No asistieron alumnos al exámen')
        case None:
            print('Valor incorrecto, ingrese un numero entero mayor o igual a 0')
        case _:
            print('================ALUMNOS Y SUS NOTAS==============\n')
            print('N° | NOMBRE       | CALIFICACIÓN')
            print('-----------------------------------------------')
            for indice, (nombre, nota) in enumerate(lista):
                print(f'{indice} | {nombre}     | {nota}')

def calcular_promedio(lista):
    suma_not = 0
    for nombre, nota in lista:
        suma_not += nota
    if len(lista) > 0:
        return suma_not / len(lista)
    else:
        print('No puede calcularse el prmedio de notas por que no asistieron alumnos')

def alumnos_aprobados(lista):
    lista_aprobados = []
    lista_desaprobados = []
    for nombre, nota in lista:
        if nota >= 6:
            lista_aprobados.append((nombre, nota))
        else:
            lista_desaprobados.append((nombre, nota))
    return lista_desaprobados, lista_aprobados

def mostrar_listas_calificaciones(lista_aprobados, lista_desaprobados):
    while True:
        print('================RESUMEN DE EXÁMEN==============\n')
        print('Ingrese una opción del menú')
        print('1- LISTADO ALUMNOS APROBADOS')
        print('2- LISTADO ALUMNOS DESAPROBADOS')
        print('3- RESUMEN GENERAL')
        print('0- SALIR')
        opcion = input('Ingrese una opcion \n')
        if funcionesUtiles.es_entero(opcion):
            opc = int(opcion)
            if funcionesUtiles.es_positivo(opc):
                match opc:
                    case 1:
                        mostrar_aprobados(lista_aprobados)
                    case 2:
                        mostrar_desaprobados(lista_desaprobados)
                    case 3:
                        resumen_examen(lista_aprobados, lista_desaprobados)
                    case 0:
                        break
                    case _:
                        print('Ingrse una opcion valida (entero entre 1-3)')

def mostrar_aprobados(lista_aprobados):
    print('================LISTADO DE ALUMNOS APROBADOS==============\n')
    print('N° | NOMBRE       | CALIFICACIÓN')
    print('-----------------------------------------------')
    for indice, (nombre, nota) in enumerate(lista_aprobados):
        print(f'{indice} | {nombre}     | {nota}')

def mostrar_desaprobados(lista_desaprobados):
    print('================LISTADO DE ALUMNOS DESAPROBADOS==============\n')
    print('N° | NOMBRE       | CALIFICACIÓN')
    print('-----------------------------------------------')
    for indice, (nombre, nota) in enumerate(lista_desaprobados):
        print(f'{indice} | {nombre}     | {nota}')

def resumen_examen(lista_aprobados, lista_desaprobados):
    total_alumnos_examen = len(lista_aprobados) + len(lista_desaprobados)
    if total_alumnos_examen > 0:
        porcentaje_desapro = (len(lista_desaprobados) / total_alumnos_examen) * 100
        porcentaje_apro = (len(lista_aprobados) / total_alumnos_examen) * 100
        print(f'Cantidad Total de alumnos ---> {total_alumnos_examen}')
        print(f'Cantidad de alumons aprobados ----> {len(lista_aprobados)} --> {porcentaje_apro}%')
        print(f'Cantidad de alumons desaprobados ----> {len(lista_desaprobados)} --> {porcentaje_desapro}%')
    else:
        print('No asistieron alumnos al exámen')

def convertir__diccionario(lista_estudiantes):
    diccionario_de_tuplas = dict(lista_estudiantes)
    print(diccionario_de_tuplas)


def main():
    lista_estudiantes = cargar_lista()
    mostrar_lista(lista_estudiantes)
    if lista_estudiantes:
        promedio = calcular_promedio(lista_estudiantes)
        print(f'El promedio general de notas es: {promedio}')
        lista_desaprobados, lista_aprobados =  alumnos_aprobados(lista_estudiantes)
        mostrar_listas_calificaciones(lista_aprobados, lista_desaprobados)
        convertir__diccionario(lista_estudiantes)

while True:
    main()
    if not continuar.continuarGen():
        print('=============FIN DEL PROGRAMA=============')
        break


