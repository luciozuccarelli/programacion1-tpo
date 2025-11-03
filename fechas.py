from datetime import date

def ingresar_valor(mensaje, minimo=None, maximo=None):
    """
    Pide un entero con un mensaje y valida rango si corresponde.
    Devuelve el entero válido.
    """
    while True:
        s = input(mensaje).strip()
        if not s.isdigit():
            print("Debe ingresar solo números.")
            continue
        n = int(s)
        if minimo is not None and n < minimo:
            print(f"El valor no puede ser menor que {minimo}.")
            continue
        if maximo is not None and n > maximo:
            print(f"El valor no puede ser mayor que {maximo}.")
            continue
        return n


def ingresar_fecha():
    """
    Solicita y valida una fecha pidiendo día, mes y año por separado.
    Devuelve la fecha en formato dd/mm/yyyy.
    """
    while True:
        # pedir fechas con topes genericos
        dia = ingresar_valor("Ingrese el dia: ", 1, 31)
        mes = ingresar_valor("Ingrese el mes: ", 1, 12)
        anio = ingresar_valor("Ingrese el anio: ", 1900, 2100)

        # esto considera los años bisiestos
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias_por_mes[1] = 29

        max_dia = dias_por_mes[mes - 1]
        if dia > max_dia:
            print(f"El mes {mes} tiene máximo {max_dia} días. Reingrese el día.")
            # vuelve a pedir solo el día con el tope correcto
            dia = ingresar_valor(f"Ingrese el dia (1-{max_dia}): ", 1, max_dia)

        # valida que no se ingresen fechas futuras
        try:
            ingresada = date(anio, mes, dia)
        except ValueError:
            print("Fecha inválida. Ingrese una fecha válida.\n")
            continue

        if ingresada > date.today():
            print("La fecha no puede ser futura. Ingrese una fecha válida.\n")
            continue

        return f"{dia:02d}/{mes:02d}/{anio}"


def ingresar_periodo():
    """
    Solicita y valida un período pidiendo mes y año por separado.
    Devuelve el período en formato mm/yyyy.
    """
    while True:
        mes = ingresar_valor("Ingrese el mes: ", 1, 12)
        anio = ingresar_valor("Ingrese el anio: ", 1900, 2100)
        return f"{mes:02d}/{anio}"
