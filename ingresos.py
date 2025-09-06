categorias_ingresos = ["Sueldo", "Ventas", "Inversiones", "Otros"]

# Datos iniciales
ingresos = [
  [150000.00, "01/08/2025", "Sueldo"],
  [20000.00, "05/08/2025", "Ventas"]
]


def registrar_ingreso(monto, fecha, categoria):
    try:
        monto = float(monto)
        if categoria not in categorias_ingresos:
            raise ValueError("Categoría no válida")
        ingreso = [monto, fecha, categoria]
        ingresos.append(ingreso)
        print(f"Ingreso registrado con éxito: {ingreso}")
    except ValueError as e:
        print(f"Error: {e}")

def mostrar_ingresos():
    if ingresos:
        print("\n📋 Lista de ingresos:")
        for i, ing in enumerate(ingresos):
            print(f"{i}. {ing[1]} - {ing[2]}: ${ing[0]:.2f}")
    else:
        print("Sin ingresos registrados al momento")


def buscar_por_fecha(fecha):
    return list(filter(lambda i: i[1] == fecha, ingresos))