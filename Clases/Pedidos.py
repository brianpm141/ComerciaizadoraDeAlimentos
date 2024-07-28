import csv
from datetime import datetime
import Clases.Registros as reg
from Clases.Ventas import Venta


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
        return f" ID: {self.id}  -  Fecha: {self.fecha}  -  Subtotal: {self.subtotal}  -  Estado: {self.estado}  -  Fecha de Entrega: {self.fecha_entrega}"

def cargar_desde_csv():
    lista_productos = []
    try:
        with open('./Archivos/pedidos.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago,estado, id_cliente, fecha_entrega,status = row
                    pedtaux = Pedido(id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago,estado, id_cliente, fecha_entrega)
                    pedtaux.setstatus(int(status))
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
        writer.writerow(["id", "fecha","hora","id_usuario", "id_producto", "cantidad", "subtotal", "metodo_pago","estado", "id_cliente", "fecha_entrega","status"])
        for venta in lista_pedidos:
            writer.writerow([venta.getid(),venta.getfecha(),venta.gethora(),venta.getid_usuario(),venta.getid_producto()
                                ,venta.getcantidad(),venta.getsubtotal(),venta.getmetodo_pago(),venta.getestado(),
                             venta.getid_cliente(),venta.getfecha_entrega(),venta.getstatus()])


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
    clnaux = Pedido(id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago,estado, id_cliente, fecha_entrega)
    listaPedidos.append(clnaux)
    guardar_en_csv(listaPedidos)
    reg.crearRegistro(id_usuario, "Nuevo Pedido", id)


def buscarVenta(id):
    for venta in listaPedidos:
        if venta.getid() == id:
            if venta.getstatus() == 1:
                return venta
            else: return None
    return None


def actualizarPedido():
    print("set")