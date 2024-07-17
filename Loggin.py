import Usuarios as us

def loggin():
    print("-----------------------------------------------------")
    valido = False
    while not valido:
        print("Ingresa nombre de usuario o 0 si desea salir y preciona enter : ")
        usuario = input()
        if usuario == "0":
            print("Saliendo...")
            break
        while not usuario:
            print("-----------------------------------------------------")
            print("Ingresa un nombre de usuario: ")
            usuario = input()
        contaux = us.buscar_usuario(usuario)
        if contaux == None:
            print("El usuario no existe, intente otra vez")
            print("-----------------------------------------------------")
        else:
            print("Ingresa la contraseña y preciona enter")
            cont = input()
            if contaux == cont:
                valido = True
            else:
                print("Usuario o contraseña no validos, intente otra vez")
                print("-----------------------------------------------------")
    return valido
