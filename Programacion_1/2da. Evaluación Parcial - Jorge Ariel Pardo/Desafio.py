import continuar
from assets.Familia import Familia

class Desafio:
    #METODO TITULO DEL DESAFIO
    @staticmethod
    def titulo():
        print('=======================================================================')
        print('Desafio:')
        print('Desafío: Informar los datos de una familia.')
        print('=======================================================================')

    #MENU DE OPCIONES(ESTATICO)
    @staticmethod
    def menu():
        print('===========================')
        print('*******FAMILIA********')
        print('===========================')
        print('1 - CARGAR DATOS DE MADRE')
        print('2 - CARGAR DATOS DE PADRE')
        print('3 - CARGAR DATOS DE HIJOS')
        print('4 - MOSTRAR DATOS DE FAMILIA')
        print('S o 0 - SALIR')
    #IMPRIMIR DATOS DE FAMILIA
    def imprimir(self, familia):
        print('\n===== DATOS DE LA FAMILIA =====')
        if familia.madre:
            print(f'\nMadre: {familia.madre.nombre} {familia.madre.apellido}, Edad: {familia.madre.edad}, DNI: {familia.madre.DNI}, Sexo: {familia.madre.sexo}')
        else:
            print('\nMadre: no cargada')

        if familia.padre:
            print(f'\nPadre: {familia.padre.nombre} {familia.padre.apellido}, Edad: {familia.padre.edad}, DNI: {familia.padre.DNI}, Sexo: {familia.padre.sexo}')
        else:
            print('\nPadre: no cargado')

        if familia.list_hijos:
            print('\nHijos:')
            for i, hijo in enumerate(familia.list_hijos, 1):
                print(f'  Hijo {i}: {hijo.nombre} {hijo.apellido}, Edad: {hijo.edad}, DNI: {hijo.DNI}, Sexo: {hijo.sexo}')

            print(f'\nCantidad total de hijos: {familia.cantidad_hijos()}')
            print(f'Cantidad de hijas mujeres: {familia.cantidad_hijos_mujeres()}')
            print(f'Cantidad de hijos varones: {familia.cantidad_hijos_varones()}')

            familia.is_hijos_mayores()
            familia.is_hijos_menores()
        else:
            print('\nHijos: no cargados')
    #METODO PRINCIPAL CON EL MENU DE OPCIONES
    def operar(self):
        familia = Familia()

        while True:
            Desafio.menu()
            opc = input('Seleccione una operación\n').strip()

            match opc:
                case '1':
                    familia.cargar_madre()
                case '2':
                    familia.cargar_padre()
                case '3':
                    familia.cargar_hijos()
                case '4':
                    self.imprimir(familia)
                case 's' | '0':
                    print('Saliendo del programa...')
                    return
                case _:
                    print('Error, opción no válida')

def execute():
    parcial_2 = Desafio()
    Desafio.titulo()
    parcial_2.operar()

while True:
    execute()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break
