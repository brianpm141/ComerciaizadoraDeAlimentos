from Personas import Persona

class Usuario(Persona):
    def __init__(self,id, nombre, apaterno, amaterno, telefono, usuario, psw, nivel):
        self.usuario = usuario
        self.psw = psw
        self.nivel = int(nivel)
        super().__init__(id, nombre, apaterno, amaterno, telefono)

    def getusuario(self):
        return self.usuario

    def getpsw(self):
        return self.psw

    def getnivel(self):
        return self.nivel

    def setusuario(self):
        self.usuario = self.usuario

    def setpsw(self):
        self.psw = self.psw

    def setnivel(self):
        self.nivel = self.nivel

