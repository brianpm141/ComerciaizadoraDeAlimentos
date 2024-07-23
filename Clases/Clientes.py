from Clases.Personas import Persona


class Cliente(Persona):
    def __init__(self, id, nombre, apaterno, amaterno, telefono, correo, direccion):
        self.correo = correo
        self.direccion = direccion
        super().__init__(id, nombre, apaterno, amaterno, telefono)

    def getCorreo(self):
        return self.correo

    def getDireccion(self):
        return self.direccion

    def setCorreo(self, correo):
        self.correo = correo

    def setDireccion(self, direccion):
        self.direccion = direccion



