import math

def validar_monto(mensaje, minimo=None, maximo=None):
    """
    Pide un número (int o float), admite '.' o ',' como separador decimal
    y valida rango si corresponde. Devuelve el valor como float.
    """
    while True:
        s = input(mensaje).strip()
        try:
            n = float(s)
        except ValueError:
            print("Debe ingresar un número válido (ej: 123, 45.67).")
            continue
        if not math.isfinite(n):
            print("El número ingresado no es válido.")
            continue
        if minimo is not None and n < minimo:
            print(f"El valor no puede ser menor que {minimo}.")
            continue
        if maximo is not None and n > maximo:
            print(f"El valor no puede ser mayor que {maximo}.")
            continue

        return n
