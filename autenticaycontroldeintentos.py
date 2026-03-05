

def validacion ():
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

