import controldegastos
import ingresos
import fechas

def imprimir_menu():
  opciones = [
      "Salir",                                # 0
      "Registrar gasto",                      # 1
      "Mostrar todos los gastos",             # 2
      "Buscar gastos",                        # 3
      "Top de gastos",                        # 4
      "Eliminar gasto",                       # 5
      "Modificar gasto",                      # 6
      "Registrar ingreso",                    # 7
      "Mostrar ingresos",                     # 8
      "Buscar ingresos por fecha",            # 9
      "Mostrar resumen mensual de gastos",    # 10
      "Mostrar resumen mensual de ingresos"   # 11
  ]

  for i in range(1, len(opciones)):
    print(f"{i} - {opciones[i]}")
  print(f"0 - {opciones[0]}")

def seleccionar_opcion():

  while True:
    try: 
      imprimir_menu()
      opcion = int(input("Seleccione una opción: "))
      
      match opcion:
        case 1:
        # REGISTRAR GASTO
          while True:
            try:
              monto = float(input("Ingrese el monto del gasto: "))
              if monto < 0:
                print("Monto no válido")
                break
              
              fecha = fechas.ingresar_fecha("Ingrese la fecha (dd/mm/yyyy):")

              print("Categorias disponibles: ", controldegastos.categorias)
              categoria = input("Ingrese la categoría: ")

              controldegastos.registrar_gasto(monto, fecha, categoria)

              seguir = input("¿Desea registrar otro gasto? (si/no): ")
              if seguir.lower() != "si":
                break
            except:
              print("Valor ingresado no válido")
        case 2:
        # MOSTRAR LISTA DE GASTOS
          controldegastos.mostrar_gastos()

        case 3:
        # MOSTRAR LISTA DE GASTOS
          controldegastos.buscar_gastos()

        case 4:
        # TOP GASTOS
          n = int(input("¿Cuántos gastos quiere ver en el top? "))
          if(n > 0):
            ordenados = controldegastos.top_gastos()

            print(f"\nTop {n} gastos más altos:")
            for i, g in enumerate(ordenados[:n], 1):
              print(f"{i}. {g[1]} - {g[2]}: ${g[0]:.2f}")
          else:
            print("El numero ingresado no es válido.")

        case 5:
        # ELIMINAR UN GASTO POR ID
          controldegastos.mostrar_gastos()

          gasto_id = int(input("Ingrese el ID del gasto a eliminar: "))
          controldegastos.eliminar_gasto(gasto_id)

        case 6:
        # MODIFICAR GASTO
          controldegastos.mostrar_gastos()

          gasto_id = int(input("Ingrese el ID del gasto a modificar: "))
          nuevo_monto = float(input("Nuevo monto: "))
          nueva_fecha = input("Nueva fecha (dd/mm/yyyy): ")
          nueva_categoria = input("Nueva categoría: ")
          controldegastos.modificar_gasto(gasto_id, nuevo_monto, nueva_fecha, nueva_categoria)

        case 7:
        # REGISTRAR INGRESO
          while True:
            try:
              monto = float(input("Ingrese el monto del ingreso: "))
              fecha = fechas.ingresar_fecha("Ingrese la fecha (dd/mm/yyyy): ")

              print("Categorias disponibles: ", ingresos.categorias)
              categoria = input("Ingrese la categoría: ")

              ingresos.registrar_ingreso(monto, fecha, categoria)

              seguir = input("¿Desea registrar otro ingreso? (si/no): ")
              if seguir.lower() != "si":
                break
            except ValueError:
              print("Valor ingresado no válido.")

        case 8:
        # MOSTRAR LISTA DE INGRESOS
          ingresos.mostrar_ingresos()

        case 9:
        # BUSCAR INGRESOS POR FECHA
          fecha = input("Ingrese la fecha a buscar (dd/mm/yyyy): ")
          resultados = ingresos.buscar_por_fecha(fecha)

          if resultados:
            print(f"\n Ingresos del {fecha}:")
            for i in resultados:
              print(f"- {i[2]}: ${i[0]:.2f}")

        case 10:
        # MOSTRAR RESUMEN MENSUAL DE GASTOS
          mes = input("Ingrese el mes (mm/yyyy): ")
          controldegastos.generar_resumen_mensual(mes)

        case 11:
        # MOSTRAR RESUMEN MENSUAL DE INGRESOS
          mes = input("Ingrese el mes (mm/yyyy): ")
          ingresos.generar_resumen_mensual(mes)

        case 0:
        # SALIR
          print("Saliendo del sistema...")
          break

        case 99:
          imprimir_menu()

        case _:
          print("Opcion no valida, ingrese nuevamente")

    except ValueError:
      print(f"Error: Valor ingresado no valido.")