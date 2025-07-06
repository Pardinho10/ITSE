""" Desafío 4
Desarrollar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el e-mail. Además se deberá presentar un Menú de Opciones con las siguientes opciones:

Crear contacto
Borrar contacto
Editar contacto
Lista de contactos
Buscar contacto
Cerrar agenda """

import continuar
from funcionesUtiles import es_cadena, es_flotante, es_entero, es_positivo, es_email_valido
import re

class Contacto():
    def __init__(self, nombre = '', ape = '', tel = 0, mail = ''):
        self.__nombre =  nombre
        self.__apellido = ape
        self.__telefono = tel
        self.__email = mail

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def email(self):
        return self.__email
    
    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError('El nombre debe ser una cadena de texto')
        if len(nombre.strip()) < 3 or len(nombre.strip()) > 30:
            raise ValueError("El nombre debe tener al menos 3 caracteres y no más de 30")
        self.__nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        if not isinstance(apellido, str):
            raise TypeError('El apellido debe ser una cadena de texto')
        if len(apellido.strip()) < 3 or len(apellido.strip()) > 30:
            raise ValueError("El apellido debe tener al menos 3 caracteres y no más de 30")
        self.__apellido = apellido

    @telefono.setter
    def telefono(self, tel):
        if not isinstance(tel, int):
            raise TypeError ('El telefono debe ser un número entero')
        if tel < 1000000000 or tel > 9999999999:
            raise ValueError('El telefono debe ser un entero entre 1000000 y 99999999')
        self.__telefono = tel

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError('El email debe ser una cadena de texto')        
        email = email.strip()        
        if len(email) < 3 or len(email) > 30:
            raise ValueError("El email debe tener al menos 3 caracteres y no más de 30")
        #Validacion de email usadno expresiones regulares
        patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if not re.match(patron, email):
            raise ValueError("Formato de email inválido. Ejemplo válido: nombre@dominio.com")
        self.__email = email

    def ingresar_datos_contacto(self):
        while True:
            nombre = input('Ingrese el nombre del conatcto\n').strip().capitalize()
            if es_cadena(nombre):
                try:
                    self.nombre = nombre
                    break
                except ValueError as e:
                    print(f'Error : {e}')
            else:
                print('El nombre ingresado es invalido. Solo se permiten letras y espacios internos')
                
        while True:
            apellido = input(f'Ingrese el apellido de {self.nombre}\n').strip().capitalize()
            if es_cadena(apellido):
                try:
                    self.apellido = apellido
                    break
                except ValueError as e:
                    print(f'Error : {e}')
            else:
                print('El apellido ingresado es invalido. Solo se permiten letras y espacios internos')

        while True:
            telefono = input(f'Ingrese el telefono para {self.nombre}\n')
            if es_entero(telefono) and es_positivo(int(telefono)):
                try:
                    self.telefono = int(telefono)
                    break
                except (ValueError, TypeError) as e:
                    print(f'Error: {e}')
            else:
                print('El teléfono ingresada es incorrecta. teléfono debe  ser un número entero.')

        while True:
            email = input(f'Ingrese el email para {self.email}\n')
            if es_email_valido(email):
                try:
                    self.email = email
                    break
                except (ValueError, TypeError) as e:
                    print(f'Error: {e}')
            else:
                print('El correo ingresado es invalido. Solo se permiten caracteres alfanumericos') 


    def __str__(self):
        print('====== DATOS DEL CONTACTO ======')
        return f'Nombre: {self.nombre} {self.apellido} | Teléfono: {self.telefono} | Email: {self.email}'


