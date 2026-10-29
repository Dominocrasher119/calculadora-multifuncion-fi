# Archivo Python para implementar operaciones aritméticas básicas.


class CalculadoraAritmetica:
    """Realiza operaciones aritméticas con los valores que recibe."""

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
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b
