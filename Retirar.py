 
def retiro():
    menu = int(input("Digite la opcion 2 "))
    if menu == 2:
     while True:
        retiro = int(input("Digite el valor a retirar: "))
        if retiro <= saldo_inicial:
            saldo_inicial -= retiro
            print("Retiro exitoso. Saldo actual:", saldo_inicial)
            break
        else:
            print("Saldo insuficiente, intente otra vez")

retiro()   









    
    