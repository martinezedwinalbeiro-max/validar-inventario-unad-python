# ============================================================
#   SISTEMA DE AUDITORIA Y CONTROL DE INVENTARIO
#   Curso: Fundamentos de Programacion - UNAD
#   Problema 3 - Fase 5 Evaluacion Final POA
# ============================================================

import os

# ---------- LIMPIAR CONSOLA ----------
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

# ---------- COLORES PARA CONSOLA ----------
AZUL     = "\033[94m"
VERDE    = "\033[92m"
ROJO     = "\033[91m"
AMARILLO = "\033[93m"
BLANCO   = "\033[97m"
RESET    = "\033[0m"
NEGRITA  = "\033[1m"

# ---------- DATOS DEL INVENTARIO ----------
# Formato: [Codigo, Nombre, Stock Actual, Stock Minimo Requerido]
inventario = [
    ["A001", "Cuadernos",        18,  25],
    ["A002", "Lapiceros",        52,  50],
    ["A003", "Resmas de Papel",   7,  20],
    ["A004", "Carpetas",          2,  15],
    ["A005", "Marcadores",       10,  10],
    ["A006", "Tijeras",           3,   8],
    ["A007", "Pegante",          14,  12],
]


# ---------- MODULO: calcular cantidad a pedir ----------
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Retorna la cantidad a pedir de un articulo.
    Si el stock actual es menor al minimo, retorna la diferencia.
    Si el stock es suficiente, retorna 0.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# ---------- PAUSA: esperar que el usuario decida ----------
def pausar():
    print(f"\n{AZUL}{'=' * 58}{RESET}")
    input(f"{BLANCO}  Presione ENTER para volver al menu principal...{RESET}")


# ---------- MOSTRAR TODOS LOS PRODUCTOS ----------
def mostrar_productos():
    limpiar_consola()
    print(f"\n{AZUL}{NEGRITA}{'=' * 58}{RESET}")
    print(f"{AZUL}{NEGRITA}   LISTA DE PRODUCTOS Y STOCK MINIMO REQUERIDO{RESET}")
    print(f"{AZUL}{NEGRITA}{'=' * 58}{RESET}")
    print(f"{BLANCO}  Stock en {ROJO}ROJO{RESET}{BLANCO}: por debajo del minimo requerido.{RESET}")
    print(f"{BLANCO}  Stock en {VERDE}VERDE{RESET}{BLANCO}: nivel correcto o superior.{RESET}")
    print(f"{AZUL}{'-' * 58}{RESET}")
    print(f"{BLANCO}{NEGRITA}  {'N':<4} {'Codigo':<8} {'Articulo':<22} {'Actual':>8} {'Minimo':>8}{RESET}")
    print(f"{AZUL}{'-' * 58}{RESET}")

    for i, articulo in enumerate(inventario, start=1):
        codigo       = articulo[0]
        nombre       = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        if stock_actual < stock_minimo:
            color_actual = ROJO
        else:
            color_actual = VERDE

        print(f"{BLANCO}  {i:<4} {codigo:<8} {nombre:<22} {color_actual}{stock_actual:>8}{RESET} {BLANCO}{stock_minimo:>8}{RESET}")

    print(f"{AZUL}{'=' * 58}{RESET}")
    print(f"{AMARILLO}  NOTA: Para ver el informe detallado de pedidos,{RESET}")
    print(f"{AMARILLO}        seleccione la opcion 3 en el menu principal.{RESET}")
    print(f"{AZUL}{'=' * 58}{RESET}")
    pausar()


# ---------- ACTUALIZAR STOCK ----------
def actualizar_inventario():
    limpiar_consola()
    print(f"\n{AMARILLO}{NEGRITA}{'=' * 58}{RESET}")
    print(f"{AMARILLO}{NEGRITA}   ACTUALIZACION DE STOCK ACTUAL{RESET}")
    print(f"{AMARILLO}{NEGRITA}{'=' * 58}{RESET}")
    print(f"{BLANCO}  Ingrese el stock actual para cada producto:{RESET}\n")

    print(f"{AMARILLO}  COMO FUNCIONA ESTA SECCION:{RESET}")
    print(f"{BLANCO}  - Escriba un numero POSITIVO si recibio o agrego productos.{RESET}")
    print(f"{BLANCO}    Ejemplo: llego un pedido de 20 lapiceros  ->  escriba: 20{RESET}")
    print(f"{BLANCO}  - Escriba un numero NEGATIVO si vendio o consumio productos.{RESET}")
    print(f"{BLANCO}    Ejemplo: se vendieron 5 cuadernos        ->  escriba: -5{RESET}")
    print(f"{BLANCO}  - Presione ENTER sin escribir nada si no hubo cambios.{RESET}")
    print(f"{AMARILLO}  {'- ' * 29}{RESET}\n")

    for articulo in inventario:
        nombre       = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        while True:
            entrada = input(f"  {BLANCO}{nombre:<24} [actual: {AMARILLO}{stock_actual}{BLANCO}] -> Ajuste (+/-): {RESET}")

            if entrada == "":
                print(f"  {VERDE}  Sin cambios. Se mantiene en {stock_actual} unidades. (Minimo: {stock_minimo}){RESET}")
                break
            else:
                try:
                    ajuste = int(entrada)
                    nuevo_stock = stock_actual + ajuste

                    if nuevo_stock < 0:
                        print(f"  {ROJO}  El stock no puede quedar negativo ({nuevo_stock}). Intente de nuevo.{RESET}")
                    else:
                        articulo[2] = nuevo_stock
                        if ajuste > 0:
                            print(f"  {VERDE}  Se agregaron {ajuste} unidades. Stock: {stock_actual} -> {nuevo_stock}. (Minimo: {stock_minimo}){RESET}")
                        else:
                            print(f"  {AMARILLO}  Se descontaron {abs(ajuste)} unidades. Stock: {stock_actual} -> {nuevo_stock}. (Minimo: {stock_minimo}){RESET}")

                        if nuevo_stock < stock_minimo:
                            faltante = stock_minimo - nuevo_stock
                            print(f"  {ROJO}  ALERTA: Faltan {faltante} unidades para el minimo requerido.{RESET}")
                        break
                except ValueError:
                    print(f"  {ROJO}  Ingrese un numero con signo (+10 o -10) o ENTER para dejar igual.{RESET}")

    print(f"\n{VERDE}{NEGRITA}  Proceso de actualizacion finalizado.{RESET}")
    print(f"{AMARILLO}{'=' * 58}{RESET}")
    pausar()


