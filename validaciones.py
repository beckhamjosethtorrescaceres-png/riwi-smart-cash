# Validar que sea entero positivo y no extremadamente grande
def validar_entrada_numerica(entrada):
    try:
        numero = int(entrada)
        return True

    except ValueError:
        print("ERROR: Debe ingresar un número entero válido.")
        return False



