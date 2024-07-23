from datetime import datetime
import csv


class Registro:
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

def cargar_registros_desde_csv():
    lista_registros = []
    try:
        with open('Archivos/registros.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    id_registro, fecha, hora, id_usuario, tipo_mov, id_mov = row
                    registro = Registro(id_registro, fecha, hora, id_usuario, tipo_mov, id_mov)
                    lista_registros.append(registro)
    except FileNotFoundError:
        print(f"El archivo {'Archivos/registros.csv'} no se encuentra.")
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
    return lista_registros

lista_registros = cargar_registros_desde_csv()

def crearRegistro(id_usuario,tipo_mov,id_mov):
    id = len(lista_registros) + 1
    ahora = datetime.now()
    fecha = ahora.strftime('%Y-%m-%d')
    hora = ahora.strftime('%H:%M:%S')

    regaux = Registro(id, fecha,hora,id_usuario,tipo_mov,id_mov)
    lista_registros.append(regaux)
    guardar_registros_en_csv()

def guardar_registros_en_csv():
    with open('Archivos/registros.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID Registro", "Fecha", "Hora", "ID Usuario", "Tipo Movimiento", "ID Movimiento"])
        for registro in lista_registros:
            writer.writerow([registro.id_registro, registro.fecha, registro.hora, registro.id_usuario, registro.tipo_mov, registro.id_mov])




    