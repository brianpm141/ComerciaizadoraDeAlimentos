from Clases.Personas import Persona
import Clases.Registros as reg
import csv


class Cliente(Persona):
    def __init__(self, id, nombre, apaterno, amaterno, telefono, correo, direccion):
        self.correo = correo
        self.direccion = direccion
        self.status = 1
        super().__init__(id, nombre, apaterno, amaterno, telefono)

    def __str__(self):
        return f" ID: {self.id}  -  Nombre del cliente: {self.nombre} {self.apaterno} {self.amaterno}"

    def getcorreo(self):
        return self.correo

    def getdireccion(self):
        return self.direccion

    def getStatus(self):
        return self.status

    def setcorreo(self, correo):
        self.correo = correo

    def setdireccion(self, direccion):
        self.direccion = direccion

    def setstatus(self,status):
        self.status = status

    def modificarCliente(self,nombre, apaterno, amaterno, telefono, correo, direccion):
        self.setnombre(nombre)
        self.setapaterno(apaterno)
        self.setamaterno(amaterno)
        self.settelefono(telefono)
        self.setcorreo(correo)
        self.setdireccion(direccion)


def cargar_desde_csv():
    lista_clien_aux = []
    try:
        with open('./Archivos/clientes.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    id, nombre, apaterno, amaterno, telefono,correo, direccion,status = row
                    cln = Cliente(id, nombre, apaterno, amaterno, telefono, correo, direccion)
                    cln.setstatus(int(status))
                    lista_clien_aux.append(cln)
    except FileNotFoundError:
        print(f"El archivo {'./Archivos/clientes.csv'} no se encuentra.")
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
    return lista_clien_aux


listaClientes = cargar_desde_csv()


def crearCliente(nombre, apaterno, amaterno, telefono, correo, direccion,id_usuario):
    id = len(listaClientes) + 1
    telefono = int(telefono)
    clnaux = Cliente(id, nombre, apaterno, amaterno, telefono, correo, direccion)
    listaClientes.append(clnaux)
    guardar_en_csv(listaClientes)
    reg.crearRegistro(id_usuario, "Creacion de Cliente", id)


def guardar_en_csv(lista_productos):
    with open('./Archivos/clientes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir la cabecera del CSV
        writer.writerow(["id", "nombre", "apaterno", "amaterno", "telefono","correo","direccion","status"])
        for cliente in listaClientes:
            writer.writerow([cliente.getid(), cliente.getnombre(),cliente.getapaterno(),cliente.getamaterno(),cliente.gettelefono(),
                             cliente.getcorreo(),cliente.getdireccion(),cliente.getStatus()])


def buscarClienteid(num):
    for cli in listaClientes:
        if num == cli.getid():
            return cli
    return False


def modificarCliente(id_usu,nombre, apaterno, amaterno, telefono, correo, direccion,id_ses):
    for cln in listaClientes:
        if id_usu == cln.getid():
            cln.modificarCliente(nombre, apaterno, amaterno, telefono, correo, direccion)
            guardar_en_csv(listaClientes)
            reg.crearRegistro(id_ses, "Modificar Cliente", id_usu)


def eliminarCliente(id_usuario, id_ses):
    for cli in listaClientes:
        if cli.getid() == id_ses:
            if cli.getStatus() == 1:
                cli.setstatus(0)
                guardar_en_csv(listaClientes)
                reg.crearRegistro(id_usuario, "Eliminar Cliente", id_ses)
            else:
                return False
            return True
    return False

def is_empty():
    for prod in listaClientes:
        if prod.getStatus() == 1: return False
    return True



