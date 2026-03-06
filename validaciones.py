# Validar que sea entero positivo y no extremadamente grande
def validar_entrada_numerica(entrada):
    try:
        numero = int(entrada)

        if numero < 0:
            print("ERROR: No se permiten números negativos.")
            return False
        
        if numero == 0:
            print("ERROR: El monto debe ser mayor a 0.")
    

        if numero > 1_000_000_000:
            print("ERROR: El número es demasiado grande.")
            return False

        return True

    except ValueError:
        print("ERROR: Debe ingresar un número entero válido.")
        return False

# validar que el monto no sea mayor al saldo disponible
def validar_retiro_permitido(saldo_actual, monto_a_retirar):
    if monto_a_retirar <= saldo_actual:
        return True
    
    else:
        print (f"Error: Fondos insuficientes. Tu saldo es ${saldo_actual}.")
        return False