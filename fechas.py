def ingresar_fecha(mensaje):
  """ Ingreso y validacion de fechas"""
  while True:
      fecha = input(mensaje)

      partes = fecha.split("/")
      if len(partes) != 3:
          print("Formato inválido. Usá dd/mm/yyyy (ej: 07/09/2025).")
          continue

      dia, mes, anio = partes

      # que sean números
      if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
          print("La fecha debe tener solo números.")
          continue

      dia, mes, anio = int(dia), int(mes), int(anio)

      # validamos año
      if anio < 1900 or anio > 2100:
          print("El año debe estar entre 1900 y 2100.")
          continue

      # validamos mes
      if mes < 1 or mes > 12:
          print("El mes debe estar entre 1 y 12.")
          continue

      # días por mes
      dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

      # si es año bisiesto, febrero tiene 29
      if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
          dias_por_mes[1] = 29

      # validamos día
      if dia < 1 or dia > dias_por_mes[mes - 1]:
          print(f"El mes {mes} tiene como máximo {dias_por_mes[mes - 1]} días.")
          continue

      # si todo está bien devolvemos la fecha en formato correcto
      return f"{dia}/{mes}/{anio}"