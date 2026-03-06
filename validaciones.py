def validar_entrada_numerica(entrada):
    try:
        numero = int(entrada)
        if numero <= 0:
            print("ERROR: El número debe ser mayor a 0.")
            return None
        if numero > 1_000_000_000:
            print("ERROR: El número es demasiado grande.")
            return None
        return numero
    except ValueError:
        print("ERROR: Debe ingresar un número entero válido.")
        return None
