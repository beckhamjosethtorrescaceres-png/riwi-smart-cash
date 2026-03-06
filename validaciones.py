def validar_entrada_numerica(entrada):
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print("ERROR: Debe ingresar un número entero válido.")
        return None
