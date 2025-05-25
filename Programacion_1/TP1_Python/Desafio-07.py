"""Desafío 7
    Desarrollar un programa que permita al usuario elegir un candidato por el cual votar.
    Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde,
    candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe
    imprimir el mensaje “Usted ha votado por el candidato [color que corresponda al
    candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de
    los candidatos disponibles, indicar “Opción errónea”.
"""
import continuar

candidatos = {
    'A' : 'Rojo',
    'B' : 'Verde' ,
    'C' : 'Azul' 
}
cA = 0
cB = 0
cC = 0
cant_vot = 0
c_voto_nulo = 0
while True:
    print('=========ELECCIONES 2025===========\n')
    print('1° - Candidato A - Partido Rojo\n')
    print('2° - Candidato B - Partido Verde\n')
    print('3° - Candidato C - Partido Azul\n')
    voto = input('Elija un candidato: (A|B|C))\n').upper().strip()
    cant_vot += 1
    if voto == 'A':
        print(f'Usted ha votado por el candidato: {candidatos["A"]}')
        cA += 1
    elif voto == 'B':
        print(f'Usted ha votado por el candidato: {candidatos["B"]}')
        cB += 1
    elif voto == 'C':
        print(f'Usted ha votado por el candidato: {candidatos["C"]}')
        cC += 1
    else:
        print('Opcion erronea')
        c_voto_nulo += 1
    if not continuar.continuarGen():
       break
print('=======RESULTADOS ELECCIONES 2025========')
print(f'Cantidad de Votantes: {cant_vot}')
print(f'Cantidad de Votos nulos: {c_voto_nulo}')

if cA > cB and cA > cC:
    print(f'El candidato ganador es: {candidatos["A"]} con {cA} votos')
    if cB > cC:
        print(f'Segundo lugar para: {candidatos["B"]} con {cB} votos')
        print(f'Tercer lugar para: {candidatos["C"]} con {cC} votos')
    else:
        print(f'Segundo lugar para: {candidatos["C"]} con {cC} votos')
        print(f'Tercer lugar para: {candidatos["B"]} con {cB} votos')
elif cB > cC:
    print(f'El candidato ganador es: {candidatos["B"]} con {cB} votos')
    if cA > cC:
        print(f'Segundo lugar para: {candidatos["A"]} con {cA} votos')
        print(f'Tercer lugar para: {candidatos["C"]} con {cC} votos')
    else:
        print(f'Segundo lugar para: {candidatos["C"]} con {cC} votos')
        print(f'Tercer lugar para: {candidatos["A"]} con {cA} votos')  
else:
    print(f'El candidato ganador es: {candidatos["C"]} con {cC} votos')
    if cB > cA:
        print(f'Segundo lugar para: {candidatos["B"]} con {cB} votos')
        print(f'Tercer lugar para: {candidatos["A"]} con {cA} votos')
    else:
        print(f'Segundo lugar para: {candidatos["A"]} con {cA} votos')
        print(f'Tercer lugar para: {candidatos["B"]} con {cB} votos') 