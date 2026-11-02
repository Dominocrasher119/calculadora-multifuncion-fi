# Grupo: B - Calculadora Multifunción
# Integrantes: Iker Sánchez Prieto, Roger Pedra Vilalta y Bernat Marín López

"""Cálculo interactivo de la media ponderada de varias notas."""

import math

from utils import EntradaSalida as es


def calcular_media_ponderada(notas, pesos):
    """Devuelve la media ponderada tras validar notas y pesos.

    Cada nota se empareja con el peso de la misma posición, que indica su
    importancia en la media. Las notas deben estar entre 0 y 10. Los pesos deben ser
    no negativos y su suma debe ser mayor que cero.

    Raises:
        ValueError: Si las listas están vacías, no tienen igual longitud o
            contienen valores no válidos.
    """
    if not notas or not pesos:
        raise ValueError("Debe proporcionarse al menos una nota y su peso.")
    if len(notas) != len(pesos):
        raise ValueError("Debe haber el mismo número de notas y pesos.")

    suma_ponderada = 0
    suma_pesos = 0

    # Se recorre cada pareja y se acumulan nota por peso y suma de pesos.
    for nota, peso in zip(notas, pesos):
        try:
            nota = float(nota)
            peso = float(peso)
        except (TypeError, ValueError):
            raise ValueError("Las notas y los pesos deben ser números válidos.")

        if not math.isfinite(nota) or nota < 0 or nota > 10:
            raise ValueError("Cada nota debe ser un número entre 0 y 10.")
        if not math.isfinite(peso) or peso < 0:
            raise ValueError("Cada peso debe ser un número no negativo.")

        suma_ponderada += nota * peso
        suma_pesos += peso

    # El total debe ser positivo para poder dividir y obtener la media.
    if suma_pesos == 0:
        raise ValueError("La suma de los pesos debe ser mayor que cero.")

    return suma_ponderada / suma_pesos


def calcular_media_ponderada_interactiva():
    """Lee varias notas y sus pesos, muestra el resultado y permite repetir."""
    while True:
        cantidad = es.tecladoInt("¿Cuántas notas quieres introducir?: ")
        while cantidad <= 0:
            print("Debes introducir al menos una nota.")
            cantidad = es.tecladoInt("¿Cuántas notas quieres introducir?: ")

        notas = []
        pesos = []

        # Se repite la lectura de cada pareja para asegurar que cumple los rangos.
        for numero in range(1, cantidad + 1):
            nota = es.tecladoFloat(f"Nota {numero} (0-10): ")
            while nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10.")
                nota = es.tecladoFloat(f"Nota {numero} (0-10): ")

            peso = es.tecladoFloat(f"Peso de la nota {numero}: ")
            while peso < 0:
                print("El peso no puede ser negativo.")
                peso = es.tecladoFloat(f"Peso de la nota {numero}: ")

            notas.append(nota)
            pesos.append(peso)

        try:
            resultado = calcular_media_ponderada(notas, pesos)
            print(f"\nLa nota media ponderada es: {resultado:.2f}\n")
        except ValueError as error:
            # Por ejemplo, si todos los pesos son cero, se informa y se continúa.
            print(f"\nNo se pudo calcular la media: {error}\n")

        repetir = input("¿Quieres calcular otra media ponderada? (s/n): ").strip().lower()
        while repetir not in ("s", "si", "sí", "n", "no"):
            repetir = input("Responde s o n: ").strip().lower()
        if repetir in ("n", "no"):
            break
