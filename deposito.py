def deposito():
 deposito = int(input("valor a depositar: "))
 confirmacion = input("confirma el valor ingresado?: ")
 if deposito <=0:
      print("no se puede depositar un valor negativo")
 elif confirmacion.lower()=="si":
     print("su nuevo saldo es: ",saldo + deposito) 
          
 else:
    print("deposito cancelado")
             