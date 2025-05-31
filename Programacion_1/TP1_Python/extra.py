# palabra = input('ingresa una palabra\n')
# Resultado = ' '.join(palabra)
# print(f'La cadena que ingresaste: ---> {Resultado}')
# numero = input('Ingresate un numero\n')
# Resultado = ' | '.join(numero)
# print(f'La cadena que ingresaste: ---> {Resultado}')


notas = []
continuar = ""


while True:
    continuar = (input('si para continuar , no para finalizar \n')).lower()
    if continuar == "si":
       nota = int(input('ingresa una nota de un alumno'))
       notas.append(nota)
       print(nota)
    
    elif continuar == "no":
        print('Gracias por utilizar el sistema')
        break
    else:
       print('desea continuar con el proceso? si / no')

def alumnos():
    sumnota = sum(notas)
    prom = sumnota / len(notas)

    return(prom)
promedio_un_curso = alumnos()
print('es ', promedio_un_curso)