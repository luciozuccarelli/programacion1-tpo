"""Módulo principal del sistema de control de gastos e ingresos.

Carga los datos iniciales desde archivos de texto y muestra el menú principal.
"""

from persistencia import cargar_datos
from menu import menu_principal


def main():
    """Punto de entrada del programa.

    Carga listas de gastos e ingresos desde archivos y delega el flujo
    al menú principal del sistema.
    """
    try:
        gastos = cargar_datos("gastos.txt")
        ingresos = cargar_datos("ingresos.txt")

        print("SISTEMA DE CONTROL DE GASTOS E INGRESOS")
        menu_principal(gastos, ingresos)
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario. Saliendo...")


if __name__ == "__main__":
    main()
