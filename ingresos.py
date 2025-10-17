CATEGORIAS_INGRESOS = ["Sueldo", "Ventas", "Inversiones", "Otros"]


def mostrar_menu_categorias_ingreso():
    """Imprime el menú numerado de categorías de ingreso."""
    print("\nSeleccione una categoría de ingreso:")
    for i, cat in enumerate(CATEGORIAS_INGRESOS, start=1):
        print(f"{i}. {cat}")


def seleccionar_categoria_ingreso():
    """Devuelve una categoría válida elegida por el usuario mediante un menú."""
    while True:
        mostrar_menu_categorias_ingreso()
        opcion = input(f"Opción (1-{len(CATEGORIAS_INGRESOS)}): ").strip()

        if opcion.isdigit():
            idx = int(opcion)
            if 1 <= idx <= len(CATEGORIAS_INGRESOS):
                return CATEGORIAS_INGRESOS[idx - 1]

        print("Opción inválida. Intente nuevamente.\n")


def registrar_ingreso(ingresos, monto, fecha, categoria):
    """
    Registra un nuevo ingreso.

    Args:
        ingresos (list): lista de ingresos actual.
        monto (float): monto del ingreso.
        fecha (str): fecha.
        categoria (str): tipo de ingreso.
    """
    categoria = categoria.capitalize()
    if categoria not in CATEGORIAS_INGRESOS:
        raise ValueError("Categoría no válida.")

    ingreso = [monto, fecha, categoria]
    ingresos.append(ingreso)
    return ingresos


def mostrar_ingresos(ingresos):
    """Imprime los ingresos actuales."""
    if not ingresos:
        print("No hay ingresos registrados.")
        return
    print("\nLista de ingresos:")
    for i, ing in enumerate(ingresos):
        print(f"{i}. {ing[1]} - {ing[2]}: ${ing[0]:.2f}")


def resumen_mensual(ingresos, mes):
    """Muestra resumen mensual de ingresos."""
    resumen = {cat: 0 for cat in CATEGORIAS_INGRESOS}
    total = 0
    for monto, fecha, categoria in ingresos:
        if fecha[3:] == mes:
            resumen[categoria] += monto
            total += monto

    print(f"\nResumen de ingresos - {mes}")
    print("-" * 35)
    for cat, monto in resumen.items():
        if monto > 0:
            print(f"{cat:<20} ${monto:>10.2f}")
    print("-" * 35)
    print(f"{'TOTAL':<20} ${total:>10.2f}")
