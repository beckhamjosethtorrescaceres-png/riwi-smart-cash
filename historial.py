def mostrar_historial(historial):
    print("\nHistorial de operaciones:")
    if len(historial) == 0:
        print("No se realizaron operaciones.")
    else:
        for operacion in historial:
            print("-", operacion)