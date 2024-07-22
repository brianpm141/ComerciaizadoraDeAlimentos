

class Producto:
    def __init__(self,id, nombre, tipo, peso, precio, cantidad):
        self.id = int(id)
        self.nombre = nombre
        self.tipo = tipo
        self.peso = int(peso)
        self.precio = int(precio)
        self.cantidad = int(cantidad)
        self.status = 1

    def __str__(self):
        return f" id: {self.id}  -  Nombre: {self.nombre}  -  Peso: {self.peso}kg  -  Inventario:{self.cantidad}"

    def getid(self):
        return self.id

    def getombre(self):
        return self.nombre

    def gettipo(self):
        return self.tipo

    def getpeso(self):
        return self.peso

    def getprecio(self):
        return self.precio

    def getcantidad(self):
        return self.cantidad

    def getstatus(self):
        return self.status

    def setid(self,id):
        self.id = id

    def setombre(self,nombre):
        self.nombre = nombre

    def settipo(self,tipo):
        self.tipo = tipo

    def setpeso(self,peso):
        self.peso = peso

    def setprecio(self,precio):
        self.precio = precio

    def setcantidad(self,cantidad):
        self.cantidad = cantidad

    def setstatus(self, status):
        self.status = status


x = Producto(1,"test","perro",45,159,200 )
lista_produtos = [x]


def is_empty():
    for prod in lista_produtos:
        if prod.getstatus() == 1: return False
    return True

def crear_Producto(nombre, tipo, peso, precio, cantidad):
    id = len(lista_produtos) + 1
    aux = Producto(id, nombre, tipo, peso, precio, cantidad)
    lista_produtos.append(aux)



