categorias = ["Sueldo", "Ventas", "Inversiones", "Otros"]

# Datos iniciales
ingresos = [
  [150000.00, "01/08/2025", "Sueldo"],
  [20000.00, "05/08/2025", "Ventas"]
]


def registrar_ingreso(monto, fecha, categoria):
    try:
        monto = float(monto)
        
        categoria = categoria.capitalize()
        if categoria not in categorias:
            raise ValueError("Categoría no válida")
    
        ingreso = [monto, fecha, categoria]
        ingresos.append(ingreso)
        print(f"Ingreso registrado con éxito: {ingreso}")
    except ValueError:
        print(f"Error: El valor ingresado no es válido")

def mostrar_ingresos():
    if ingresos:
        print("Lista de ingresos:")
        for i, ing in enumerate(ingresos):
            print(f"{i}. {ing[1]} - {ing[2]}: ${ing[0]:.2f}")
    else:
        print("Sin ingresos registrados al momento")


def buscar_por_fecha(fecha):
    return list(filter(lambda i: i[1] == fecha, ingresos))

def generar_resumen_mensual(mes):
    """Genera un resumen de los ingresos de un mes específico (mm/yyyy)"""

    resumen = [[cat, 0] for cat in categorias]
    total_general = 0

    for i in ingresos:
        if i[1][3:] == mes:
            for fila in resumen:
                if fila[0] == i[2]:
                    fila[1] += i[0]
                    break
            total_general += i[0]

    print(f"\n Resumen de ingresos - {mes}")
    print("-" *40)
    print(f"{'Categoría':<20} | {'Monto ($)':>10}")
    print("-" *40)

    for fila in resumen:
        if fila[1] > 0:
            print(f"{fila[0]:<20} | {fila[1]:>10.2f}")

    print("-" *40)
    print(f"{'TOTAL':<20} | {total_general:>10.2f}")
    print("-" *40)

    return resumen, total_general