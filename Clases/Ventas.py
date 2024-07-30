import csv
import io
import os
import tempfile
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfgen import canvas as rl_canvas
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from datetime import datetime
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import Clases.Registros as reg
import Clases.Productos as prod


class Venta:
    def __init__(self, id, fecha, hora, id_usuario, id_producto, cantidad, subtotal, metodo_pago):
        self.id = int(id)
        self.fecha = fecha
        self.hora = hora
        self.id_usuario = id_usuario
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.subtotal = subtotal
        self.metodo_pago = metodo_pago

    def getid(self):
        return self.id

    def getfecha(self):
        return self.fecha

    def gethora(self):
        return self.hora

    def getid_producto(self):
        return self.id_producto

    def getcantidad(self):
        return self.cantidad

    def getsubtotal(self):
        return self.subtotal

    def getmetodo_pago(self):
        return self.metodo_pago

    def getid_usuario(self):
        return self.id_usuario

    def setid(self, id):
        self.id = int(id)

    def setfecha(self, fecha):
        self.fecha = fecha

    def sethora(self, hora):
        self.hora = hora

    def setid_producto(self, id_producto):
        self.id_producto = id_producto

    def setcantidad(self, cantidad):
        self.cantidad = cantidad

    def setsubtotal(self, subtotal):
        self.subtotal = subtotal

    def setmetodo_pago(self, metodo_pago):
        self.metodo_pago = metodo_pago

    def setid_usuario(self, id_usuario):
        self.id_usuario = int(id_usuario)

    def __str__(self):
        return f"ID: {self.id} - Fecha: {self.fecha} - Subtotal: {self.subtotal}"


def cargar_desde_csv():
    lista_productos = []
    try:
        with open('./Archivos/ventas.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    id, fecha, hora, id_usuario, id_producto, cantidad, subtotal, metodo_pago = row
                    ventaux = Venta(id, fecha, hora, id_usuario, id_producto, cantidad, subtotal, metodo_pago)
                    lista_productos.append(ventaux)
    except FileNotFoundError:
        print(f"El archivo {'./Archivos/ventas.csv'} no se encuentra.")
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
    return lista_productos


listaVentas = cargar_desde_csv()


def guardar_en_csv(lista_ventas):
    with open('./Archivos/ventas.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "fecha", "hora", "id_usuario", "id_producto", "cantidad", "subtotal", "metodo_pago"])
        for venta in lista_ventas:
            writer.writerow([venta.getid(), venta.getfecha(), venta.gethora(), venta.getid_usuario(), venta.getid_producto(),
                             venta.getcantidad(), venta.getsubtotal(), venta.getmetodo_pago()])


def is_empty():
    return len(listaVentas) == 0


def buscarVenta(id):
    for venta in listaVentas:
        if venta.getid() == id:
            return venta
    return None


def crearVenta(id_ses, id_usuario, id_producto, cantidad, subtotal, metodo_pago):
    now = datetime.now()
    id = len(listaVentas) + 1
    fecha = now.strftime("%Y-%m-%d")
    hora = now.strftime("%H:%M:%S")
    clnaux = Venta(id, fecha, hora, id_usuario, id_producto, cantidad, subtotal, metodo_pago)
    listaVentas.append(clnaux)
    guardar_en_csv(listaVentas)
    reg.crearRegistro(id_ses, "Nueva venta", id)
    for idaux, cantaux in zip(id_producto, cantidad):
        prod.restaInventario(idaux, cantaux)


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
    for item in listaVentas:
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
        writer.writerow(["id", "fecha", "id_usuario", "id_producto", "cantidad", "subtotal", "metodo_pago"])
        for venta in listaVentas:
            writer.writerow([venta.getid(), venta.getfecha(), venta.getid_usuario(), venta.getid_producto(),
                             venta.getcantidad(), venta.getsubtotal(), venta.getmetodo_pago()])


def gengerarexel(ruta):
    columnas = ["id", "fecha", "hora", "id_usuario", "id_producto", "cantidad", "subtotal", "metodo_pago"]
    datos = [
        [pedido.getid(), pedido.getfecha(), pedido.gethora(), pedido.getid_usuario(), pedido.getid_producto(),
         pedido.getcantidad(), pedido.getsubtotal(), pedido.getmetodo_pago()]
        for pedido in listaVentas
    ]
    df = pd.DataFrame(datos, columns=columnas)
    df.to_excel(ruta, index=False, engine='openpyxl')


def calcular_ventas_diarias():
    ventas_diarias = {}
    for venta in listaVentas:
        fecha = venta.getfecha()
        if fecha in ventas_diarias:
            ventas_diarias[fecha] += 1
        else:
            ventas_diarias[fecha] = 1
    return ventas_diarias


def generar_grafica_ventas_diarias(pdf_ruta):
    ventas_diarias = calcular_ventas_diarias()

    fechas = list(ventas_diarias.keys())
    cantidades = list(ventas_diarias.values())

    # Crear la gráfica
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(fechas, cantidades, color='blue')
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Cantidad de Ventas')
    ax.set_title('Ventas Diarias')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar la gráfica en un buffer en memoria
    buffer = io.BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(buffer)
    plt.close(fig)

    # Crear un archivo temporal para la imagen
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_file_path = temp_file.name
    temp_file.write(buffer.getvalue())
    temp_file.close()

    # Agregar la gráfica al PDF
    c = rl_canvas.Canvas(pdf_ruta, pagesize=letter)
    width, height = letter
    c.drawString(50, height - 50, "Gráfica de Ventas Diarias")
    c.drawImage(temp_file_path, 50, height - 400, width=500, height=300)
    c.save()

    # Eliminar el archivo temporal
    os.remove(temp_file_path)

