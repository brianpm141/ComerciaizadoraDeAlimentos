import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from Clases import Clientes as cln  # Asegúrate de importar la clase adecuada
import re  # Importa el módulo de expresiones regulares

def crearCliente(id_usuario, actualizar_lista_callback):
    def salir():
        root.destroy()

    def completar():
        nombre = entry_nombre.get()
        apaterno = entry_apaterno.get()
        amaterno = entry_amaterno.get()
        telefono = entry_telefono.get()
        correo = entry_correo.get()
        direccion = entry_direccion.get()

        def es_entero(valor):
            try:
                int(valor)
                return True
            except ValueError:
                return False

        def es_correo_valido(correo):
            patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            return re.match(patron, correo) is not None

        if not nombre or not apaterno or not amaterno or not telefono or not correo or not direccion:
            messagebox.showerror("Error", "¡Introduce todos los campos!")
        elif len(nombre) > 24:
            messagebox.showerror("Error", "¡El nombre no puede tener más de 24 caracteres!")
        elif len(apaterno) > 24:
            messagebox.showerror("Error", "¡El apellido paterno no puede tener más de 24 caracteres!")
        elif len(amaterno) > 24:
            messagebox.showerror("Error", "¡El apellido materno no puede tener más de 24 caracteres!")
        elif not es_entero(telefono) or len(telefono) != 10:
            messagebox.showerror("Error", "¡Introduce un número de teléfono válido de 10 dígitos!")
        elif not es_correo_valido(correo):
            messagebox.showerror("Error", "¡Introduce un correo electrónico válido!")
        elif len(direccion) > 180:
            messagebox.showerror("Error", "¡La dirección no puede tener más de 180 caracteres!")
        else:
            cln.crearCliente(nombre, apaterno, amaterno, telefono, correo, direccion, id_usuario)
            actualizar_lista_callback()
            root.destroy()

    root = tk.Toplevel()
    root.title("Creacion de usuario")

    tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Apellido Paterno:").grid(row=1, column=0, padx=10, pady=5)
    entry_apaterno = tk.Entry(root)
    entry_apaterno.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Apellido Materno:").grid(row=2, column=0, padx=10, pady=5)
    entry_amaterno = tk.Entry(root)
    entry_amaterno.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Teléfono:").grid(row=3, column=0, padx=10, pady=5)
    entry_telefono = tk.Entry(root)
    entry_telefono.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Correo:").grid(row=4, column=0, padx=10, pady=5)
    entry_correo = tk.Entry(root)
    entry_correo.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="Dirección:").grid(row=5, column=0, padx=10, pady=5)
    entry_direccion = tk.Entry(root)
    entry_direccion.grid(row=5, column=1, padx=10, pady=5)

    btn_completar = tk.Button(root, text="Crear Cliente", command=completar)
    btn_completar.grid(row=9, column=0, padx=10, pady=10)

    btn_salir = tk.Button(root, text="Cancelar", command=salir)
    btn_salir.grid(row=9, column=1, padx=10, pady=10)

