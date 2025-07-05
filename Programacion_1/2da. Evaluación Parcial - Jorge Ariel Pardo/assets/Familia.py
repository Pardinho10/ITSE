from assets.Persona import Persona

class Familia:
    def __init__(self, madre=None, padre=None, hijo=None):
        self.madre = madre
        self.padre = padre
        self.list_hijos = hijo if hijo is not None else []

    def __str__(self):
        return f'{self.madre}'
    #CARGAR DATOS DE MADRE
    def cargar_madre(self):
        persona_madre = Persona()
        persona_madre.ingresar_datos_persona('Ingrese los datos personales de la madre\n')
        self.madre = persona_madre
    #CARGAR DATOS DE PADRE
    def cargar_padre(self):
        persona_padre = Persona()
        persona_padre.ingresar_datos_persona('Ingrese los datos personales del padre\n')
        self.padre = persona_padre

    #CARGAR DATOS DE HIJOS EN UNA LISTA
    def cargar_hijos(self):
        try:
            cant_hijos = int(input('Ingrese la cantidad de hijos de la familia\n'))
        except ValueError:
            print('Cantidad inválida.')
            return 

        for i in range(cant_hijos):
            persona_hijo = Persona()
            persona_hijo.ingresar_datos_persona(f'Ingrese los datos del hijo {i + 1}\n')
            self.list_hijos.append(persona_hijo)

    #HIJOS MAYORES DE EDAD
    def is_hijos_mayores(self):
        print('\n===== HIJOS MAYORES DE EDAD =====')
        hay_mayores = False
        for hijo in self.list_hijos:
            if hijo.edad >= 18:
                print(f'{hijo.nombre} {hijo.apellido} - Edad: {hijo.edad}')
                hay_mayores = True
        if not hay_mayores:
            print('No hay hijos mayores de edad.')
    #HIJOS MENORES DE EDAD
    def is_hijos_menores(self):
        print('\n===== HIJOS MENORES DE EDAD =====')
        hay_menores = False
        for hijo in self.list_hijos:
            if hijo.edad < 18:
                print(f'{hijo.nombre} {hijo.apellido} - Edad: {hijo.edad}')
                hay_menores = True
        if not hay_menores:
            print('No hay hijos menores de edad.')
    #CANTIDAD DE HIJOS DE LA FAMILIA
    def cantidad_hijos(self):
        print('\n===== CANTIDAD DE HIJOS =====')
        return len(self.list_hijos)   
    #CANTIDAD DE HIJAS MUJERES
    def cantidad_hijos_mujeres(self):
        cont_muj = 0
        print('\n===== CANTIDAD DE HIJOS MUJERES =====')
        for muj in self.list_hijos:
            if muj.sexo == 'f':
                cont_muj += 1
        return cont_muj    
    #CANTIDAD DE HIJOS VARONES
    def cantidad_hijos_varones(self):
        cont_varo = 0
        print('\n===== CANTIDAD DE HIJOS VARONES =====')
        for varo in self.list_hijos:
            if varo.sexo == 'm':
                cont_varo += 1
        return cont_varo
