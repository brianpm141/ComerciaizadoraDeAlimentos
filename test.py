import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
from Clases import Usuarios as usu  # Asegúrate de importar la clase adecuada

def crearUsuario(id_usuario, actualizar_lista_callback):
    niveles = {
        "Vendedor": 1,
        "Gerente": 2,
        "Administrador": 3
    }

    def salir():
        root.destroy()

    def completar():
        nombre = entry_nombre.get()
        apaterno = entry_apaterno.get()
        amaterno = entry_amaterno.get()
        telefono = entry_telefono.get()
        usuario = entry_usuario.get()
        psw = entry_psw.get()
        nivel = combo_nivel.get()

        def es_entero(valor):
            try:
                int(valor)
                return True
            except ValueError:
                return False

        if not nombre or not apaterno or not amaterno or not telefono or not usuario or not psw or not nivel:
            messagebox.showerror("Error", "¡Introduce todos los campos!")
        elif not es_entero(telefono) or len(telefono) != 10:
            messagebox.showerror("Error", "¡Introduce un número de teléfono válido de 10 dígitos!")
        elif nivel not in niveles:
            messagebox.showerror("Error", "¡Seleccione un nivel válido!")
        else:
            nivel_codigo = niveles[nivel]
            usu.crearUsuario(id_usuario,nombre, apaterno, amaterno, telefono, usuario, psw, nivel_codigo)
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

    tk.Label(root, text="Usuario:").grid(row=4, column=0, padx=10, pady=5)
    entry_usuario = tk.Entry(root)
    entry_usuario.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="Contraseña:").grid(row=5, column=0, padx=10, pady=5)
    entry_psw = tk.Entry(root, show="*")
    entry_psw.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(root, text="Nivel:").grid(row=6, column=0, padx=10, pady=5)
    combo_nivel = ttk.Combobox(root, values=list(niveles.keys()))
    combo_nivel.grid(row=6, column=1, padx=10, pady=5)

    btn_completar = tk.Button(root, text="Crear Usuario", command=completar)
    btn_completar.grid(row=7, column=0, padx=10, pady=10)

    btn_salir = tk.Button(root, text="Cancelar", command=salir)
    btn_salir.grid(row=7, column=1, padx=10, pady=10)

