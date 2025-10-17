import os


def cargar_datos(nombre_archivo):
    """
    Carga datos desde un archivo de texto.
    Cada línea debe tener: monto,fecha,categoria
    """
    datos = []
    if not os.path.exists(nombre_archivo):
        return datos

    with open(nombre_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            try:
                monto, fecha, categoria = linea.strip().split(",")
                datos.append([float(monto), fecha, categoria])
            except ValueError:
                continue
    return datos


def guardar_datos(nombre_archivo, datos):
    """Guarda datos en un archivo de texto plano."""
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for monto, fecha, categoria in datos:
            f.write(f"{monto},{fecha},{categoria}\n")


def registrar_evento(mensaje):
    """Agrega un evento o error al archivo de log."""
    with open("log.txt", "a", encoding="utf-8") as log:
        log.write(mensaje + "\n")