# ============================================================
#   SISTEMA DE AUDITORIA Y CONTROL DE INVENTARIO
#   Curso: Fundamentos de Programacion - UNAD
#   Problema 3 - Fase 5 Evaluacion Final POA
# ============================================================

import os

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


# ---------- LIMPIAR CONSOLA ----------
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


# ---------- PAUSA: esperar que el usuario decida ----------
def pausar():
    print(AZUL + "\n" + "=" * 58 + RESET)
    input(BLANCO + "  Presione ENTER para volver al menu principal..." + RESET)


# ---------- MOSTRAR TODOS LOS PRODUCTOS ----------
def mostrar_productos():
    limpiar_consola()
    print(AZUL + NEGRITA + "\n" + "=" * 58 + RESET)
    print(AZUL + NEGRITA + "   LISTA DE PRODUCTOS Y STOCK MINIMO REQUERIDO" + RESET)
    print(AZUL + NEGRITA + "=" * 58 + RESET)
    print(BLANCO + "  Stock en " + ROJO + "ROJO" + RESET + BLANCO + ": por debajo del minimo requerido." + RESET)
    print(BLANCO + "  Stock en " + VERDE + "VERDE" + RESET + BLANCO + ": nivel correcto o superior." + RESET)
    print(AZUL + "-" * 58 + RESET)
    print(BLANCO + NEGRITA + "  " + "N".ljust(4) + "Codigo".ljust(8) + "Articulo".ljust(22) + "Actual".rjust(8) + "Minimo".rjust(8) + RESET)
    print(AZUL + "-" * 58 + RESET)

    numero = 1
    for articulo in inventario:
        codigo       = articulo[0]
        nombre       = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        if stock_actual < stock_minimo:
            color_actual = ROJO
        else:
            color_actual = VERDE

        print(BLANCO + "  " + str(numero).ljust(4) + codigo.ljust(8) + nombre.ljust(22) + color_actual + str(stock_actual).rjust(8) + RESET + BLANCO + str(stock_minimo).rjust(8) + RESET)
        numero = numero + 1

    print(AZUL + "=" * 58 + RESET)
    print(AMARILLO + "  NOTA: Para ver el informe detallado de pedidos," + RESET)
    print(AMARILLO + "        seleccione la opcion 3 en el menu principal." + RESET)
    print(AZUL + "=" * 58 + RESET)
    pausar()


# ---------- ACTUALIZAR STOCK ----------
def actualizar_inventario():
    limpiar_consola()
    print(AMARILLO + NEGRITA + "\n" + "=" * 58 + RESET)
    print(AMARILLO + NEGRITA + "   ACTUALIZACION DE STOCK ACTUAL" + RESET)
    print(AMARILLO + NEGRITA + "=" * 58 + RESET)

    print(AMARILLO + "  COMO FUNCIONA ESTA SECCION:" + RESET)
    print(BLANCO + "  - Numero POSITIVO si recibio o agrego productos." + RESET)
    print(BLANCO + "    Ejemplo: llego un pedido de 20 lapiceros  ->  escriba: 20" + RESET)
    print(BLANCO + "  - Numero NEGATIVO si vendio o consumio productos." + RESET)
    print(BLANCO + "    Ejemplo: se vendieron 5 cuadernos        ->  escriba: -5" + RESET)
    print(BLANCO + "  - Presione ENTER sin escribir nada si no hubo cambios." + RESET)
    print(AMARILLO + "  " + "- " * 29 + RESET + "\n")

    for articulo in inventario:
        nombre       = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        while True:
            entrada = input(BLANCO + "  " + nombre.ljust(24) + " [actual: " + AMARILLO + str(stock_actual) + BLANCO + "] -> Ajuste (+/-): " + RESET)

            if entrada == "":
                print(VERDE + "     Sin cambios. Se mantiene en " + str(stock_actual) + " unidades. (Minimo: " + str(stock_minimo) + ")" + RESET)
                break
            else:
                try:
                    ajuste      = int(entrada)
                    nuevo_stock = stock_actual + ajuste

                    if nuevo_stock < 0:
                        print(ROJO + "     El stock no puede quedar negativo (" + str(nuevo_stock) + "). Intente de nuevo." + RESET)
                    else:
                        articulo[2] = nuevo_stock

                        if ajuste > 0:
                            print(VERDE + "     Se agregaron " + str(ajuste) + " unidades. Stock: " + str(stock_actual) + " -> " + str(nuevo_stock) + ". (Minimo: " + str(stock_minimo) + ")" + RESET)
                        else:
                            print(AMARILLO + "     Se descontaron " + str(abs(ajuste)) + " unidades. Stock: " + str(stock_actual) + " -> " + str(nuevo_stock) + ". (Minimo: " + str(stock_minimo) + ")" + RESET)

                        if nuevo_stock < stock_minimo:
                            faltante = stock_minimo - nuevo_stock
                            print(ROJO + "     ALERTA: Faltan " + str(faltante) + " unidades para el minimo requerido." + RESET)

                        break
                except ValueError:
                    print(ROJO + "     Ingrese un numero con signo (+10 o -10) o ENTER para dejar igual." + RESET)

    print(VERDE + NEGRITA + "\n  Proceso de actualizacion finalizado." + RESET)
    print(AMARILLO + "=" * 58 + RESET)
    pausar()


