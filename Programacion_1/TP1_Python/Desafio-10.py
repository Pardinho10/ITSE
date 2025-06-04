"""Desafío 10
    Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. El instituto dicta clases a
    estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: los Lunes se dicta el nivel inicial, los Martes el nivel intermedio, los Miércoles el nivel avanzado, los Jueves son para práctica hablada y los Viernes se dicta inglés para viajeros.
    Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "día, DD/MM", donde [día] es un día de la semana, DD es el número de día y MM es el número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31 o el mes supere el número 12, finalizar el programa indicando que se produjo un error. Debe permitirse que ingrese el día de la semana en  minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
    Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el programa le mostrará el porcentaje de aprobados.
    Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la mayoría" si no es así.
    Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir "Comienzo de nuevo ciclo" y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego imprimir el ingreso total en $.
"""

import continuar
#MENU DE OPCIONES
def menu():
    print('=============================\n')
    print('  INSTITUTO APRENDER INGLÉS  \n')
    print('=============================\n')
    print('Seleccione una opcion para continuar\n')
    print('1) Cargar alumnos inscriptos por comisión\n')
    print('2) Ingresar una fecha para consultar\n')
    opcion = int(input())
    tupla_alumnos = None 
    match opcion: 
        case 1:
            tupla_alumnos = cargar_alumnos()
        case 2:
            tupla_fechas = fechas()
            if not tupla_fechas:
                print('Fecha inválida.')
                if not continuar.continuarGen():
                    print('========FIN DEL PROGRAMA=======')
                    exit()
                else:
                    return  # vuelve al menú principal
            if tupla_alumnos is None:
                print('Primero debe cargar los alumnos (opción 1)')
            else:
                consultas(tupla_fechas, tupla_alumnos)

#CARGA LA CANTIDAD DE ALUMNOS POR COMISION
def cargar_alumnos():
    canTot_inicial = int(input('Ingrese cantidad de alumnos inscriptos a Nivel Inicial\n'))
    canTot_intermedio = int(input('Ingrese cantidad de alumnos inscriptos a Nivel Intermedio\n'))
    canTot_avanzado = int(input('Ingrese cantidad de alumnos inscriptos a Nivel Avanzado\n'))
    canTot_hablado = int(input('Ingrese cantidad de alumnos inscriptos a Prática Hablada\n'))
    canTot_viajero = int(input('Ingrese cantidad de alumnos inscriptos a Inglés para Viajeros\n'))
    return canTot_inicial, canTot_intermedio, canTot_avanzado, canTot_hablado, canTot_viajero

#MANEJO DE FECHAS
def fechas():
   tupla_fecha = ingresar_fechas('Ingrese una fecha actual en formato dia, DD/MM:\n')
   return tupla_fecha
   
#SEPARACION DE LA CADENA FECHA
def ingresar_fechas(mensaje):
    fecha = input(mensaje).capitalize().strip()
    dia = fecha.split(', ')[0]
    dia_numero = int(fecha.split(', ')[1].split('/')[0])
    mes = int(fecha.split('/')[1])
    
    if validar_fecha(dia, dia_numero, mes ):        
        return dia, dia_numero, mes 
    else:
        return None

#VALIDACION DE LA FECHA 
def validar_fecha(dia, dia_numero, mes):
    dia_habiles = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    if dia in dia_habiles and (dia_numero > 0 and dia_numero <= 31) and (mes > 0 and mes <= 12):
        print('Fecha valida')
        return True
    elif dia in ('Domingo', 'Sabado'):
        print('Sabado y Domingo son dias no laborables')
    elif dia_numero < 0 or dia_numero > 31:
        print(f'Dia {dia_numero} no es un día de mes valido')
    elif mes < 0 or mes > 12:
        print(f'Mes {mes} no es un mes valido')
    else:
        print('dia invalido')
    return False