def editarUsuario(id,actualizar_lista_callback):
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    while True:
        numero = simpledialog.askinteger("Entrada", "Ingrese el ID del usuario a modificar:")
        if numero is None:
            break
        elif not usu.buscarUsuarioid(numero) :  # Aquí puedes agregar cualquier condición de validación que necesites
            messagebox.showerror("Error", "El usuario buscado no existe.")
        else:
            dato = usu.buscarUsuarioid(numero)
            id_mod = dato.getid()
            nombre = dato.getnombre()
            apaterno = dato.getapaterno()
            amaterno = dato.getamaterno()
            telefono = dato.gettelefono()
            usuario = dato.getusuario()
            psw = dato.getpsw()
            nivel = dato.getnivel()

            niveles = {
                "Vendedor": 1,
                "Gerente": 2,
                "Administrador": 3
            }

            if nivel == 1:
                nivel = "Vendedor"
            elif nivel == 2:
                nivel = "Gerente"
            else:
                nivel = "Administrador"
            def salir():
                root2.destroy()
            def editar():
                nombre = entry_nombre.get()
                apaterno = entry_apaterno.get()
                amaterno = entry_apmaterno.get()
                telefono = entry_telefono.get()
                usuario = entry_usuario.get()
                psw = entry_psw.get()
                nivel = combo_nivel.get()

                def es_entero(valor):
                    try:
                        int(valor)
                        return True
                    except ValueError:
                        return False

                if not nombre or not apaterno or not amaterno or not telefono or not usuario or not psw or not nivel:
                    messagebox.showerror("Error", "¡Introduce todos los campos!")
                elif not es_entero(telefono) or len(telefono) != 10:
                    messagebox.showerror("Error", "¡Introduce un número de teléfono válido de 10 dígitos!")
                elif nivel not in niveles:
                    messagebox.showerror("Error", "¡Seleccione un nivel válido!")
                else:
                    nivel_codigo = niveles[nivel]
                    usu.modificarUsuario(id_mod,nombre,apaterno,amaterno,telefono,usuario,psw,nivel,id)
                    messagebox.showinfo("Exito", "Usuario modificado exitosamente.")
                    root2.destroy()
                    actualizar_lista_callback()

            root2 = tk.Toplevel()
            root2.title("Modificar Usuario")

            tk.Label(root2, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
            entry_nombre = tk.Entry(root2)
            entry_nombre.grid(row=0, column=1, padx=10, pady=5)
            entry_nombre.insert(0,nombre)

            tk.Label(root2, text="Apellido Paterno:").grid(row=1, column=0, padx=10, pady=5)
            entry_apaterno = tk.Entry(root2)
            entry_apaterno.grid(row=1, column=1, padx=10, pady=5)
            entry_apaterno.insert(0,apaterno)

            tk.Label(root2, text="Apellido Materno:").grid(row=2, column=0, padx=10, pady=5)
            entry_apmaterno = tk.Entry(root2)
            entry_apmaterno.grid(row=2, column=1, padx=10, pady=5)
            entry_apmaterno.insert(0, amaterno)

            tk.Label(root2, text="Teléfono:").grid(row=3, column=0, padx=10, pady=5)
            entry_telefono = tk.Entry(root2)
            entry_telefono.grid(row=3, column=1, padx=10, pady=5)
            entry_telefono.insert(0,telefono)

            tk.Label(root2, text="Usuario:").grid(row=4, column=0, padx=10, pady=5)
            entry_usuario = tk.Entry(root2)
            entry_usuario.grid(row=4, column=1, padx=10, pady=5)
            entry_usuario.insert(0,usuario)

            tk.Label(root2, text="Contraseña:").grid(row=5, column=0, padx=10, pady=5)
            entry_psw = tk.Entry(root2, show="*")
            entry_psw.grid(row=5, column=1, padx=10, pady=5)
            entry_psw.insert(0,psw)

            tk.Label(root2, text="Nivel:").grid(row=6, column=0, padx=10, pady=5)
            combo_nivel = ttk.Combobox(root2, values=list(niveles.keys()))
            combo_nivel.grid(row=6, column=1, padx=10, pady=5)

            btn_completar = tk.Button(root2, text="Modificar", command=editar)
            btn_completar.grid(row=7, column=0, padx=10, pady=10)
            combo_nivel.set(nivel)

            btn_salir = tk.Button(root2, text="Cancelar", command=salir)
            btn_salir.grid(row=7, column=1, padx=10, pady=10)
            break

    root.destroy()

def eliminarUsuario(id, actualizar_lista_wrapper):
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    while True:
        numero = simpledialog.askinteger("Entrada", "Ingrese el ID del usuario a Eliminar:")
        if numero is None:
            break
        elif not usu.buscarUsuarioid(numero):  # Aquí puedes agregar cualquier condición de validación que necesites
            messagebox.showerror("Error", "El usuario buscado no existe.")
        else:
            usu.eliminarUsuario(numero,id)
            actualizar_lista_wrapper()
            break
    root.destroy()


def menuprincipal(ventana, nivel, id):
    ventana.destroy()
    import MenuPrincipal as mp
    mp.main(nivel, id)

def mostrar_detalles(event):
    seleccion = lista_usuarios.curselection()
    if seleccion:
        indice = seleccion[0]
        detalles = usu.listaUsuaros[indice]
        detalles_str = (
            f"Id: {detalles.getid()}\n"
            f"Nombre: {detalles.getnombre()}\n"
            f"Apellido Paterno: {detalles.getapaterno()}\n"
            f"Apellido Materno: {detalles.getamaterno()}\n"
            f"Teléfono: {detalles.gettelefono()}\n"
            f"Usuario: {detalles.getusuario()}\n"
            f"Contraseña: {detalles.getpsw()}\n"
            f"Nivel: {detalles.getnivel()}"
        )
        messagebox.showinfo("Detalles del Producto", detalles_str)

def actualizar_lista(lista_usuarios):
    lista_usuarios.delete(0, tk.END)
    if usu.is_empty():
        lista_usuarios.insert(tk.END, "No existe ningún usuario registrado")
    else:
        for registro in usu.listaUsuaros:
            if registro.getstatus() == 1:
                lista_usuarios.insert(tk.END, str(registro))

def main(nivel, id):
    def actualizar_lista_wrapper():
        actualizar_lista(lista_usuarios)

    ventana = tk.Tk()
    ventana.title("Registro de actividades")
    ventana.geometry("600x400")

    frame_izquierdo = tk.Frame(ventana)
    frame_izquierdo.pack(side=tk.LEFT, padx=10, pady=10)

    boton_crear_usuario = tk.Button(frame_izquierdo, text="Crear Usuario",
                                     command=lambda: crearUsuario(id, actualizar_lista_wrapper))
    boton_crear_usuario.pack(pady=5)

    boton_editar_usuario = tk.Button(frame_izquierdo, text="Editar Usuario",
                                    command=lambda: editarUsuario(id,actualizar_lista_wrapper))
    boton_editar_usuario.pack(pady=5)

    boton_eliminar = tk.Button(frame_izquierdo, text="Eliminar Usuario" ,
                                     command=lambda: eliminarUsuario(id, actualizar_lista_wrapper))
    boton_eliminar.pack(pady=5)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Regresar al Menú Principal",
                                     command=lambda: menuprincipal(ventana, nivel, id))
    boton_menu_principal.pack(pady=5)

    frame_derecho = tk.Frame(ventana)
    frame_derecho.pack(side=tk.RIGHT, padx=10, pady=10)

    global lista_usuarios
    lista_usuarios = tk.Listbox(frame_derecho, width=80, height=20)
    lista_usuarios.pack()
    lista_usuarios.bind('<<ListboxSelect>>', mostrar_detalles)

    actualizar_lista(lista_usuarios)
    ventana.mainloop()

