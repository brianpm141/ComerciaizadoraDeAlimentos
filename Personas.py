class Persona:
    def __init__(self,id,  nombre, apaterno, amaterno, telefono):
        self.id_usuario = int(id)
        self.nombre = nombre
        self.apaterno = apaterno
        self.amaterno = amaterno
        self.telefono = int(telefono)

    def getid(self):
        return self.id_usuario

    def getnombre(self):
        return self.nombre

    def getapaterno(self):
        return self.apaterno

    def getamaterno(self):
        return self.amaterno

    def gettelefono(self):
        return self.telefono

    def setnombre(self, nombre):
        self.nombre = nombre

    def setapaterno(self, apaterno):
        self.apaterno = apaterno

    def setamaterno(self, amaterno):
        self.amaterno = amaterno

    def settelefono(self, telefono):
        self.telefono = telefono