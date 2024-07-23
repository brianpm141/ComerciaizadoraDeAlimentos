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

    def getid_producto(self):
        return self.id_producto

    def getcantidad(self):
        return self.cantidad

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

    def setid_producto(self, id_producto):
        self.id_producto.append(int(id_producto))

    def setcantidad(self, cantidad):
        self.cantidad.append(int(cantidad))

    def setmetodo_pago(self, metodo_pago):
        self.metodo_pago = metodo_pago

    def setid_usuario(self, id_usuario):
        self.id_usuario = int(id_usuario)