def editarCliente(id, actualizar_lista_callback):
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    while True:
        numero = simpledialog.askinteger("Entrada", "Ingrese el ID del cliente a modificar:")
        if numero is None:
            break
        elif cln.buscarClienteid(numero) == False:  # Aquí puedes agregar cualquier condición de validación que necesites
            messagebox.showerror("Error", "El cliente solicitado no existe.")
        else:
            dato = cln.buscarClienteid(numero)
            id_mod = dato.getid()
            nombre = dato.getnombre()
            apaterno = dato.getapaterno()
            amaterno = dato.getamaterno()
            telefono = dato.gettelefono()
            correo = dato.getcorreo()
            direccion = dato.getdireccion()

            def salir():
                root2.destroy()

            def editar():
                nombre = entry_nombre.get()
                apaterno = entry_apaterno.get()
                amaterno = entry_amaterno.get()
                telefono = entry_telefono.get()
                correo = entry_correo.get()
                direccion = entry_direccion.get()

                def es_entero(valor):
                    try:
                        int(valor)
                        return True
                    except ValueError:
                        return False

                def es_correo_valido(correo):
                    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                    return re.match(patron, correo) is not None

                if not nombre or not apaterno or not amaterno or not telefono or not correo or not direccion:
                    messagebox.showerror("Error", "¡Introduce todos los campos!")
                elif len(nombre) > 24:
                    messagebox.showerror("Error", "¡El nombre no puede tener más de 24 caracteres!")
                elif len(apaterno) > 24:
                    messagebox.showerror("Error", "¡El apellido paterno no puede tener más de 24 caracteres!")
                elif len(amaterno) > 24:
                    messagebox.showerror("Error", "¡El apellido materno no puede tener más de 24 caracteres!")
                elif not es_entero(telefono) or len(telefono) != 10:
                    messagebox.showerror("Error", "¡Introduce un número de teléfono válido de 10 dígitos!")
                elif not es_correo_valido(correo):
                    messagebox.showerror("Error", "¡Introduce un correo electrónico válido!")
                elif len(direccion) > 180:
                    messagebox.showerror("Error", "¡La dirección no puede tener más de 180 caracteres!")
                else:
                    cln.modificarCliente(id_mod, nombre, apaterno, amaterno, telefono, correo, direccion, id)
                    messagebox.showinfo("Exito", "Usuario modificado exitosamente.")
                    root2.destroy()
                    actualizar_lista_callback()

            root2 = tk.Toplevel()
            root2.title("Modificar Usuario")

            tk.Label(root2, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
            entry_nombre = tk.Entry(root2)
            entry_nombre.grid(row=0, column=1, padx=10, pady=5)
            entry_nombre.insert(0, nombre)

            tk.Label(root2, text="Apellido Paterno:").grid(row=1, column=0, padx=10, pady=5)
            entry_apaterno = tk.Entry(root2)
            entry_apaterno.grid(row=1, column=1, padx=10, pady=5)
            entry_apaterno.insert(0, apaterno)

            tk.Label(root2, text="Apellido Materno:").grid(row=2, column=0, padx=10, pady=5)
            entry_amaterno = tk.Entry(root2)
            entry_amaterno.grid(row=2, column=1, padx=10, pady=5)
            entry_amaterno.insert(0, amaterno)

            tk.Label(root2, text="Teléfono:").grid(row=3, column=0, padx=10, pady=5)
            entry_telefono = tk.Entry(root2)
            entry_telefono.grid(row=3, column=1, padx=10, pady=5)
            entry_telefono.insert(0, telefono)

            tk.Label(root2, text="Correo:").grid(row=4, column=0, padx=10, pady=5)
            entry_correo = tk.Entry(root2)
            entry_correo.grid(row=4, column=1, padx=10, pady=5)
            entry_correo.insert(0, correo)

            tk.Label(root2, text="Dirección:").grid(row=5, column=0, padx=10, pady=5)
            entry_direccion = tk.Entry(root2)
            entry_direccion.grid(row=5, column=1, padx=10, pady=5)
            entry_direccion.insert(0, direccion)

            btn_completar = tk.Button(root2, text="Modificar", command=editar)
            btn_completar.grid(row=9, column=0, padx=10, pady=10)

            btn_salir = tk.Button(root2, text="Cancelar", command=salir)
            btn_salir.grid(row=9, column=1, padx=10, pady=10)

            break  # Salir del bucle si se encontró el cliente

def eliminarCliente(id, actualizar_lista_callback):
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    while True:
        numero = simpledialog.askinteger("Entrada", "Ingrese el ID del cliente a eliminar:")
        if numero is None:
            break
        elif cln.buscarClienteid(numero) == False:
            messagebox.showerror("Error", "El cliente solicitado no existe.")
        else:
            cln.eliminarCliente(numero, id)
            messagebox.showinfo("Exito", "Usuario eliminado exitosamente.")
            actualizar_lista_callback()
            break

def actualizar_lista(lista_usuarios):
    lista_usuarios.delete(0, tk.END)
    if cln.is_empty():
        lista_usuarios.insert(tk.END, "No existe ningún Cliente registrado")
    else:
        for registro in cln.listaClientes:
            if registro.getStatus() == 1:
                lista_usuarios.insert(tk.END, str(registro))


def menuprincipal(ventana, nivel, id):
    ventana.destroy()
    import Vistas.MenuPrincipal as mp
    mp.main(nivel, id)


def main(nivel, id):
    def actualizar_lista_wrapper():
        actualizar_lista(lista_clientes)

    ventana = tk.Tk()
    ventana.title("Gestion de clientes")
    ventana.geometry("600x400")

    frame_izquierdo = tk.Frame(ventana)
    frame_izquierdo.pack(side=tk.LEFT, padx=10, pady=10)

    boton_crear_usuario = tk.Button(frame_izquierdo, text="Crear Cliente",
                                    command=lambda: crearCliente(id, actualizar_lista_wrapper))
    boton_crear_usuario.pack(pady=5)

    boton_editar_usuario = tk.Button(frame_izquierdo, text="Editar Cliente",
                                     command=lambda: editarCliente(id, actualizar_lista_wrapper))
    boton_editar_usuario.pack(pady=5)

    boton_eliminar = tk.Button(frame_izquierdo, text="Eliminar Cliente",
                               command=lambda: eliminarCliente(id, actualizar_lista_wrapper))
    boton_eliminar.pack(pady=5)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Regresar al Menú Principal",
                                     command=lambda: menuprincipal(ventana, nivel, id))
    boton_menu_principal.pack(pady=5)

    frame_derecho = tk.Frame(ventana)
    frame_derecho.pack(side=tk.RIGHT, padx=10, pady=10)

    global lista_clientes
    lista_clientes = tk.Listbox(frame_derecho, width=80, height=20)
    lista_clientes.pack()

    actualizar_lista(lista_clientes)
    ventana.mainloop()