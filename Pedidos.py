from Ventas import Venta

class Pedido(Venta):
    def __init__(self, estado, id_cliente, fecha_entrega, id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago):
        self.estado = int(estado)
        self.id_cliente = int(id_cliente)
        self.fecha_entrega = fecha_entrega
        super().__init__( id, fecha,hora,id_usuario, id_producto, cantidad,  subtotal, metodo_pago)

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