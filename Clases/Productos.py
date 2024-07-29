import Clases.Registros as reg
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd


class Producto:
    def __init__(self,id, nombre, tipo, peso, precio, cantidad):
        self.id = int(id)
        self.nombre = nombre
        self.tipo = tipo
        self.peso = int(peso)
        self.precio = int(precio)
        self.cantidad = int(cantidad)
        self.enpedido = 0
        self.status = 1

    def __str__(self):
        if self.enpedido == 0:
            return f" id: {self.id}  -  Nombre: {self.nombre}  -  Peso: {self.peso}kg  -  Precio: {self.precio}$  -  Inventario:{self.cantidad}"
        else:
            return f" id: {self.id}  -  Nombre: {self.nombre}  -  Peso: {self.peso}kg  -  Precio: {self.precio}$  -  Inventario:{self.cantidad}  -  En pedido: {self.enpedido}"
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

    def getenpedido(self):
        return self.enpedido

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

    def setenpedido(self,enpedido):
        self.enpedido = enpedido

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
                    id, nombre, tipo, peso, precio, cantidad,enpedido, status = row
                    producto = Producto(id, nombre, tipo, peso, precio, cantidad)
                    producto.setenpedido(int(enpedido))
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


def restaInventario(id, cnt):
    for prod in lista_produtos:
        if id == prod.getid():
            prod.setcantidad(prod.getcantidad() - int(cnt))
    guardar_en_csv(lista_produtos)

def crear_Producto(id_usuario,nombre, tipo, peso, precio, cantidad):
    id = len(lista_produtos) + 1
    aux = Producto(id, nombre, tipo, peso, precio, cantidad)
    lista_produtos.append(aux)
    guardar_en_csv(lista_produtos)
    reg.crearRegistro(id_usuario,"Crear Producto",id)


def eliminar_producto(id_usuario,id):
    for product in lista_produtos:
        if product.getid() == id:
            if product.getstatus() == 1:
                product.setstatus(0)
                guardar_en_csv(lista_produtos)
                reg.crearRegistro(id_usuario, "Eliminar Producto", id)
            else: return False
            return True
    return False

def buscar_producto(id):
    for product in lista_produtos:
        if product.getid() == id:
            if product.getstatus() == 1:
                return product
            else: return None
    return None

def guardar_en_csv(lista_productos):
    with open('./Archivos/productos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir la cabecera del CSV
        writer.writerow(["ID", "Nombre", "Tipo", "Peso", "Precio", "Cantidad","enpedido" ,"Status"])
        # Escribir los datos de cada producto
        for producto in lista_productos:
            writer.writerow([producto.getid(), producto.getombre(), producto.gettipo(), producto.getpeso(), producto.getprecio(), producto.getcantidad(),producto.getenpedido(), producto.getstatus()])


def generar_pdf(ruta_archivo):
    c = canvas.Canvas(ruta_archivo, pagesize=letter)
    width, height = letter
    x = 50
    y = height - 50
    line_height = 14
    c.setFont("Helvetica-Bold", 16)
    c.drawString(x, y, "Datos de la Lista")
    y -= 30
    c.setFont("Helvetica", 12)
    for item in lista_produtos:
        if item.getstatus() == 1:
            c.drawString(x, y, str(item))
            y -= line_height

            # Si se llega al final de la página, agregar una nueva
            if y < 50:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 12)
    c.save()


def generarcsv(ruta):
    with open('./Archivos/productos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nombre", "Tipo", "Peso", "Precio", "Cantidad","En pedido"])
        for producto in lista_produtos:
            writer.writerow([producto.getid(), producto.getombre(), producto.gettipo(), producto.getpeso(), producto.getprecio(), producto.getcantidad(),producto.getenpedido()])


def generarexel(ruta):
    # Definir las columnas del DataFrame
    columnas = ["ID", "Nombre", "Tipo", "Peso", "Precio", "Cantidad","En pedido"]

    # Extraer los datos de los objetos Pedido
    datos = [
        [producto.getid(), producto.getombre(), producto.gettipo(), producto.getpeso(), producto.getprecio(), producto.getcantidad(),producto.getenpedido()]
        for producto in lista_produtos
    ]
    # Crear un DataFrame a partir de la lista de datos
    df = pd.DataFrame(datos, columns=columnas)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel(ruta, index=False, engine='openpyxl')