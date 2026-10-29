"""Funciones de cálculo de ingeniería"""

import math


def potencia_dos(exponente):
    """Devuelve 2 elevado a ``exponente``, también para exponentes negativos."""
    try:
        exponente = float(exponente)
    except (TypeError, ValueError):
        raise ValueError("El exponente debe ser un número válido.")
    if not math.isfinite(exponente):
        raise ValueError("El exponente debe ser un número finito.")
    try:
        return 2 ** exponente
    except OverflowError:
        raise ValueError("El resultado es demasiado grande para representarlo.")


def logaritmo_base_dos(numero):
    """Devuelve el logaritmo en base 2 de un número positivo y finito."""
    try:
        numero = float(numero)
    except (TypeError, ValueError):
        raise ValueError("El número debe ser válido.")
    if not math.isfinite(numero) or numero <= 0:
        raise ValueError("El número debe ser positivo y finito.")
    # math.log2 no depende del intervalo arbitrario [-100, 100] de la búsqueda
    # binaria original y mantiene precisión para valores muy grandes o pequeños.
    return math.log2(numero)
