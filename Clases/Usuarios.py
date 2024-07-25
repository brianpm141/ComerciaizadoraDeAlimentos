from Clases.Personas import Persona
import Clases.Registros as reg
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

    def setusuario(self,usuario):
        self.usuario = usuario

    def setpsw(self,psw):
        self.psw = psw

    def setnivel(self,nivel):
        self.nivel = nivel

    def setstatus(self,val):
        self.status = val

    def __str__(self):
        return f" ID: {self.id}  -  Usuario: {self.usuario} -- Nivel:{self.nivel}"


    def modificarUsuario(self,nombre, apaterno, amaterno, telefono, usuario, psw, nivel):
        self.setnombre(nombre)
        self.setapaterno(apaterno)
        self.setamaterno(amaterno)
        self.settelefono(telefono)
        self.setusuario(usuario)
        self.setpsw(psw)
        self.setnivel(nivel)




def cargar_desde_csv():
    lista_productos = []
    try:
        with open('./Archivos/usuarios.csv', mode='r') as file:
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


def buscarUsuarioid(num):
    for usr in listaUsuaros:
        if num == usr.getid():
            return usr
    return False


def getnombre_usuario(valor):
    for usr in listaUsuaros:
        if valor == usr.getid():
            return usr.getusuario()


def is_empty():
    for prod in listaUsuaros:
        if prod.getstatus() == 1: return False
    return True


def crearUsuario(id_usuario,nombre, apaterno, amaterno, telefono, usuario, psw, nivel):
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
    guardar_en_csv(listaUsuaros)
    reg.crearRegistro(id_usuario,"Creacion de usuario",id)


def guardar_en_csv(lista_productos):
    with open('./Archivos/usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir la cabecera del CSV
        writer.writerow(["id", "nombre", "apaterno", "amaterno", "telefono", "usuario", "psw", "nivel","status"])
        for usuario in listaUsuaros:
            writer.writerow([usuario.getid(), usuario.getnombre(),usuario.getapaterno(),usuario.getamaterno(),usuario.gettelefono(),
                             usuario.getusuario(),usuario.getpsw(),usuario.getnivel(),usuario.getstatus()])

def modificarUsuario(id_usu,nombre, apaterno, amaterno, telefono, usuario, psw, nivel,id_ses):
    if nivel == "Administrador":
        nivel = 3
    elif nivel == "Gerente":
        nivel = 2
    else:
        nivel = 1

    for usr in listaUsuaros:
        if id_usu == usr.getid():
            usr.modificarUsuario(nombre, apaterno, amaterno, telefono, usuario, psw, nivel)
            guardar_en_csv(listaUsuaros)
            reg.crearRegistro(id_ses, "Modificar Usuario", id_usu)

def eliminarUsuario(id_usuario, id_ses):
    for usr in listaUsuaros:
        if id_usuario == usr.getid():
            usr.setstatus(0)
            guardar_en_csv(listaUsuaros)
            reg.crearRegistro(id_ses, "Eliminar Usuario", id_ses)





