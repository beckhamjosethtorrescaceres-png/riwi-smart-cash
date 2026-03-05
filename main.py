from consultar_saldo import consultar_s
from Retirar import retiro
from deposito import deposito
from autenticaycontroldeintentos import validarusuarioeintentos
from historial import mostrar_historial
historial = []
saldo =1000
saldoretirado=0
saldodeposito=0

validacion = validarusuarioeintentos ()
if validacion == True:
    
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
            historial.append(f"consulto :{saldo}")
        elif opcion == 2:
            print("  → Iniciando retiro... ")
            saldoretirado= retiro(saldo)
            saldo=saldoretirado
            historial.append(f"retiro :{saldo}")
        elif opcion == 3:
            print("  → Iniciando depósito... ")
            saldodeposito=deposito(saldo)
            saldo=saldodeposito
            historial.append(f"deposito :{saldo}")
        elif opcion == 4:
            print("  ╔════════════════════════════════════╗")
            print("  ║   ¡Gracias por usar nuestro cajero!   ║")
            print("  ║          ¡Vuelve pronto! 👋           ║")
            print("  ╚════════════════════════════════════╝\n")
            mostrar_historial(historial)
            break
        else:
            print("  Opción no válida. Elige entre 1 y 5.\n")
