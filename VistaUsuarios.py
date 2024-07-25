import tkinter as tk
from tkinter import messagebox
from Clases import Usuarios as usu


def crearUsuario(id):
    print("holi")


def editarUsuario(id):
    print("edicion usuario")

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
                                     command=lambda: crearUsuario(id))
    boton_crear_usuario.pack(pady=5)

    boton_editar_usuario = tk.Button(frame_izquierdo, text="Editar Usuario",
                                    command=lambda: editarUsuario(id))
    boton_editar_usuario.pack(pady=5)


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


main(3, 1)