# ---------- MOSTRAR INFORME DE PEDIDOS ----------
def mostrar_informe():
    limpiar_consola()
    print(VERDE + NEGRITA + "\n" + "=" * 58 + RESET)
    print(VERDE + NEGRITA + "   INFORME DE AUDITORIA DE INVENTARIO" + RESET)
    print(VERDE + NEGRITA + "=" * 58 + RESET)
    print(BLANCO + "  Muestra el estado de cada producto y cuanto pedir." + RESET)
    print(BLANCO + "  Estado " + ROJO + "PEDIR" + RESET + BLANCO + ": stock insuficiente. Estado " + VERDE + "OK" + RESET + BLANCO + ": sin novedad." + RESET)
    print(VERDE + "-" * 58 + RESET)
    print(BLANCO + NEGRITA + "  " + "Codigo".ljust(8) + "Articulo".ljust(22) + "Actual".rjust(7) + "Minimo".rjust(7) + "A Pedir".rjust(9) + "  Estado" + RESET)
    print(VERDE + "-" * 58 + RESET)

    articulos_a_pedir = []

    for articulo in inventario:
        codigo         = articulo[0]
        nombre         = articulo[1]
        stock_actual   = articulo[2]
        stock_minimo   = articulo[3]
        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

        if cantidad_pedir > 0:
            estado = ROJO + "PEDIR" + RESET
            articulos_a_pedir.append((nombre, cantidad_pedir))
        else:
            estado = VERDE + "OK" + RESET

        print(BLANCO + "  " + codigo.ljust(8) + nombre.ljust(22) + str(stock_actual).rjust(7) + str(stock_minimo).rjust(7) + AMARILLO + str(cantidad_pedir).rjust(9) + RESET + "  " + estado)

    print(VERDE + "=" * 58 + RESET)
    print(AZUL + NEGRITA + "\n  RESUMEN DE PEDIDOS A REALIZAR:" + RESET)
    print(AZUL + "-" * 40 + RESET)

    if len(articulos_a_pedir) == 0:
        print(VERDE + "  Todo el inventario esta en orden. Sin pedidos." + RESET)
    else:
        numero = 1
        for item in articulos_a_pedir:
            nombre   = item[0]
            cantidad = item[1]
            print(BLANCO + "  " + str(numero) + ". " + nombre.ljust(22) + " Pedir: " + AMARILLO + str(cantidad) + " unidades" + RESET)
            numero = numero + 1

    print(AZUL + "-" * 40 + RESET)
    print(BLANCO + "  Total de articulos a reabastecer: " + AMARILLO + str(len(articulos_a_pedir)) + RESET)
    print(VERDE + "=" * 58 + RESET)
    pausar()


# ---------- MENU PRINCIPAL ----------
def menu():
    while True:
        limpiar_consola()
        print(AZUL + NEGRITA + "\n" + "=" * 58 + RESET)
        print(AZUL + NEGRITA + "   SISTEMA DE AUDITORIA Y CONTROL DE INVENTARIO" + RESET)
        print(AZUL + NEGRITA + "=" * 58 + RESET)
        print(BLANCO + "  1. Ver lista de productos" + RESET)
        print(BLANCO + "  2. Actualizar inventario (ingresar stock actual)" + RESET)
        print(BLANCO + "  3. Mostrar informe de pedidos" + RESET)
        print(BLANCO + "  4. Salir" + RESET)
        print(AZUL + "-" * 58 + RESET)

        opcion = input(BLANCO + "  Seleccione una opcion (1-4): " + RESET)

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            actualizar_inventario()
        elif opcion == "3":
            mostrar_informe()
        elif opcion == "4":
            limpiar_consola()
            print(VERDE + NEGRITA + "\n  Programa finalizado. Hasta pronto.\n" + RESET)
            break
        else:
            print(ROJO + "\n  Opcion invalida. Ingrese un numero del 1 al 4." + RESET)
            input(BLANCO + "  Presione ENTER para continuar..." + RESET)


# ---------- PROGRAMA PRINCIPAL ----------
menu()
