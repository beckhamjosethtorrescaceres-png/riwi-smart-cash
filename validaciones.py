# Validar que sea entero positivo y no extremadamente grande
def validar_entrada_numerica_extrema(entrada):
    try:
        numero = int(entrada)

        if numero < 0:
            print("ERROR: No se permiten números negativos.")
            return False

        if numero > 1_000_000_000:
            print("ERROR: El número es demasiado grande.")
            return False

        return True

    except ValueError:
        print("ERROR: Debe ingresar un número entero válido.")
        return False


# Validar que el monto sea mayor a cero
def validar_monto_positivo(monto):
    if monto > 0:
        return True
    else:
        print("Error: El monto debe ser mayor a 0.")
        return False


# Validar que el monto no sea mayor al saldo disponible
def validar_retiro_permitido(saldo_actual, monto_a_retirar):
    if monto_a_retirar <= saldo_actual:
        return True
    else:
        print(f"Error: Fondos insuficientes. Tu saldo es ${saldo_actual}.")
        return False


# --------------------------- RETIRO ------------------------------

def retiro(saldo):
    if not validar_entrada_numerica_extrema(saldo):
        return
    saldo = int(saldo)

    while True:
        valor = input("Digite el valor a retirar: ")

        # VALIDAR QUE SEA NUMÉRICO
        if not validar_entrada_numerica_extrema(valor):
            continue

        valor = int(valor)

        # Validaciones lógicas
        if not validar_monto_positivo(valor):
            continue

        if not validar_retiro_permitido(saldo, valor):
            continue

        # Si pasa todas las validaciones
        saldo -= valor
        print("✅ Retiro exitoso. Saldo actual:", saldo)
        return saldo


retiro(input("Ingrese su saldo actual: "))

# --------------------------- DEPÓSITO ------------------------------
def deposito(saldo):
    valor = input("valor a depositar: ")

    # Validar que sea número entero válido y no extremo
    if not validar_entrada_numerica_extrema(valor):
        return saldo

    deposito = int(valor)

    # Validar que sea mayor a 0
    if not validar_monto_positivo(deposito):
        return saldo

    confirmacion = input("confirma el valor ingresado?: ")

    if confirmacion.lower() == "si":
        print("su nuevo saldo es: ", saldo + deposito)
        return saldo + deposito
    else:
        print("deposito cancelado")
        return saldo
    
 
deposito(input("Ingrese su saldo actual: "))