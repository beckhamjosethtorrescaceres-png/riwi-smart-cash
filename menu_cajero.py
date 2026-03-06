# menu_cajero.py
# Nikolaz - Menú interactivo del cajero automático
# Etapa final - Listo para conectar con las funciones reales del equipo

def mostrar_menu():
    print("\n" + "═" * 45)
    print("          CAJERO AUTOMÁTICO - MENÚ PRINCIPAL")
    print("═" * 45)
    print("  1  →  Consultar saldo")
    print("  2  →  Retirar dinero")
    print("  3  →  Depositar dinero")
    print("  4  →  Cambiar PIN")
    print("  5  →  Salir")
    print("═" * 45)


def consultar_saldo():
    
    print("  → Consultando saldo... (pendiente de integración)")
    print("    Saldo actual: [en desarrollo]\n")


def retirar_dinero():
    
    print("  → Iniciando retiro... (pendiente de integración)")
    print("    Monto a retirar: [en desarrollo]\n")


def depositar_dinero():
    
    print("  → Procesando depósito... (pendiente de integración)")
    print("    Monto a depositar: [en desarrollo]\n")


def cambiar_pin():
    
    print("  → Iniciando cambio de PIN... (pendiente de integración)") 
    print("    Nuevo PIN: [en desarrollo]\n")



print("╔════════════════════════════════════════════╗")
print("║     BIENVENIDO AL CAJERO AUTOMÁTICO        ║")
print("╚════════════════════════════════════════════╝\n")

while True:
    mostrar_menu()

    try:
        opcion = int(input("  → Tu opción: "))
        print()  
    except ValueError:
        print("  ¡Error! Debes ingresar un número (1-5).\n")
        continue

    if opcion == 1:
        consultar_saldo()
    elif opcion == 2:
        retirar_dinero()
    elif opcion == 3:
        depositar_dinero()
    elif opcion == 4:
        cambiar_pin()
    elif opcion == 5:
        print("  ╔════════════════════════════════════╗")
        print("  ║   ¡Gracias por usar nuestro cajero!   ║")
        print("  ║          ¡Vuelve pronto! 👋           ║")
        print("  ╚════════════════════════════════════╝\n")
        break
    else:
        print("  Opción no válida. Elige entre 1 y 5.\n")
