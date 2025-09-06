# Control de gastos
categorias = ["Comida", "Transporte", "Servicios", "Entretenimiento", "Salud", "Educación", "Inversiones"]
gastos = []  #lista principal donde se van a guardar los gastos por fecha y categoria

# Datos iniciales
gastos.extend([
  [28500.00, "12/08/2025", "Entretenimiento"],
  [8800.00, "15/08/2025", "Comida"],
  [26000.00, "15/08/2025", "Comida"],
  [15000.00, "01/09/2025", "Servicios"],
  [230000.00, "01/09/2025", "Educación"]
  ])

def registrar_gasto(monto, fecha, categoria):
  """ Registra un gasto en la lista de gastos"""
  
  try:
    monto = float(monto)

    if categoria not in categorias:
      raise ValueError("Categoría no válida")

    #los 3 datos los ingresamos en una lista
    gasto = [monto, fecha, categoria]

    #creo una lista de listas con los 3 datos anteriores
    gastos.append(gasto)

    print(f"Gasto registrado con éxito: {gasto[0]}, {gasto[1]}, {gasto[2]}")

  except ValueError as e:
    print(f"Error: {e}")

def mostrar_gastos():
  """Muestra todos los gastos registrados"""
  if len(gastos) != 0:
    print("Lista de gastos:")

    for i in range(len(gastos)):
      print(f"{i}. {gastos[i][1]} - {gastos[i][2]}: ${gastos[i][0]:.2f}")
  else:
    print("Sin gastos registrados al momento")

def buscar_por_fecha(fecha):
    """Devuelve los gastos de una fecha específica"""
    encontrados = list(filter(lambda g: g[1] == fecha, gastos))
    return encontrados
def buscar_por_id(id):
    """Devuelve un gasto"""
    return gastos[id]