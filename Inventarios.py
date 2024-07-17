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
        print("------------Datos del producto------------")
        print(f"ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}, "
              f"Categoría: {self.categoria}, Peso: {self.peso}kg, Stock: {self.stock}")
        print("------------Datos del producto------------")
        print("Para modificar añade un nuevo valor, si desea conservar el mismo solo de enter")
        print("El id del producto es: ",self.id)
        print("El nombre del producto es: ", self.nombre)
        nombre = input("Introduzca el nuevo nombre, para conservarlo precione enter: ")
        if nombre:
          self.nombre = nombre
        print("El precio del producto es: ", self.precio)
        precio = input("Introduzca el precio del producto, para conservarlo precione enter: ")
        if precio:
            self.precio = int(precio)
        print("La categoria del producto es: ", self.categoria)
        categoria = input("Introduzca la categoria del producto, para conservarlo precione enter: ")
        if categoria:
            self.categoria = categoria
        print("El peso del producto es: ", self.peso)
        peso = input("Introduzca el peso de producto, para conservarlo precione enter: ")
        if peso:
            self.peso = int(peso)
        print("El stock del producto es: ", self.stock)
        stock = input("Introduzca el stock del producto, para conservarlo precione enter: ")
        if stock:
            self.stock = int(stock)

        print("Producto Modificado")


def registrar_producto():
    id = int(len(lista_Productos)) + 1
    nombre = input("Introduce el nombre del producto: ")
    while not nombre:
        nombre = input("Por favor introduce el nombre del prooducto ")
    precio = input("Introduce el precio del producto en pesos: ")
    while not precio:
        precio = input("Introduce el precio del producto en pesos: ")
    precio = int(precio)
    categoria = input("Introduce el categoria del producto: ")
    while not categoria:
        categoria = input("Por favor introduce la categoria del producto: ")
    peso = input("Introduce el peso del producto en Kg: ")
    while not peso:
        peso = input("Por favor introduce el peso del producto en Hg: ")
    preso = int(peso)
    stock = input("Introduce el stock del producto en numero: ")
    while not stock:
        print("Por favor introduce el stock del producto en numero")
    stock = int(stock)
    prod = "prod",id

    prod = Producto(id, nombre, precio, categoria, peso, stock)
    lista_Productos.append(prod)


def imprimir_productos():
    if lista_Productos == []:
        print("No hay productos registrados")
    else:
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
                idaux = input("Introduce el id del producto que desea modificar, introduzca 0 para cancelar: ")
                while not idaux:
                    idaux = input("Por favor introduce el id, introduzca 0 para cancelar: ")
                idaux = int(idaux)
                for producto in lista_Productos:
                    if producto.id == idaux:
                        producto.modificar_producto()
                    else:
                        if idaux == 0:
                            print("Cancelando modificacion")
                        else:
                            print("El id no existe")
            else:
                idaux = int(input("Inserta el id del articulo a borrar : "))
                aux = eliminar_producto(idaux)
                if aux:
                    print("Producto eliminado")
                else:
                    print("Error al eliminar producto")

obj0 = Producto(1, "Purina Dog Chow Extra Life", 600, "Perros", 16, 15)
lista_Productos.append(obj0)
