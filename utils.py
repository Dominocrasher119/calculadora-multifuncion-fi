# Grupo: B - Calculadora Multifunción
# Integrantes: Iker Sánchez Prieto, Roger Pedra Vilalta y Bernat Marín López

import math


class EntradaSalida:
    """Lee y valida entradas sin guardar estado ni requerir una instancia.

    Los métodos estáticos se llaman directamente desde otros módulos.
    """

    @staticmethod
    def tecladoInt(mensaje="Ingrese un número entero: "):
        """Lee un entero; repite la pregunta hasta recibir una entrada válida."""
        while True:
            # int convierte el texto; si no es un entero, se vuelve a preguntar.
            try:
                return int(input(mensaje))
            except ValueError:
                # Capturar el error evita cerrar el programa por una entrada incorrecta.
                print("Entrada inválida. Escribe un número entero.")

    @staticmethod
    def tecladoFloat(mensaje="Ingrese un número (puede usar coma o punto decimal): "):
        """Lee un número finito y acepta coma o punto como separador decimal."""
        while True:
            texto = input(mensaje).strip()
            try:
                # float() entiende el punto; se convierte la coma antes de validar.
                numero = float(texto.replace(",", "."))
                if math.isfinite(numero):
                    return numero
                print("Entrada inválida. El número debe ser finito.")
            except ValueError:
                print("Número incompleto o inválido. Ejemplos: 12, 3.5 o 3,5.")

    @staticmethod
    def tecladoString():
        """Lee una cadena que no esté vacía ni contenga solo espacios."""
        while True:
            texto = input("Ingrese un texto: ").strip()
            if texto:
                return texto
            print("El texto no puede estar vacío.")

    @staticmethod
    def tecladoChar():
        """Lee exactamente un carácter, ignorando espacios exteriores."""
        while True:
            texto = input("Ingrese un carácter: ").strip()
            if len(texto) == 1:
                return texto
            print("Debe ingresar un solo carácter.")
