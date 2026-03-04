from consultar_saldo import consultar_s
from Retirar import retiro
saldo = 1000
#Definiendo el nombre de usuario y su contraseña
user_name = "riwi"
user_password = 123
#Bool que valida que el usuario, contraseña y la cantidad de intentos sea menor que 3
is_valid= False
is_valid_atte=True
#Contador de intentos
attempts= 0

while is_valid==False and is_valid_atte==True:
    try:
        name=input("Digite el nombre de usuario: ")
        password=input("Digite su contraseña: ")
        password=int(password)
        if (name==user_name and password==user_password):
            is_valid=True
            print("Iniciaste sesión correctamente")
       
        else:
            print("Usuario y/o Contraseña inválidos")
            attempts=attempts+1
            print("Te quedan",3-attempts,"intentos")

        if (attempts==3) :
            print("Superaste la cantidad de intentos permitidos")
            is_valid_atte= False
    except:
        print("Usuario y/o Contraseña inválidos")
        attempts=attempts+1
        print("Te quedan",3-attempts,"intentos")
        if (attempts==3) :
            print("Superaste la cantidad de intentos permitidos")
            is_valid_atte= False      

def mostrar_menu():
    print("\n" + "═" * 45)
    print("          CAJERO AUTOMÁTICO - MENÚ PRINCIPAL")
    print("═" * 45)
    print("  1  →  Consultar saldo")
    print("  2  →  Retirar dinero")
    print("  3  →  Depositar dinero")
    print("  4  →  Salir")
    print("═" * 45)

def depositar_dinero():
    # Aquí irá la función real de depósito
    print("  → Procesando depósito... (pendiente de integración)")
    print("    Monto a depositar: [en desarrollo]\n")



# Programa principal
print("╔════════════════════════════════════════════╗")
print("║     BIENVENIDO AL CAJERO AUTOMÁTICO        ║")
print("╚════════════════════════════════════════════╝\n")

while True:
    mostrar_menu()

    try:
        opcion = int(input("  → Tu opción: "))
        print()  # línea en blanco para mejor lectura
    except ValueError:
        print("  ¡Error! Debes ingresar un número (1-5).\n")
        continue

    if opcion == 1:
        print("  → Consultando saldo... ")
        consultar_s(saldo)
    elif opcion == 2:
        print("  → Iniciando retiro... ")
        retiro(saldo)
    elif opcion == 3:
        depositar_dinero()
    elif opcion == 4:
        print("  ╔════════════════════════════════════╗")
        print("  ║   ¡Gracias por usar nuestro cajero!   ║")
        print("  ║          ¡Vuelve pronto! 👋           ║")
        print("  ╚════════════════════════════════════╝\n")
        break
    else:
        print("  Opción no válida. Elige entre 1 y 5.\n")