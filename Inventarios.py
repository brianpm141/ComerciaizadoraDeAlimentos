lista_Productos = []


class Producto:
    def __init__(self, id, nombre, precio, categoria, peso, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.peso = peso
        self.stock = stock
        self.status = 1

    def imprimir_producto(self):
        if self.status == 1:
            print (f"ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}, "
                    f"Categoría: {self.categoria}, Peso: {self.peso}kg, Stock: {self.stock}")

    def implrimir_producto_eliminado(self):
        if self.status == 0:
            print (f"ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}, "
                    f"Categoría: {self.categoria}, Peso: {self.peso}kg, Stock: {self.stock}")


        print("Producto Modificado")
    def eliminar_producto(self):
        self.status = 0