class Agenda():
    def __init__(self, contacto = None):
        self.list_contacto = contacto if contacto is not None else []

    def crear_contacto(self):
        print('=INGRESAR DATOS DE CONTACTO=')
        while True:
            contact = Contacto()
            contact.ingresar_datos_contacto()   
            self.list_contacto.append(contact)
            conti  = input('Desea ingresar un nuevo contacto? (si|no)\n').lower().strip()
            if conti == 'no':
                break

    def borrar_contacto(self):
        print('=BORRAR CONTACTO ESPECÍFICO=')
        if not self.list_contacto:
            print("No hay contactos cargados.")
            return

        while True:
            self.listar_contacto_reducido()
            try:
                opc = int(input('Seleccione un contacto de la lista para eliminar\n').strip())
                if opc < 1 or opc > len(self.list_contacto):
                    print("Opción inválida. Intente de nuevo.")
                    continue
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
                continue

            contacto_a_eliminar = self.list_contacto[opc - 1]
            print('\nEstá por eliminar el siguiente contacto:')
            print(contacto_a_eliminar)

            confirmar = input('¿Desea continuar? (si|no): ').strip().lower()
            if confirmar == 'si':
                self.list_contacto.remove(contacto_a_eliminar)
                print("Contacto eliminado con éxito.")
            else:
                print("Eliminación cancelada.")

            repetir = input('¿Desea eliminar otro contacto? (si|no): ').strip().lower()
            if repetir != 'si':
                break
             

    def editar_contacto(self):
        print('=EDITAR CONTACTO ESPECÍFICO=')
        if not self.list_contacto:
            print("No hay contactos cargados.")
            return
        while True:
            self.listar_contacto_reducido()
            try:
                opc = int(input('Seleccione un contacto de la lista para editar\n').strip())
                if opc < 1 or opc > len(self.list_contacto):
                    print("Opción inválida. Intente de nuevo.")
                    continue
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
                continue
            for i, cont in enumerate(self.list_contacto, 1):
                if opc == i:
                    cont.ingresar_datos_contacto()
                    print(cont)
            
            repetir = input('¿Desea editar otro contacto? (si|no): ').strip().lower()
            if repetir != 'si':
                break

    def listar_contacto(self):
        print('=LISTA DE CONTACTOS AGENDADOS=')
        if not self.list_contacto:
            print("No hay contactos cargados.")
            return

        print('==================================================')
        print('N°   NOMBRE COMPLETO         TELÉFONO        EMAIL')
        print('==================================================')
        for i, contacto in enumerate(self.list_contacto, 1):
            nombre_completo = f"{contacto.nombre} {contacto.apellido}"
            print(f'{i:<5}{nombre_completo:<25}{contacto.telefono:<15}{contacto.email}')

    def listar_contacto_reducido(self):
        print('=LISTA REDUCIDA DE CONTACTOS AGENDADOS=')
        if not self.list_contacto:
            print("No hay contactos cargados.")
            return

        print('=============================')
        print('N°   NOMBRE COMPLETO    ')
        print('=============================')
        for i, contacto in enumerate(self.list_contacto, 1):
            nombre_completo = f"{contacto.nombre} {contacto.apellido}"
            print(f'{i:<5}{nombre_completo:<25}')

    def buscar_contacto(self):
        print('=MOSTRAR DATOS DE CONTACTO ESPECIFICO=')
        if not self.list_contacto:
            print("No hay contactos cargados.")
            return
        while True:
            self.listar_contacto_reducido()
            try:
                opc = int(input('Seleccione un contacto de la lista para mostrar su informacion\n').strip())
                if opc < 1 or opc > len(self.list_contacto):
                    print("Opción inválida. Intente de nuevo.")
                    continue
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
                continue
            for i, cont in enumerate(self.list_contacto, 1):
                if opc == i:
                    print(cont)  
            
            repetir = input('¿Desea buscar otro contacto? (si|no): ').strip().lower()
            if repetir != 'si':
                break


    @staticmethod
    def menu_agenda():
        print('============================')
        print('******* AGENDA ITSE ********')
        print('============================')
        print('1 - CREAR CONTACTO')
        print('2 - BORRAR CONTACTO')
        print('3 - EDITAR CONTACTO')
        print('4 - LISTAR CONTACTOS')
        print('5 - BUSCAR CONTACTO')
        print('S o 0- CERRAR AGENDA')

    def operar_agenda(self):
        while True:
            Agenda.menu_agenda()
            opc = input('Seleccione una operación\n').strip()
            match opc:
                case '1':
                    self.crear_contacto()   
                case '2':
                    self.borrar_contacto()
                case '3':
                    self.editar_contacto()
                case '4':
                    self.listar_contacto()
                case '5':
                    self.buscar_contacto()
                case 's' | '0':
                    print('Cerrando agenda...')
                    return
                case _:
                    print('Error, opcion no valida')

def desafio_4():
    agenda = Agenda()
    agenda.operar_agenda()

while True:
    desafio_4()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break