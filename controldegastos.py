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

    if monto < 0:
      raise ValueError("Monto no válido")

    categoria = categoria.capitalize()
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

def buscar_por_id(id):
  """Devuelve un gasto por su índice"""
  try:
    if 0 <= id < len(gastos):
      return gastos[id]
    else:
      return False
  except IndexError as e:
    raise IndexError("ID fuera de rango")
  except ValueError:
    print(f"Error: Ingrese un valor válido.")
    return False

def buscar_gastos():
  if not gastos:
    print("No hay gastos todavía")
    return
  op = input("Buscar por (1) categoría, (2) fecha o (3) ID: ")
  if op == "1":
    cat = input("Categoría: ").strip().capitalize()
    filtrados = [g for g in gastos if g[2] == cat]
    for g in filtrados:
      print(f"${g[0]:.2f} | {g[1]} | {g[2]}")
  elif op == "2":
    f = input("Fecha (dd/mm/aaaa): ").strip()
    filtrados = [g for g in gastos if g[1] == f]
    for g in filtrados:
      print(f"${g[0]:.2f} | {g[1]} | {g[2]}")
  elif op == "3":
    id = int(input("Ingrese el ID del gasto: "))
    resultado = buscar_por_id(id)

    if resultado:
      print(f"{id}. {resultado[1]} - {resultado[2]}: ${resultado[0]:.2f}")
    else:
      print(f"No existe gasto con id {id}")


def top_gastos():
  """Devuelve los gastos ordenados por monto de mayor a menor"""
  try:
    if gastos:
      ordenados = sorted(gastos, key=lambda g: g[0], reverse=True)
      return ordenados
    else:
      print("No hay gastos registrados.")
      return
  except:
    print(f"Error al mostrar top de gastos.")


def eliminar_gasto(id):
  """Elimina un gasto por id"""
  try:
    eliminado = gastos.pop(id)
    print(f"Gasto eliminado: {eliminado}")
  except IndexError:
    print("Error: id no válido.")


def modificar_gasto(id, nuevo_monto=None, nueva_fecha=None, nueva_categoria=None):
  """Modifica un gasto existente"""
  try:
    if id < 0 or id >= len(gastos):
      raise IndexError("Índice fuera de rango.")

    if nuevo_monto:
      gastos[id][0] = float(nuevo_monto)
    if nueva_fecha:
      gastos[id][1] = nueva_fecha
    if nueva_categoria and nueva_categoria in categorias:
      gastos[id][2] = nueva_categoria

    print(f"Gasto modificado: {gastos[id]}")
  except ValueError:
    print("Error: monto inválido.")
  except IndexError as e:
    print(f"Error: {e}")

def generar_resumen_mensual(mes):
    """Genera un resumen de los gastos de un mes específico (mm/yyyy)"""

    resumen = [[cat, 0] for cat in categorias]
    total_general = 0

    for g in gastos:
        if g[1][3:] == mes:
            for fila in resumen:
                if fila[0] == g[2]:
                    fila[1] += g[0]
                    break
            total_general += g[0]

    print(f"\n Resumen de gastos - {mes}")
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
