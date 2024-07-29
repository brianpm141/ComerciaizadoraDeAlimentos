import csv
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
import Clases.Registros as reg
from Clases.Ventas import Venta
import Clases.Productos as prod


class Pedido(Venta):
    def __init__(self,id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago,estado, id_cliente, fecha_entrega):
        self.estado = estado
        self.id_cliente = int(id_cliente)
        self.fecha_entrega = fecha_entrega
        super().__init__(id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago)

    def getestado(self):
        return self.estado

    def getid_cliente(self):
        return self.id_cliente

    def getfecha_entrega(self):
        return self.fecha_entrega

    def setestado(self,estado):
        self.estado = estado

    def setid_cliente(self,id_cliente):
        self.id_cliente = id_cliente

    def setfecha_entrega(self,fecha_entrega):
        self.fecha_entrega = fecha_entrega

    def __str__(self):
        return f" ID: {self.id}  -  Fecha: {self.fecha}  -  Subtotal: {self.subtotal}  -  Estado: {self.estado}  -  Cliente: {self.id_cliente}  -  Fecha de Entrega: {self.fecha_entrega}"

def cargar_desde_csv():
    lista_productos = []
    try:
        with open('./Archivos/pedidos.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago,estado, id_cliente, fecha_entrega = row
                    pedtaux = Pedido(id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago,estado, id_cliente, fecha_entrega)
                    lista_productos.append(pedtaux)
    except FileNotFoundError:
        print(f"El archivo {'./Archivos/pedidos.csv'} no se encuentra.")
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
    return lista_productos


listaPedidos = cargar_desde_csv()


def guardar_en_csv(lista_pedidos):
    with open('./Archivos/pedidos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir la cabecera del CSV
        writer.writerow(["id", "fecha","hora","id_usuario", "id_producto", "cantidad", "subtotal", "metodo_pago","estado", "id_cliente", "fecha_entrega"])
        for venta in lista_pedidos:
            writer.writerow([venta.getid(),venta.getfecha(),venta.gethora(),venta.getid_usuario(),venta.getid_producto()
                                ,venta.getcantidad(),venta.getsubtotal(),venta.getmetodo_pago(),venta.getestado(),
                             venta.getid_cliente(),venta.getfecha_entrega()])


def is_empty():
    for pedido in listaPedidos:
        if pedido.getstatus() == 1: return False
    return True

def buscarVenta(num):
    for vnt in listaPedidos:
        if num == vnt.getid():
            return vnt
    return False


def crearPedido(id_usuario, id_producto, cantidad,  subtotal, metodo_pago,estado, id_cliente, fecha_entrega):
    now = datetime.now()
    id = len(listaPedidos) + 1
    fecha = now.strftime("%Y-%m-%d")
    hora = now.strftime("%H:%M:%S")
    clnaux = Pedido(id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago,estado,
                    id_cliente, fecha_entrega)
    listaPedidos.append(clnaux)
    guardar_en_csv(listaPedidos)
    reg.crearRegistro(id_usuario, "Nuevo Pedido", id)


def actualizarPedido():
    print("set")


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
    for item in listaPedidos:
        c.drawString(x, y, str(item))
        y -= line_height
        if y < 50:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 12)
    c.save()


def generarcsv(ruta):
    with open(ruta, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir la cabecera del CSV
        writer.writerow(["id", "fecha","hora","id_usuario", "id_producto", "cantidad", "subtotal", "metodo_pago","estado", "id_cliente", "fecha_entrega"])
        for venta in listaPedidos:
            writer.writerow([venta.getid(),venta.getfecha(),venta.gethora(),venta.getid_usuario(),venta.getid_producto()
                                ,venta.getcantidad(),venta.getsubtotal(),venta.getmetodo_pago(),venta.getestado(),
                             venta.getid_cliente(),venta.getfecha_entrega()])


def gengerarexel(ruta):
    # Definir las columnas del DataFrame
    columnas = ["id", "fecha","hora","id_usuario", "id_producto", "cantidad", "subtotal", "metodo_pago","estado", "id_cliente", "fecha_entrega"]

    # Extraer los datos de los objetos Pedido
    datos = [
        [pedido.getid(), pedido.getfecha(), pedido.gethora(), pedido.getid_usuario(), pedido.getid_producto(),
         pedido.getcantidad(), pedido.getsubtotal(), pedido.getmetodo_pago(), pedido.getestado(),
         pedido.getid_cliente(), pedido.getfecha_entrega()]
        for pedido in listaPedidos
    ]
    # Crear un DataFrame a partir de la lista de datos
    df = pd.DataFrame(datos, columns=columnas)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel(ruta, index=False, engine='openpyxl')
