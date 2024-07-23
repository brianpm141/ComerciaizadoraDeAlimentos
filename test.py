import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Clases import Registros as reg


def eliminar_prod():
    print("Eliminando...")


def menuprincipal():
    print("Menuprincipal")


def formulario_productos(id,actualizar_lista_wrapper):
    print()


def  modificar_producto(id,actualizar_lista_wrapper):
    print("hola")


def actualizar_lista(lista_registros):
    # Actualiza la lista de productos en la interfaz
    lista_registros.delete(0, tk.END)
    if reg.is_empty():
        lista_registros.insert(tk.END, "No existe ningún producto registrado")
    else:
        for registro in reg.lista_registros:
            lista_registros.insert(tk.END, str(registro))


def main(nivel,id):
    print(id)
    def actualizar_lista_wrapper():
        actualizar_lista(lista_productos)

    ventana = tk.Tk()
    ventana.title("Gestión de Productos")
    ventana.geometry("600x400")

    frame_izquierdo = tk.Frame(ventana)
    frame_izquierdo.pack(side=tk.LEFT, padx=10, pady=10)

    boton_nuevo_producto = tk.Button(frame_izquierdo, text="Nuevo Producto", command=lambda: formulario_productos(id,actualizar_lista_wrapper))
    boton_nuevo_producto.pack(pady=5)

    if nivel >= 2:
        boton_menu_principal = tk.Button(frame_izquierdo, text="Editar Producto", command=lambda: modificar_producto(id,actualizar_lista_wrapper))
        boton_menu_principal.pack(pady=5)

        boton_menu_principal = tk.Button(frame_izquierdo, text="Eliminar Producto",
                                         command=lambda: eliminar_prod(id,actualizar_lista_wrapper))
        boton_menu_principal.pack(pady=5)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Regresar al Menú Principal",
                                     command=lambda: menuprincipal(ventana, nivel,id))
    boton_menu_principal.pack(pady=5)

    frame_derecho = tk.Frame(ventana)
    frame_derecho.pack(side=tk.RIGHT, padx=10, pady=10)

    lista_productos = tk.Listbox(frame_derecho, width=80, height=20)
    lista_productos.pack()

    actualizar_lista(lista_productos)
    ventana.mainloop()


main(3,1)