# Grupo: B - Calculadora Multifunción
# Integrantes: Iker Sánchez Prieto, Roger Pedra Vilalta y Bernat Marín López

"""Funciones de cálculo de ingeniería"""

import math


def potencia_dos(exponente):
    """Devuelve 2 elevado a exponente, incluso si es decimal o negativo.

    Valida que sea finito y controla el desbordamiento; ** calcula la potencia.
    """
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
    """Devuelve el exponente al que elevar 2 para obtener numero.

    Valida que el número sea positivo y finito y utiliza math.log2.
    """
    try:
        numero = float(numero)
    except (TypeError, ValueError):
        raise ValueError("El número debe ser válido.")
    if not math.isfinite(numero) or numero <= 0:
        raise ValueError("El número debe ser positivo y finito.")
    # math.log2 no depende del intervalo arbitrario [-100, 100] de la búsqueda
    # binaria original y mantiene precisión para valores muy grandes o pequeños.
    return math.log2(numero)