# ---------- MOSTRAR INFORME DE PEDIDOS ----------
def mostrar_informe():
    limpiar_consola()
    print(f"\n{VERDE}{NEGRITA}{'=' * 58}{RESET}")
    print(f"{VERDE}{NEGRITA}   INFORME DE AUDITORIA DE INVENTARIO{RESET}")
    print(f"{VERDE}{NEGRITA}{'=' * 58}{RESET}")
    print(f"{BLANCO}  Muestra el estado de cada producto y cuanto pedir.{RESET}")
    print(f"{BLANCO}  Estado {ROJO}PEDIR{RESET}{BLANCO}: stock insuficiente. Estado {VERDE}OK{RESET}{BLANCO}: sin novedad.{RESET}")
    print(f"{VERDE}{'-' * 58}{RESET}")
    print(f"{BLANCO}{NEGRITA}  {'Codigo':<8} {'Articulo':<22} {'Actual':>7} {'Minimo':>7} {'A Pedir':>8}  {'Estado'}{RESET}")
    print(f"{VERDE}{'-' * 58}{RESET}")

    articulos_a_pedir = []

    for articulo in inventario:
        codigo       = articulo[0]
        nombre       = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

        if cantidad_pedir > 0:
            estado = f"{ROJO}PEDIR{RESET}"
            articulos_a_pedir.append((nombre, cantidad_pedir))
        else:
            estado = f"{VERDE}OK   {RESET}"

        print(f"{BLANCO}  {codigo:<8} {nombre:<22} {stock_actual:>7} {stock_minimo:>7} {AMARILLO}{cantidad_pedir:>8}{RESET}  {estado}")

    print(f"{VERDE}{'=' * 58}{RESET}")

    print(f"\n{AZUL}{NEGRITA}  RESUMEN DE PEDIDOS A REALIZAR:{RESET}")
    print(f"{AZUL}{'-' * 40}{RESET}")

    if len(articulos_a_pedir) == 0:
        print(f"{VERDE}  Todo el inventario esta en orden. Sin pedidos.{RESET}")
    else:
        for i, (nombre, cantidad) in enumerate(articulos_a_pedir, start=1):
            print(f"{BLANCO}  {i}. {nombre:<22} Pedir: {AMARILLO}{cantidad} unidades{RESET}")

    print(f"{AZUL}{'-' * 40}{RESET}")
    print(f"{BLANCO}  Total de articulos a reabastecer: {AMARILLO}{len(articulos_a_pedir)}{RESET}")
    print(f"{VERDE}{'=' * 58}{RESET}")
    pausar()


# ---------- MENU PRINCIPAL ----------
def menu():
    while True:
        limpiar_consola()
        print(f"\n{AZUL}{NEGRITA}{'=' * 58}{RESET}")
        print(f"{AZUL}{NEGRITA}   SISTEMA DE AUDITORIA Y CONTROL DE INVENTARIO{RESET}")
        print(f"{AZUL}{NEGRITA}{'=' * 58}{RESET}")
        print(f"{BLANCO}  1. Ver lista de productos{RESET}")
        print(f"{BLANCO}  2. Actualizar inventario (ingresar stock actual){RESET}")
        print(f"{BLANCO}  3. Mostrar informe de pedidos{RESET}")
        print(f"{BLANCO}  4. Salir{RESET}")
        print(f"{AZUL}{'-' * 58}{RESET}")

        opcion = input(f"{BLANCO}  Seleccione una opcion (1-4): {RESET}")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            actualizar_inventario()
        elif opcion == "3":
            mostrar_informe()
        elif opcion == "4":
            limpiar_consola()
            print(f"\n{VERDE}{NEGRITA}  Programa finalizado. Hasta pronto.{RESET}\n")
            break
        else:
            print(f"\n{ROJO}  Opcion invalida. Ingrese un numero del 1 al 4.{RESET}")
            input(f"{BLANCO}  Presione ENTER para continuar...{RESET}")


# ---------- PROGRAMA PRINCIPAL ----------
menu()