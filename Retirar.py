def retiro(saldo):
    verdadero=True
    while verdadero:
        valor = int(input("Digite el valor a retirar: "))
        if valor <= saldo:
            saldo -= valor
            print("Retiro exitoso. Saldo actual:", saldo)
            verdadero=False
        else:
            verdadero=False
            print("Saldo insuficiente")
            return saldo 

    
    
    
    