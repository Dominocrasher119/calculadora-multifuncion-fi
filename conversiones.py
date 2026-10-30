"""Funciones para convertir bases numéricas y unidades informáticas."""

import math


_BASES = {
    "binario": 2,
    "octal": 8,
    "decimal": 10,
    "hexadecimal": 16,
}

_UNIDADES_KIB = {
    "KiB": 1,
    "MiB": 1024,
    "GiB": 1024 * 1024,
}


def convertir_base(numero, base_origen, base_destino):
    """Convierte un número entero entre binario, octal, decimal y hexadecimal.

    ``numero`` se recibe como texto para conservar dígitos como los ceros
    iniciales y las letras hexadecimales. Se admiten valores negativos.
    """
    origen = str(base_origen).strip().lower()
    destino = str(base_destino).strip().lower()
    if origen not in _BASES or destino not in _BASES:
        raise ValueError("La base debe ser binario, octal, decimal o hexadecimal.")

    texto = str(numero).strip()
    try:
        valor = int(texto, _BASES[origen])
    except (TypeError, ValueError):
        raise ValueError("El número no es válido para la base de origen.")

    if destino == "decimal":
        return valor
    return format(valor, {"binario": "b", "octal": "o", "hexadecimal": "X"}[destino])


def convertir_unidades(cantidad, origen, destino):
    """Convierte cantidades entre KiB, MiB y GiB usando múltiplos de 1024.

    Se admiten cantidades decimales y negativas. Los valores no finitos y las
    unidades no reconocidas producen un ``ValueError`` controlado.
    """
    if origen not in _UNIDADES_KIB or destino not in _UNIDADES_KIB:
        raise ValueError("La unidad debe ser KiB, MiB o GiB.")
    try:
        cantidad = float(cantidad)
    except (TypeError, ValueError):
        raise ValueError("La cantidad debe ser numérica.")
    if not math.isfinite(cantidad):
        raise ValueError("La cantidad debe ser un número finito.")

    resultado = cantidad * _UNIDADES_KIB[origen] / _UNIDADES_KIB[destino]
    if resultado.is_integer():
        return int(resultado)
    return resultado
