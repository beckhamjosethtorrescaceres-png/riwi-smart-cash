
print("hola")

# Validar que la entrada sea numérica
def validar_entrada_numerica(entrada):
    try:
        float(entrada)
        return True
    except ValueError:
        print("Error: La entrada tiene que ser numerica.")
        return False


validar_entrada_numerica("")