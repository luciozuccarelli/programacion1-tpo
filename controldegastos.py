def registrar_gastos():
    gastos = []  #lista principal donde se van a guardar los gastos por fecha y categoria

    print("Categorias disponibles: Comida, Transporte, Servicios, Entretenimiento, Salud, Educación, Inversiones")

    while True:
        monto = float(input("Ingrese el monto del gasto en pesos: "))
        fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
        categoria = input("Ingrese la categoría: ")

        #los 3 datos los ingresamos en una lista
        gasto = [monto, fecha, categoria]

        #creo una lista de listas con los 3 datos anteriores
        gastos.append(gasto)

        seguir = input("¿Desea ingresar otro gasto? (si/no): ")
        if seguir.lower() != "si":
            break

    print(gastos)