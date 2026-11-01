# Grupo: C12 - Calculadora Multifunción
# Integrantes: Iker Sánchez Prieto, Roger Pedra Vilalta y Bernat Marín López

# Archivo Python para implementar operaciones aritméticas básicas.


class CalculadoraAritmetica:
    """Opera con dos valores numéricos, a y b, y devuelve el resultado.

    En la resta y la división importa el orden de los valores.
    """

    def suma(self, a, b):
        """Devuelve la suma de a y b."""
        return a + b

    def resta(self, a, b):
        """Devuelve la resta de b a a."""
        return a - b

    def multiplicacion(self, a, b):
        """Devuelve el producto de a y b."""
        return a * b

    def division(self, a, b):
        """Devuelve a dividido entre b; lanza ValueError si b es cero."""
        # La división entre cero no está definida; el menú captura el error.
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b
