import controldegastos

def opciones():
  opciones = ["Registrar Gasto", "Salir"]
  
  for i in range(len(opciones)):
    print(f"{i} - {opciones[i]}")
  
  opcion = int(input("Seleccione una opción: "))
  
  match opcion:
    case 0:
      controldegastos.registrar_gastos()
    case 1:
      return False
    