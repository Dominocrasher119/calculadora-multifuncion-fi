# Grupo: C12 - Calculadora Multifunción
# Asignatura: Fundamentos de Ingeniería
# Curso académico: 2026-2027
#
# Integrantes:
# Iker Sánchez Prieto
# Roger Pedra Vilalta
# Bernat Marín López
#
# Descripción:
# Calculadora multifunción en Python con operaciones
# aritméticas, media ponderada y funciones de
# utilidad para la ingeniería informática.

"""Punto de entrada de la Calculadora Multifunción."""

# El módulo menu reúne la navegación y llama a los cálculos.
from menu import iniciar_calculadora

# Solo inicia la interfaz al ejecutar este archivo, no al importarlo.
if __name__ == "__main__":
    iniciar_calculadora()
