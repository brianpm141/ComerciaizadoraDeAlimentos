lista_Productos = []


class Producto:
    def __init__(self, id, nombre, precio, categoria, peso, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.peso = peso
        self.stock = stock

    def imprimir_producto(self):
        print (f"ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}, "
                f"Categoría: {self.categoria}, Peso: {self.peso}kg, Stock: {self.stock}")

    def modificar_producto(self):
        print("Modificar")



def registrar_producto():
    id = int(len(lista_Productos)) + 1
    nombre = input("Introduce el nombre del producto: ")
    precio = int(input("Introduce el precio del producto: "))
    categoria = input("Introduce el categoria del producto: ")
    peso = int(input("Introduce el peso del producto: "))
    stock = int(input("Introduce el stock del producto: "))
    prod = "producto",id

    prod = Producto(id, nombre, precio, categoria, peso, stock)
    lista_Productos.append(prod)


def imprimir_productos():
    for producto in lista_Productos:
        producto.imprimir_producto()


def eliminar_producto(id):
    for producto in lista_Productos:
        if producto.id == id:
            lista_Productos.remove(producto)
            return True
    return False

def despliegue_menu():
    print("---------------Inventarios---------------------")
    print("Opcion 1: Registro Producto")
    print("Opcion 2: Lista de productos")
    print("Opcion 3: Modificar Producto")
    print("Opcion 4: Eliminar Producto")
    print("Opcion 0: Menu Principal")


def menu_inventarios():
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
            if op > 4 or op < 0:
                print("Introduzca una opcion valida")
                despliegue_menu()
            elif op == 0:
                print("Saliendo al menu principal")
                break
            elif op == 1:
                registrar_producto()
            elif op == 2:
                imprimir_productos()
            elif op == 3:
                print("Modificar Producto")
            else:
                idaux = int(input("Inserta el id del articulo a borrar : "))
                aux = eliminar_producto(idaux)
                if aux:
                    print("Producto eliminado")
                else:
                    print("Error al eliminar producto")

obj0 = Producto(0, "Purina Dog Chow Extra Life", 600, "Perros", 16, 15)
lista_Productos.append(obj0)
