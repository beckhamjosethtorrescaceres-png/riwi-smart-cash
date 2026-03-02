# validacion de reglas de negocio

# validar que el monto sea positivo
def validar_monto_positivo(monto):
    """Verifica que el monto sea mayor a cero."""
    if monto > 0:
        return True
    else:
        print("Error: El monto debe ser mayor a $0.")
        return False
    
# validar que el monto no sea mayor al permitido
def validar_retiro_permitido(saldo_actual, monto_a_retirar):
    """Verifica si hay fondos suficientes."""
    if monto_a_retirar <= saldo_actual:
        return True
    else:
        print(f"Error: Fondos insuficientes. Tu saldo es ${saldo_actual}.")
        return False
