import controldegastos

def seleccionar_opcion():

  
  opciones = [
      "Registrar gasto",
      "Mostrar gastos",
      "Buscar gastos por fecha",
      "Buscar gasto por ID",
      "Top de gastos",
      "Eliminar gasto",
      "Modificar gasto",
      "Registrar ingreso",
      "Mostrar ingresos",
      "Buscar ingresos por fecha",
      "Salir"
  ]

  while True:
    for i in range(len(opciones)):
      print(f"{i} - {opciones[i]}")
    
    opcion = int(input("Seleccione una opción: "))
    
    match opcion:
      case 0:
        while True:
          monto = float(input("Ingrese el monto del gasto: "))
          fecha = input("Ingrese la fecha (dd/mm/aaaa): ")

          print("Categorias disponibles: ", controldegastos.categorias)
          categoria = input("Ingrese la categoría: ")

          controldegastos.registrar_gasto(monto, fecha, categoria)

          seguir = input("¿Desea ingresar otro gasto? (si/no): ")
          if seguir.lower() != "si":
            break
      case 1:
        #Lista de gastos
        controldegastos.mostrar_gastos()
      case 2:
        #Buscar gastos por fecha
        fecha = input("Ingrese la fecha a buscar (dd/mm/yyyy): ")
        resultados = controldegastos.buscar_por_fecha(fecha)

        if resultados:
          print(f"\n Gastos del {fecha}:")
          for g in resultados:
            print(f"- {g[2]}: ${g[0]:.2f}")
      case 3:
        #Buscar gastos por ID
        id = int(input("Ingrese el ID del gasto: "))
        resultado = controldegastos.buscar_por_id(id)
        print(f"{id}. {resultado[1]} - {resultado[2]}: ${resultado[0]:.2f}")
      case 4:
        # n = int(input("¿Cuántos gastos quiere ver en el top? "))
        # top = controldegastos.top_gastos(n)
        # print("\nTop de gastos:")
        # for g in top:
        #   print(f"- {g[2]}: ${g[0]:.2f} ({g[1]})")
        pass
      case 5:
        controldegastos.mostrar_gastos
        gasto_id = int(input("Ingrese el ID del gasto a eliminar: "))
        #controldegastos.eliminar_gasto(gasto_id)
      case 6:
        gasto_id = int(input("Ingrese el ID del gasto a modificar: "))
        nuevo_monto = float(input("Nuevo monto: "))
        nueva_fecha = input("Nueva fecha (dd/mm/yyyy): ")
        nueva_categoria = input("Nueva categoría: ")
        controldegastos.modificar_gasto(gasto_id, nuevo_monto, nueva_fecha, nueva_categoria)

      ## FALTA LLAMADO A INGRESOS

      case 10:
        print("Saliendo del sistema...")
        break
      case _:
        print("Opcion no valida, elija nuevamente")
    