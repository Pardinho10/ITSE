"""Desafío 37
    Una Chocolatería tiene a la venta bombones en cajas de 5, 8 y 13 unidades.
    Desarrollar una función que reciba el dato de la cantidad de bombones pedida por el cliente, luego, calcular e informar si es posible entregar el pedido y con cuantas cajas de cada tamaño o no es posible armar una entrega con esa cantidad pedida.
    Utilice varias estrategias para realizar el calculo. Luego, testear cada estrategia con 13 cantidades generadas aleatoriamente de un rango de entre 1 a 1000.
"""

import random
import continuar

# TAMAÑOS DE CAJAS DISPONIBLES
cajas = (13, 8, 5)

# ESTRATEGIA 1: VORAZ — USAR LAS CAJAS MÁS GRANDES PRIMERO
def estrategia_voraz(pedido):
    # INTENTA USAR LA MAYOR CANTIDAD POSIBLE DE CAJAS GRANDES
    for c13 in range(pedido // 13 + 1):
        for c8 in range((pedido - c13 * 13) // 8 + 1):
            for c5 in range((pedido - c13 * 13 - c8 * 8) // 5 + 1):
                total = c13 * 13 + c8 * 8 + c5 * 5
                if total == pedido:
                    return c13, c8, c5
    return None

# ESTRATEGIA 2: BACKTRACKING CON RECURSIÓN
def estrategia_backtracking(pedido, usados=None):
    if usados is None:
        usados = [0, 0, 0]  # INICIALIZA CONTADOR DE CAJAS [13, 8, 5]

    if pedido == 0:
        return usados

    if pedido < 0:
        return None

    for i, tamaño in enumerate(cajas):
        usados[i] += 1
        resultado = estrategia_backtracking(pedido - tamaño, usados[:])
        if resultado:
            return resultado
        usados[i] -= 1
    return None

# ESTRATEGIA 3: PROGRAMACIÓN DINÁMICA (BOTTOM-UP)
def estrategia_dinamica(pedido):
    dp = [None] * (pedido + 1)
    dp[0] = (0, 0, 0)  # BASE: 0 BOMBONES → 0 CAJAS

    for i in range(1, pedido + 1):
        for j, tamaño in enumerate(cajas):
            if i >= tamaño and dp[i - tamaño] is not None:
                anterior = dp[i - tamaño]
                nuevo = list(anterior)
                nuevo[j] += 1
                dp[i] = tuple(nuevo)
                break  # SE DETIENE EN LA PRIMERA COMBINACIÓN VÁLIDA

    return dp[pedido]


# MUESTRA LOS RESULTADOS DE CADA ESTRATEGIA
def mostrar_resultado(pedido, resultado, metodo):
    print(f'\n{metodo} → PEDIDO: {pedido} bombones')
    if resultado:
        c13, c8, c5 = resultado
        print(f'CAJAS DE 13: {c13} | DE 8: {c8} | DE 5: {c5}')
        total = c13 * 13 + c8 * 8 + c5 * 5
        print(f'TOTAL ENTREGADO: {total} bombones')
    else:
        print('NO SE PUEDE CUMPLIR EL PEDIDO CON LAS CAJAS DISPONIBLES')


# GENERA 13 PEDIDOS ALEATORIOS Y LOS TESTEA
def testear_estrategias():
    print('================= DESAFÍO 37: CAJAS DE BOMBONES =================\n')
    pedidos = [random.randint(1, 1000) for _ in range(13)]

    for pedido in pedidos:
        mostrar_resultado(pedido, estrategia_voraz(pedido), 'ESTRATEGIA VORAZ')
        mostrar_resultado(pedido, estrategia_backtracking(pedido), 'ESTRATEGIA BACKTRACKING')
        mostrar_resultado(pedido, estrategia_dinamica(pedido), 'ESTRATEGIA DINÁMICA')
        print('-----------------------------------------------------------------')


# PROGRAMA PRINCIPAL
if __name__ == '__main__':
    testear_estrategias()
