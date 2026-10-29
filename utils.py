import math


class EntradaSalida:
    """Métodos estáticos para leer y validar datos introducidos por teclado."""

    @staticmethod
    def tecladoInt(mensaje="Ingrese un número entero: "):
        """Lee un entero; repite la pregunta hasta recibir una entrada válida."""
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
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
