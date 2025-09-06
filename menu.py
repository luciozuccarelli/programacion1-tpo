import controldegastos
import ingresos

def seleccionar_opcion():
 
  opciones = [
      "Salir",                                # 0
      "Registrar gasto",                      # 1
      "Mostrar gastos",                       # 2
      "Buscar gastos por fecha",              # 3
      "Buscar gasto por ID",                  # 4
      "Top de gastos",                        # 5
      "Eliminar gasto",                       # 6
      "Modificar gasto",                      # 7
      "Registrar ingreso",                    # 8
      "Mostrar ingresos",                     # 9
      "Buscar ingresos por fecha",            # 10
      "Mostrar resumen mensual de gastos",    # 11
      "Mostrar resumen mensual de ingresos"   # 12
  ]

  for i in range(1, len(opciones)):
    print(f"{i} - {opciones[i]}")
  print(f"0 - {opciones[0]}")

  while True:
    try: 
    
      opcion = int(input("Seleccione una opción: "))
      
      match opcion:
        case 1:
        # REGISTRAR GASTO
          while True:
            try:
              monto = float(input("Ingrese el monto del gasto: "))
              fecha = input("Ingrese la fecha (dd/mm/yyyy): ")

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
        # BUSCAR GASTO POR FECHA
          fecha = input("Ingrese la fecha a buscar (dd/mm/yyyy): ")
          resultados = controldegastos.buscar_por_fecha(fecha)

          if resultados:
            print(f"\n Gastos del {fecha}:")
            for g in resultados:
              print(f"- {g[2]}: ${g[0]:.2f}")
          else:
            print("No existen gastos para la fecha ingresada.")

        case 4:
        # BUSCAR GASTO POR ID
          id = int(input("Ingrese el ID del gasto: "))
          resultado = controldegastos.buscar_por_id(id)

          if resultado:
            print(f"{id}. {resultado[1]} - {resultado[2]}: ${resultado[0]:.2f}")
          else:
            print(f"No existe gasto con id {id}")

        case 5:
        # TOP GASTOS
          n = int(input("¿Cuántos gastos quiere ver en el top? "))
          if(n > 0):
            ordenados = controldegastos.top_gastos()

            print(f"\nTop {n} gastos más altos:")
            for i, g in enumerate(ordenados[:n], 1):
              print(f"{i}. {g[1]} - {g[2]}: ${g[0]:.2f}")
          else:
            print("El numero ingresado no es válido.")

        case 6:
        # ELIMINAR UN GASTO POR ID
          controldegastos.mostrar_gastos()

          gasto_id = int(input("Ingrese el ID del gasto a eliminar: "))
          controldegastos.eliminar_gasto(gasto_id)

        case 7:
        # MODIFICAR GASTO
          controldegastos.mostrar_gastos()

          gasto_id = int(input("Ingrese el ID del gasto a modificar: "))
          nuevo_monto = float(input("Nuevo monto: "))
          nueva_fecha = input("Nueva fecha (dd/mm/yyyy): ")
          nueva_categoria = input("Nueva categoría: ")
          controldegastos.modificar_gasto(gasto_id, nuevo_monto, nueva_fecha, nueva_categoria)

        case 8:
        # REGISTRAR INGRESO
          while True:
            try:
              monto = float(input("Ingrese el monto del ingreso: "))
              fecha = input("Ingrese la fecha (dd/mm/yyyy): ")

              print("Categorias disponibles: ", ingresos.categorias)
              categoria = input("Ingrese la categoría: ")

              ingresos.registrar_ingreso(monto, fecha, categoria)

              seguir = input("¿Desea registrar otro ingreso? (si/no): ")
              if seguir.lower() != "si":
                break
            except ValueError:
              print("Valor ingresado no válido.")

        case 9:
        # MOSTRAR LISTA DE INGRESOS
          ingresos.mostrar_ingresos()

        case 10:
        # BUSCAR INGRESOS POR FECHA
          fecha = input("Ingrese la fecha a buscar (dd/mm/yyyy): ")
          resultados = ingresos.buscar_por_fecha(fecha)

          if resultados:
            print(f"\n Ingresos del {fecha}:")
            for i in resultados:
              print(f"- {i[2]}: ${i[0]:.2f}")

        case 11:
        # MOSTRAR RESUMEN MENSUAL DE GASTOS
          mes = input("Ingrese el mes (mm/yyyy): ")
          controldegastos.generar_resumen_mensual(mes)

        case 12:
        # MOSTRAR RESUMEN MENSUAL DE GASTOS
          mes = input("Ingrese el mes (mm/yyyy): ")
          ingresos.generar_resumen_mensual(mes)

        case 0:
        # SALIR
          print("Saliendo del sistema...")
          break

        case _:
          print("Opcion no valida, ingrese nuevamente")

    except ValueError:
      print(f"Error: Valor ingresado no valido.")