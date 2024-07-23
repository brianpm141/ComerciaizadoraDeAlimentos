class Registros:
    def __init__(self,id_registro,fecha,hora,id_usuario,tipo_mov,id_mov):
        self.id_registro = int(id_registro)
        self.fecha = fecha
        self.hora = hora
        self.id_usuario = int(id_usuario)
        self.tipo_mov = int(tipo_mov)
        self.id_mov = int(id_mov)

def getid_registro(self):
    return self.id_registro

def getfecha(self):
    return self.fecha

def gethora(self):
    return self.hora

def getid_usuario(self):
    return self.id_usuario

def gettipomov(self):
    return self.tipomov

def getid_mov(self):
    return self.id_mov

def setid_registro(self,id_registro):
    self.id_registro = id_registro

def sethora(self,hora):
    self.hora = hora

def setid_usuario(self,id_usuario):
    self.id_usuario = int(id_usuario)

def setitimomov(self,tipomov):
    self.tipomov = int(tipomov)

def setid_mov(self,id_mov):
    self.id_mov = int(id_mov)

    