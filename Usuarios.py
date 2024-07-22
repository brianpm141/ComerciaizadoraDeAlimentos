from Personas import Persona

class Usuario(Persona):
    def __init__(self,id, nombre, apaterno, amaterno, telefono, usuario, psw, nivel):
        self.usuario = usuario
        self.psw = psw
        self.nivel = int(nivel)
        self.status = 1
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

x = Usuario(1,"carlito","campos", "campos", "72234231", "admin","admin",3)
y = Usuario(2,"carlito2","campos", "campos", "72234231", "user2","12345",2)
z = Usuario(3, "carlito3", "campos", "campos", "72234231", "user1", "12345", 1)

listaUsuaros = [x,y,z]

def buscarUsuario(usuario):
    for usr in listaUsuaros:
        if usuario == usr.getusuario():
            return (usr.getpsw(), usr.getnivel(),usr.getid())
    return None, None, None

def creacionUsuario(nombre, apaterno, amaterno, telefono, usuario, psw, nivel):
    id = len(listaUsuaros) + 1
    usuaux = Usuario(id, nombre, apaterno, amaterno, telefono, usuario, psw, nivel)
    listaUsuaros.append(usuaux)




