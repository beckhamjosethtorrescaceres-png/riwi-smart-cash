
print("hola")

# Validar que la entrada sea numérica
def validar_entrada_numerica(entrada):
    try:
        float(entrada)
        return True
    except ValueError:
        return False

# Que no esté vacío
def validar_entrada_no_vacia(entrada):
    if entrada.strip() == "":
        print("Error: La entrada no puede estar vacía.")
        return False
    return True


