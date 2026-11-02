# Grupo: B - Calculadora Multifunción
# Integrantes: Iker Sánchez Prieto, Roger Pedra Vilalta y Bernat Marín López

from utils import EntradaSalida as es
from operaciones import CalculadoraAritmetica
from notas import calcular_media_ponderada_interactiva
from calculos import potencia_dos, logaritmo_base_dos
from conversiones import convertir_base, convertir_unidades

# El menú conecta las entradas con los módulos de cálculo y conversión.
# Las opciones del menú se corresponden con su posición en estas listas.
menuGeneral = [
    "Operaciones aritméticas",
    "Cálculo de media ponderada",
    "Conversión de bases numéricas",
    "Conversión de unidades informáticas",
    "Cálculo de potencias de 2",
    "Logaritmos en base 2",
]
submenuAritmetica = ["Suma", "Resta", "Multiplicación", "División"]


def mostrar_titulo(titulo):
    """Imprime un título centrado para distinguir las secciones de la consola."""
    print("\n" + "=" * 42)
    print(titulo.center(42))
    print("=" * 42)


def printMenu(menu, textoOpcionCero="Salir", titulo="Menú"):
    """Muestra las opciones y devuelve una selección válida.

    Args:
        menu: Lista de opciones que se van a mostrar.
        textoOpcionCero: Texto asociado a la opción 0.
        titulo: Título que aparece encima de las opciones.

    Returns:
        La opción elegida, entre 0 y la cantidad de elementos del menú.
    """
    mostrar_titulo(titulo)
    for numero, opcion in enumerate(menu, start=1):
        print(f"  {numero}. {opcion}")
    print(f"  0. {textoOpcionCero}\n")

    # El bucle mantiene el menú abierto hasta que se introduce una opción del rango.
    opcion = es.tecladoInt("Selecciona una opción: ")
    while opcion < 0 or opcion > len(menu):
        print("Opción inválida. Inténtalo de nuevo.\n")
        opcion = es.tecladoInt("Selecciona una opción: ")
    return opcion


def ejecutar_operacion(calculadoraAritmetica, opcion):
    """Pide dos números, ejecuta una operación y permite repetirla.

    Args:
        calculadoraAritmetica: Instancia que realiza el cálculo.
        opcion: Número de la operación seleccionada en el submenú.
    """
    nombre = submenuAritmetica[opcion - 1].lower()
    mostrar_titulo(nombre.capitalize())

    while True:
        numero1 = es.tecladoFloat("  Primer número: ")
        numero2 = es.tecladoFloat("  Segundo número: ")

        # Cada rama selecciona el método asociado a la opción.
        try:
            if opcion == 1:
                resultado = calculadoraAritmetica.suma(numero1, numero2)
            elif opcion == 2:
                resultado = calculadoraAritmetica.resta(numero1, numero2)
            elif opcion == 3:
                resultado = calculadoraAritmetica.multiplicacion(numero1, numero2)
            elif opcion == 4:
                resultado = calculadoraAritmetica.division(numero1, numero2)
            else:
                print("Opción de operación inválida.\n")
                return
            print(f"\n  Resultado: {resultado}\n")
        except ValueError as error:
            # La división avisa si el divisor es cero; se informa sin salir.
            print(f"\n  Error: {error}\n")

        # Se valida la respuesta antes de repetir o volver al submenú.
        repetir = input("¿Quieres hacer otra operación del mismo tipo? (s/n): ").strip().lower()
        while repetir not in ("s", "si", "sí", "n", "no"):
            repetir = input("Responde s o n: ").strip().lower()
        if repetir in ("n", "no"):
            print()
            break
        print(f"\n¡Seguimos con la {nombre}!\n")


def repetir_calculo():
    """Pregunta si se quiere repetir una operación de ingeniería."""
    repetir = input("¿Quieres hacer otro cálculo? (s/n): ").strip().lower()
    while repetir not in ("s", "si", "sí", "n", "no"):
        repetir = input("Responde s o n: ").strip().lower()
    return repetir in ("s", "si", "sí")


def ejecutar_calculo_ingenieria(opcion):
    """Gestiona la entrada, el cálculo y la repetición de las opciones 5 y 6."""
    while True:
        try:
            if opcion == 5:
                exponente = es.tecladoFloat("Exponente de 2: ")
                resultado = potencia_dos(exponente)
                print(f"\n2 elevado a {exponente:g} = {resultado:g}\n")
            else:
                numero = es.tecladoFloat("Número positivo: ")
                resultado = logaritmo_base_dos(numero)
                print(f"\nLogaritmo en base 2 de {numero:g} = {resultado:g}\n")
        except ValueError as error:
            print(f"\nError: {error}\n")
        if not repetir_calculo():
            break


def ejecutar_conversion_bases():
    """Solicita los datos y permite repetir una conversión de base."""
    bases = {"2": "binario", "8": "octal", "10": "decimal", "16": "hexadecimal"}
    while True:
        numero = input("Número entero que deseas convertir: ").strip()
        origen = input("Base de origen (binario, octal, decimal, hexadecimal): ").strip().lower()
        destino = input("Base de destino (binario, octal, decimal, hexadecimal): ").strip().lower()
        origen = bases.get(origen, origen)
        destino = bases.get(destino, destino)
        try:
            resultado = convertir_base(numero, origen, destino)
            print(f"\nResultado: {resultado}\n")
        except ValueError as error:
            print(f"\nError: {error}\n")
        if not repetir_calculo():
            break


def ejecutar_conversion_unidades():
    """Solicita datos y permite repetir una conversión de unidades."""
    unidades = {"kib": "KiB", "mib": "MiB", "gib": "GiB"}
    while True:
        cantidad = es.tecladoFloat("Cantidad: ")
        origen = input("Unidad de origen (KiB, MiB, GiB): ").strip().lower()
        destino = input("Unidad de destino (KiB, MiB, GiB): ").strip().lower()
        origen = unidades.get(origen, origen)
        destino = unidades.get(destino, destino)
        try:
            resultado = convertir_unidades(cantidad, origen, destino)
            print(f"\nResultado: {resultado} {destino}\n")
        except ValueError as error:
            print(f"\nError: {error}\n")
        if not repetir_calculo():
            break


def iniciar_calculadora():
    """Inicia la aplicación y mantiene la navegación hasta que el usuario salga."""
    calculadora = CalculadoraAritmetica()
    mostrar_titulo("CALCULADORA MULTIFUNCIÓN")

    # El menú principal se repite hasta que se elige salir.
    while True:
        opcion = printMenu(menuGeneral, titulo="Menú principal")
        if opcion == 0:
            print("\n¡Hasta pronto!\n")
            break
        elif opcion == 1:
            # El submenú se repite hasta elegir 0, que devuelve al menú principal.
            while True:
                operacion = printMenu(
                    submenuAritmetica,
                    textoOpcionCero="Volver",
                    titulo="Operaciones aritméticas",
                )
                if operacion == 0:
                    break
                ejecutar_operacion(calculadora, operacion)
        elif opcion == 2:
            calcular_media_ponderada_interactiva()
        elif opcion == 3:
            ejecutar_conversion_bases()
        elif opcion == 4:
            ejecutar_conversion_unidades()
        elif opcion == 5 or opcion == 6:
            ejecutar_calculo_ingenieria(opcion)
        else:
            # Rama de seguridad: printMenu limita la selección al rango válido.
            print("\nFunción no válida\n")
