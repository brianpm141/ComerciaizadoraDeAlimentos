from Clases.Personas import Persona
import csv

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

    def getstatus(self):
        return self.status

    def setusuario(self):
        self.usuario = self.usuario

    def setpsw(self):
        self.psw = self.psw

    def setnivel(self):
        self.nivel = self.nivel

    def setstatus(self):
        self.status = self.status

    def __str__(self):
        return f" Usuario: {self.usuario} -- Nivel:{self.nivel}"


def cargar_desde_csv():
    lista_productos = []
    try:
        with open('../Archivos/usuarios.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    id, nombre, apaterno, amaterno, telefono, usuario, psw, nivel,status = row
                    usuario = Usuario(id, nombre, apaterno, amaterno, telefono, usuario, psw, nivel)
                    usuario.setstatus(int(status))
                    lista_productos.append(usuario)
    except FileNotFoundError:
        print(f"El archivo {'./Archivos/usuarios.csv'} no se encuentra.")
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
    return lista_productos


listaUsuaros = cargar_desde_csv()

def buscarUsuario(usuario):
    for usr in listaUsuaros:
        if usuario == usr.getusuario():
            return (usr.getpsw(), usr.getnivel(),usr.getid())
    return None, None, None


def getnombre_usuario(valor):
    for usr in listaUsuaros:
        if valor == usr.getid():
            return usr.getusuario()


def is_empty():
    for prod in listaUsuaros:
        if prod.getstatus() == 1: return False
    return True


def crearUsuario(nombre, apaterno, amaterno, telefono, usuario, psw, nivel):
    id = len(listaUsuaros) + 1
    if nivel == "Administrador":
        nivel = 3
    elif nivel == "Gerente":
        nivel = 2
    else:
        nivel = 1
    telefono = int(telefono)
    usuaux = Usuario(id, nombre, apaterno, amaterno, telefono, usuario, psw, nivel)
    listaUsuaros.append(usuaux)
    print(usuaux.__str__())

def guardar_en_csv(lista_productos):
    with open('../Archivos/usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir la cabecera del CSV
        writer.writerow(["id", "nombre", "apaterno", "amaterno", "telefono", "usuario", "psw", "nivel,status"])
        for usuario in listaUsuaros:
            writer.writerow([usuario.getid(), usuario.getnombre(),usuario.getapaterno(),usuario.gettelefono(),
                             usuario.getusuario(),usuario.getpsw(),usuario.getnivel(),usuario.getstatus()])

guardar_en_csv(listaUsuaros)