#CONSULTAS DEL EJERCICIO
def consultas(tupla_fechas, tupla_alumnos):
    canTot_inicial, canTot_intermedio, canTot_avanzado, canTot_hablado, canTot_viajero = tupla_alumnos
    dia, dia_numero, mes = tupla_fechas
    print(f'Fecha ingresada: {dia}, {dia_numero}/{mes}')   
    dias_examen = ['Lunes', 'Martes', 'Miercoles'] 

    if dia in dias_examen: 
        if (dia_numero >=10 and dia_numero <= 15) and (mes == 3 or mes == 7 or mes == 12):           
           resultado_examen(canTot_inicial, canTot_intermedio, canTot_avanzado)
        else:
            print('Dia normal de clases!')
    elif dia == 'Jueves':
        resultado_asistencia(canTot_hablado)
    elif dia == 'Viernes':
        if dia_numero == 1 and (mes == 1 or mes == 7):
            resultado_nuevo_ciclo(canTot_viajero)
        else:
            print('Dia normal de clases!')    
    else:
        print('No deberia pasar por aqui')

#RESULTADOS DE LA SEMANA DE EXAMENES
def resultado_examen(canTot_inicial, canTot_intermedio, canTot_avanzado):
    print('================SEMANA DE EXÁMENES!!===================\n')  
    canApro_inicial = int(input('Ingrese la cantidad de aprobados en Nivel Inicial'))
    canApro_intermedio = int(input('Ingrese la cantidad de aprobados en Nivel Intermedio'))
    canApro_avanzado = int(input('Ingrese la cantidad de aprobados en Nivel Avanzado'))
    canDApro_inicial = int(input('Ingrese la cantidad de desaprobados en Nivel Inicial'))
    canDApro_intermedio = int(input('Ingrese la cantidad de desaprobados en Nivel Intermedio'))
    canDApro_avanzado = int(input('Ingrese la cantidad de adesprobados en Nivel Avanzado'))
    porApro_inicial = (canApro_inicial / canTot_inicial) * 100
    porApro_intermedio = (canApro_intermedio / canTot_intermedio) * 100
    porApro_avanzado = (canApro_avanzado / canTot_avanzado) * 100
    porDApro_inicial = (canDApro_inicial / canTot_inicial) * 100
    porDApro_intermedio = (canDApro_intermedio / canTot_intermedio) * 100
    porDApro_avanzado = (canDApro_avanzado / canTot_avanzado) * 100
    print('=======RESULTADOS NIVEL INICIAL=========')
    print(f'Cantidad alumnos inscriptos: {canTot_inicial}')
    print(f'Alumnos aprobados: {canApro_inicial} ({porApro_inicial}%)')
    print(f'Alumnos desaprobados: {canDApro_inicial} ({porDApro_inicial}%)')
    print('=======RESULTADOS NIVEL INTERMEDIO=========')
    print(f'Cantidad alumnos inscriptos: {canTot_intermedio}')
    print(f'Alumnos aprobados: {canApro_intermedio} ({porApro_intermedio}%)')
    print(f'Alumnos desaprobados: {canDApro_intermedio} ({porDApro_intermedio}%)')
    print('=======RESULTADOS NIVEL AVANZADO=========')
    print(f'Cantidad alumnos inscriptos: {canTot_avanzado}')
    print(f'Alumnos aprobados: {canApro_avanzado} ({porApro_avanzado}%)')
    print(f'Alumnos desaprobados: {canDApro_avanzado} ({porDApro_avanzado}%)')

#ASSTENCIA DIA JUEVES
def resultado_asistencia(canTot_hablado):
    porAsis_hablado = float(input('Ingrese el porcentaje de asistencia del día'))
    print('Asistió la mayoria de alumnos\n' if porAsis_hablado > 50.0 else 'No asistió la mayoria')

#NUEVO CICLO COMISION VIERNES
def resultado_nuevo_ciclo(canTot_viajero):
    print('====================INICIO DE UN NUEVO CICLO LECTIVO=============================\n')
    canTot_viajero = int(input('Ingrese cantidad de alumnos inscriptos a Inglés para Viajeros:\n'))
    arancel_alumno = float(input('Ingrese el monto a abonar por alumno:\n'))
    ingreso_total = canTot_viajero * arancel_alumno
    print(f'Total de alumnos inscriptos para Inglés para Viajeros: {canTot_viajero}')
    print(f'Ingreso total ${ingreso_total} pesos')

#FUNCUON PRINCIPAL
def main():    
    menu()

while True:
    main()
    if not continuar.continuarGen():
        print('========FIN DEL PROGRAMA=======')
        break


