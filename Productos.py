class Producto:
    def __init__(self,id, nombre, tipo, peso, precio, cantidad):
        self.id = int(id)
        self.nombre = nombre
        self.tipo = tipo
        self.peso = int(peso)
        self.precio = int(precio)
        self.cantidad = int(cantidad)