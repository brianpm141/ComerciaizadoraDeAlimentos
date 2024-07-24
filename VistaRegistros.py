import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Clases import Registros as reg


def menuprincipal(ventana, nivel, id):
    ventana.destroy()
    import MenuPrincipal as mp
    mp.main(nivel, id)


def mostrar_detalles(event):
    from Clases import Usuarios as us
    seleccion = lista_registros.curselection()
    if seleccion:
        indice = seleccion[0]
        detalles = reg.lista_registros[indice]
        id_buscar= detalles.getid_usuario()
        detalles_str = f"Fecha: {detalles.getfecha()}\nhora: {detalles.gethora()}\nid_usuario que realizo la accion: {us.getnombre_usuario(id_buscar)}\nMovimiento: {detalles.gettipomov()}\nid del movimiento: {detalles.getid_mov()}"
        messagebox.showinfo("Detalles del Producto", detalles_str)


def actualizar_lista(lista_registros):
    lista_registros.delete(0, tk.END)
    if reg.is_empty():
        lista_registros.insert(tk.END, "No se han registrado movimientos")
    else:
        for registro in reg.lista_registros:
            lista_registros.insert(tk.END, str(registro))


def main(nivel, id):

    def actualizar_lista_wrapper():
        actualizar_lista(lista_registros)

    ventana = tk.Tk()
    ventana.title("Registro de actividades")
    ventana.geometry("600x400")

    frame_izquierdo = tk.Frame(ventana)
    frame_izquierdo.pack(side=tk.LEFT, padx=10, pady=10)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Regresar al Menú Principal",
                                     command=lambda: menuprincipal(ventana, nivel, id))
    boton_menu_principal.pack(pady=5)

    frame_derecho = tk.Frame(ventana)
    frame_derecho.pack(side=tk.RIGHT, padx=10, pady=10)

    global lista_registros
    lista_registros = tk.Listbox(frame_derecho, width=80, height=20)
    lista_registros.pack()
    lista_registros.bind('<<ListboxSelect>>', mostrar_detalles)

    actualizar_lista(lista_registros)
    ventana.mainloop()