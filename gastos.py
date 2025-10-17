CATEGORIAS_GASTOS = [
    "Comida", "Transporte", "Servicios", "Entretenimiento",
    "Salud", "Educación", "Inversiones"
]


def registrar_gasto(gastos, monto, fecha, categoria):
    """
    Registra un nuevo gasto en la lista.

    Args:
        gastos (list): lista actual de gastos.
        monto (float): monto del gasto.
        fecha (str): fecha del gasto.
        categoria (str): categoría del gasto.

    Returns:
        list: lista actualizada de gastos.
    """
    categoria = categoria.capitalize()
    if categoria not in CATEGORIAS_GASTOS:
        raise ValueError("Categoría no válida.")

    gasto = [monto, fecha, categoria]
    gastos.append(gasto)
    return gastos


def mostrar_gastos(gastos):
    """Imprime los gastos en formato legible."""
    if not gastos:
        print("No hay gastos registrados.")
        return
    print("\nLista de gastos:")
    for i, g in enumerate(gastos):
        print(f"{i}. {g[1]} - {g[2]}: ${g[0]:.2f}")


def eliminar_gasto(gastos, idx):
    """Elimina un gasto por índice."""
    try:
        eliminado = gastos.pop(idx)
        print(f"Gasto eliminado: {eliminado}")
    except IndexError:
        print("ID no válido.")
    return gastos


def resumen_mensual(gastos, mes):
    """
    Muestra un resumen mensual de gastos por categoría.

    Args:
        gastos (list): lista de gastos.
        mes (str): mes a consultar (mm/yyyy).
    """
    resumen = {cat: 0 for cat in CATEGORIAS_GASTOS}
    total = 0
    for monto, fecha, categoria in gastos:
        if fecha[3:] == mes:
            resumen[categoria] += monto
            total += monto

    print(f"\nResumen de gastos - {mes}")
    print("-" * 35)
    for cat, monto in resumen.items():
        if monto > 0:
            print(f"{cat:<20} ${monto:>10.2f}")
    print("-" * 35)
    print(f"{'TOTAL':<20} ${total:>10.2f}")