import continuar
import app

#FUNCION PRINCIPAL
def main():
    app.titulo()
    lista_fibo_str, lista_fibo = app.generar_fibo()
    app.mostrar_serie_fibo(lista_fibo_str, lista_fibo)
    if lista_fibo:
        lista_fibo_multiplos = app.multiplos_fibo(lista_fibo)
        app.mostrar_mutiplos_fibo(lista_fibo_multiplos)


while True:
    main()
    if not continuar.continuarGen():
        print('===========FIN DEL PROGRAMA===========')
        break
    
