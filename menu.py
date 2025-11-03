from fechas import (ingresar_fecha, ingresar_periodo)
from gastos import (
    registrar_gasto, mostrar_gastos, eliminar_gasto, resumen_mensual, CATEGORIAS_GASTOS
)
from ingresos import (
    registrar_ingreso, mostrar_ingresos, resumen_mensual as resumen_ingresos,
    CATEGORIAS_INGRESOS
)
from persistencia import guardar_datos, registrar_evento


def _mostrar_menu(opciones, titulo):
    """Imprime un menú numerado simple."""
    print(f"\n{titulo}:")
    for i, texto in enumerate(opciones, start=1):
        print(f"{i}. {texto}")


def _elegir_de_menu(opciones, etiqueta="Opción"):
    """Pide una opción hasta que sea válida y devuelve el texto elegido."""
    while True:
        _mostrar_menu(opciones, "Seleccione una opción")
        entrada = input(f"{etiqueta} (1-{len(opciones)}): ").strip()
        if entrada.isdigit():
            n = int(entrada)
            if 1 <= n <= len(opciones):
                return opciones[n - 1]
        print("Opción inválida. Intente nuevamente.\n")


def menu_principal(gastos, ingresos):
    while True:
        print("\n=== SISTEMA DE GESTIÓN FINANCIERA ===")
        print("1 - Registrar gasto")
        print("2 - Mostrar gastos")
        print("3 - Eliminar gasto")
        print("4 - Resumen mensual de gastos")
        print("5 - Registrar ingreso")
        print("6 - Mostrar ingresos")
        print("7 - Resumen mensual de ingresos")
        print("0 - Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Opción no válida.")
            continue

        if opcion == 0:
            guardar_datos("gastos.txt", gastos)
            guardar_datos("ingresos.txt", ingresos)
            print("Datos guardados. Saliendo...")
            break

        elif opcion == 1:
            try:
                monto = float(input("Monto del gasto: "))
                fecha = ingresar_fecha("Fecha (dd/mm/yyyy): ")
                categoria = _elegir_de_menu(CATEGORIAS_GASTOS, "Categoría")
                gastos = registrar_gasto(gastos, monto, fecha, categoria)
                print(" Gasto registrado correctamente.")
            except Exception as e:
                print(f"Error: {e}")
                registrar_evento(f"Error registrando gasto: {e}")

        elif opcion == 2:
            mostrar_gastos(gastos)

        elif opcion == 3:
            mostrar_gastos(gastos)
            try:
                idx = int(input("ID a eliminar: "))
                gastos = eliminar_gasto(gastos, idx)
            except Exception as e:
                print(f"Error: {e}")
                registrar_evento(f"Error eliminando gasto: {e}")

        elif opcion == 4:
            fecha = ingresar_periodo("Periodo (mm/yyyy):")
            resumen_mensual(gastos, fecha)

        elif opcion == 5:
            try:
                monto = float(input("Monto del ingreso: "))
                fecha = ingresar_fecha("Fecha (dd/mm/yyyy): ")
                categoria = _elegir_de_menu(CATEGORIAS_INGRESOS, "Categoría")
                ingresos = registrar_ingreso(ingresos, monto, fecha, categoria)
                print(" Ingreso registrado correctamente.")
            except Exception as e:
                print(f"Error: {e}")
                registrar_evento(f"Error registrando ingreso: {e}")

        elif opcion == 6:
            mostrar_ingresos(ingresos)

        elif opcion == 7:
            mes = input("Mes (mm/yyyy): ")
            resumen_ingresos(ingresos, mes)
        else:
            print("Opción no válida.")
