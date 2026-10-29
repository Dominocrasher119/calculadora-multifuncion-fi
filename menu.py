from utils import EntradaSalida as es
from operaciones import CalculadoraAritmetica
from notas import calcular_media_ponderada_interactiva

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
        calculadora: Instancia de CalculadoraAritmetica. que realiza el cálculo.
        opcion: Número de la operación seleccionada en el submenú.
    """
    nombre = submenuAritmetica[opcion - 1].lower()
    mostrar_titulo(nombre.capitalize())

    while True:
        numero1 = es.tecladoFloat("  Primer número: ")
        numero2 = es.tecladoFloat("  Segundo número: ")

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
            # Calculadora.division avisa con ValueError si el divisor es cero.
            print(f"\n  Error: {error}\n")

        repetir = input("¿Quieres hacer otra operación del mismo tipo? (s/n): ").strip().lower()
        while repetir not in ("s", "si", "sí", "n", "no"):
            repetir = input("Responde s o n: ").strip().lower()
        if repetir in ("n", "no"):
            print()
            break
        print(f"\n¡Seguimos con la {nombre}!\n")


def iniciar_calculadora():
    """Inicia la aplicación y mantiene la navegación hasta que el usuario salga."""
    calculadora = CalculadoraAritmetica()
    mostrar_titulo("CALCULADORA MULTIFUNCIÓN")

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
        else:
            # Las opciones restantes están reservadas para el resto del equipo.
            print("\nFunción todavía no implementada.\n")
