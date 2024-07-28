import csv
from datetime import datetime
import Clases.Registros as reg


class Venta:
    def __init__(self, id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago):
        self.id = int(id)
        self.fecha = fecha
        self.hora = hora
        self.id_usuario = id_usuario
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.subtotal = subtotal
        self.metodo_pago = metodo_pago
        self.status = 1

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

    def getstatus(self):
        return self.status

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

    def setstatus(self, status):
        self.status = status

    def __str__(self):
        return f" ID: {self.id}  -  Fecha: {self.fecha}  -  Subtotal: {self.subtotal}"


def cargar_desde_csv():
    lista_productos = []
    try:
        with open('./Archivos/ventas.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago,status = row
                    ventaux = Venta(id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago)
                    ventaux.setstatus(int(status))
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
        # Escribir la cabecera del CSV
        writer.writerow(["id", "fecha","hora","id_usuario", "id_producto", "cantidad", "subtotal", "metodo_pago","status"])
        for venta in lista_ventas:
            writer.writerow([venta.getid(),venta.getfecha(),venta.gethora(),venta.getid_usuario(),venta.getid_producto()
                                ,venta.getcantidad(),venta.getsubtotal(),venta.getmetodo_pago(),venta.getstatus()])


def is_empty():
    for venta in listaVentas:
        if venta.getstatus() == 1: return False
    return True

def buscarVenta(num):
    for vnt in listaVentas:
        if num == vnt.getid():
            return vnt
    return False


def crearVenta(id_usuario, id_producto, cantidad,  subtotal, metodo_pago):
    now = datetime.now()
    id = len(listaVentas) + 1
    fecha = now.strftime("%Y-%m-%d")
    hora = now.strftime("%H:%M:%S")
    clnaux = Venta(id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago)
    listaVentas.append(clnaux)
    guardar_en_csv(listaVentas)
    reg.crearRegistro(id_usuario, "Nueva venta", id)

def buscarVenta(id):
    for venta in listaVentas:
        if venta.getid() == id:
            if venta.getstatus() == 1:
                return venta
            else: return None
    return None


