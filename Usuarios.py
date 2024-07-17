class usuario:
    def __init__(self,id , nombreus, cont, nivel):
        self.id = id
        self.nombreus = nombreus
        self.cont = cont
        self.nivel = nivel

    def get_usuario(self):
        return self.nombreus

    def get_cont(self):
        return self.cont

x = usuario(1,'admin', 'admin', 3)
y = usuario(2,'gerente', '12345', 2)
z = usuario(3,'vendedor', '12345', 1)
lista_usuarios = [x,y,z]


def buscar_usuario(nombre):
    for usu in lista_usuarios:
        if usu.get_usuario() == nombre:
            cont = usu.get_cont()
            return cont


print(buscar_usuario('jefe'))