import Clases.Registros as reg
import csv


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

    def modificar_valores(self,id_usuario,nombre, tipo, peso, precio, cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = int(peso)
        self.precio = int(precio)
        self.cantidad = int(cantidad)

        reg.crearRegistro(id_usuario, "Modificar Producto", self.id)


def cargar_desde_csv():
    lista_productos = []
    try:
        with open('./Archivos/productos.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    id, nombre, tipo, peso, precio, cantidad, status = row
                    producto = Producto(id, nombre, tipo, peso, precio, cantidad)
                    producto.setstatus(int(status))
                    lista_productos.append(producto)
    except FileNotFoundError:
        print(f"El archivo {'./Archivos/productos.csv'} no se encuentra.")
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
    return lista_productos

lista_produtos = cargar_desde_csv()


def is_empty():
    for prod in lista_produtos:
        if prod.getstatus() == 1: return False
    return True

def crear_Producto(id_usuario,nombre, tipo, peso, precio, cantidad):
    id = len(lista_produtos) + 1
    aux = Producto(id, nombre, tipo, peso, precio, cantidad)
    lista_produtos.append(aux)
    guardar_en_csv(lista_produtos)
    reg.crearRegistro(id_usuario,"Crear Producto",id)

def eliminar_producto(id_usuario,id):
    for product in lista_produtos:
        if product.getid() == id:
            product.setstatus(0)
            guardar_en_csv(lista_produtos)
            reg.crearRegistro(id_usuario, "Eliminar Producto", id)
            return True
    return False

def buscar_producto(id):
    for product in lista_produtos:
        if product.getid() == id:
            return product
    return None

def guardar_en_csv(lista_productos):
    with open('./Archivos/productos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir la cabecera del CSV
        writer.writerow(["ID", "Nombre", "Tipo", "Peso", "Precio", "Cantidad", "Status"])
        # Escribir los datos de cada producto
        for producto in lista_productos:
            writer.writerow([producto.getid(), producto.getombre(), producto.gettipo(), producto.getpeso(), producto.getprecio(), producto.getcantidad(), producto.getstatus()])


