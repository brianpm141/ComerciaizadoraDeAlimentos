import Loggin as lg
import Inventarios as inv

def despliegue_menu():
    print("-----------------Menu Principal--------------------------")
    print("Opcion 1: Menu de ventas")
    print("Opcion 2: Menu de inventarios")
    print("Opcion 3: Generar Reportes")
    print("Opcion 4: Gestion de usuarios")
    print("Opcion 5: Cerrar session")
    print("Opcion 0: Salir")


def main():
    aut = lg.loggin()
    if aut:
        print("-----------------------------------------------------")
        print("Seleccione una opcion")
        print("Introduzca el numero y precione enter")
        op = -1
        while op != 0:
            despliegue_menu()
            op = input()
            if not op:
                print("Introduzca una opcion valida")
            else:
                op = int(op)
                if op > 5 or op < 0:
                    print("Introduzca una opcion valida")
                    despliegue_menu()
                elif op == 0:
                    print("Saliendo...")
                    break
                elif op == 1:
                    print("ventas")
                elif op == 2:
                    inv.menu_inventarios()
                elif op == 3:
                    print("Reportes")
                elif op == 4:
                    print("usuarios")
                elif op == 5:
                    aut = False
                    main()  # Llama a la función main de nuevo


# Llamar a la función main para iniciar el programa
if __name__ == "__main__":
    main()

