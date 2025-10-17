from datetime import date

def ingresar_fecha(mensaje):
    """
    Solicita y valida una fecha en formato dd/mm/yyyy.

    Args:
        mensaje (str): texto que se muestra al usuario.

    Returns:
        str: fecha validada en formato dd/mm/yyyy.
    """
    while True:
        fecha = input(mensaje).strip()
        partes = fecha.split("/")

        if len(partes) != 3:
            print("Formato inválido. Usa dd/mm/yyyy.")
            continue

        dia, mes, anio = partes
        if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
            print("La fecha debe tener solo números.")
            continue

        dia, mes, anio = int(dia), int(mes), int(anio)
        if anio < 1900 or anio > 2100:
            print("Año fuera de rango.")
            continue
        if mes < 1 or mes > 12:
            print("Mes inválido.")
            continue

        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias_por_mes[1] = 29

        if dia < 1 or dia > dias_por_mes[mes - 1]:
            print(f"El mes {mes} tiene máximo {dias_por_mes[mes - 1]} días.")
            continue

        try:
            ingresada = date(anio, mes, dia)
        except ValueError:
            print("Fecha inválida.")
            continue

        if ingresada > date.today():
            print("La fecha no puede ser futura.")
            continue

        return f"{dia:02d}/{mes:02d}/{anio}"
