import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import Productos as pr


def formulario_productos(actualizar_lista_callback):
    tipo_dict = {
        "Perros": 1,
        "Gatos": 2,
        "Canarios": 3
    }

    def salir():
        root.destroy()

    def completar():
        nombre = entry_nombre.get()
        tipo = combo_tipo.get()
        peso = entry_peso.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()

        def es_entero(valor):
            try:
                int(valor)
                return True
            except ValueError:
                return False

        if not nombre or not tipo or not peso or not precio or not cantidad:
            messagebox.showerror("Error", "¡Introduce todos los campos!")
        elif not es_entero(peso):
            messagebox.showerror("Error", "¡Introduce un numero en peso!")
        elif not es_entero(precio):
            messagebox.showerror("Error", "¡Introduce un numero en precio!")
        elif not es_entero(cantidad):
            messagebox.showerror("Error", "¡Introduce un numero en cantidad!")
        elif not tipo:
            messagebox.showerror("Error", "¡Seleccione el tipo de aliento que es!")
        else:
            pr.crear_Producto(nombre, tipo, peso, precio, cantidad)
            actualizar_lista_callback()  # Llama a la función de actualización
            root.destroy()

    root = tk.Tk()
    root.title("Formulario de Productos")

    tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Tipo:").grid(row=1, column=0, padx=10, pady=5)
    combo_tipo = ttk.Combobox(root, values=list(tipo_dict.keys()))
    combo_tipo.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Peso:").grid(row=2, column=0, padx=10, pady=5)
    entry_peso = tk.Entry(root)
    entry_peso.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Precio:").grid(row=3, column=0, padx=10, pady=5)
    entry_precio = tk.Entry(root)
    entry_precio.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Cantidad:").grid(row=4, column=0, padx=10, pady=5)
    entry_cantidad = tk.Entry(root)
    entry_cantidad.grid(row=4, column=1, padx=10, pady=5)

    btn_completar = tk.Button(root, text="Registrar", command=completar)
    btn_completar.grid(row=5, column=0, padx=10, pady=10)

    btn_salir = tk.Button(root, text="Calncelar", command=salir)
    btn_salir.grid(row=5, column=1, padx=10, pady=10)
    root.mainloop()


def menuprincipal(ventana,nivel):
    import MenuPrincipal as mp
    ventana.destroy()
    mp.main(nivel)


def actualizar_lista(lista_productos):
    # Actualiza la lista de productos en la interfaz
    lista_productos.delete(0, tk.END)
    if pr.is_empty():
        lista_productos.insert(tk.END, "No existe ningun producto registrado")
    else:
        for producto in pr.lista_produtos:
            lista_productos.insert(tk.END, str(producto))

def eliminar_prod():
    def solicitar_numero():
        def confirmar():
            try:
                valor = int(entry.get())
                messagebox.showinfo("Éxito", f"Número introducido: {valor}")
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, introduce un número válido.")

        def cancelar():
            dialog.destroy()

        dialog = tk.Tk()
        dialog.title("Introduce un número")

        label = tk.Label(dialog, text="Por favor, introduce el id a modificar:")
        label.pack(padx=20, pady=10)

        entry = tk.Entry(dialog)
        entry.pack(padx=20, pady=10)

        button_frame = tk.Frame(dialog)
        button_frame.pack(padx=20, pady=10)

        confirmar_button = tk.Button(button_frame, text="Confirmar", command=confirmar)
        confirmar_button.grid(row=0, column=0, padx=10)

        cancelar_button = tk.Button(button_frame, text="Cancelar", command=cancelar)
        cancelar_button.grid(row=0, column=1, padx=10)

        dialog.mainloop()

    # Llama a la función para mostrar la ventana emergente
    print()


def modificar_producto(ventana, nivel):
    print()

def main(nivel):

    def actualizar_lista_wrapper():
        actualizar_lista(lista_productos)

    ventana = tk.Tk()
    ventana.title("Gestión de Productos")
    ventana.geometry("600x400")

    frame_izquierdo = tk.Frame(ventana)
    frame_izquierdo.pack(side=tk.LEFT, padx=10, pady=10)

    boton_nuevo_producto = tk.Button(frame_izquierdo, text="Nuevo Producto", command=lambda: formulario_productos(actualizar_lista_wrapper))
    boton_nuevo_producto.pack(pady=5)

    if nivel >= 2:
        boton_menu_principal = tk.Button(frame_izquierdo, text="Editar Producto", command=lambda: modificar_producto(ventana,nivel))
        boton_menu_principal.pack(pady=5)

        boton_menu_principal = tk.Button(frame_izquierdo, text="Eliminar Producto",
                                         command=lambda: eliminar_prod())
        boton_menu_principal.pack(pady=5)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Regresar al Menú Principal",
                                     command=lambda: menuprincipal(ventana, nivel))
    boton_menu_principal.pack(pady=5)

    frame_derecho = tk.Frame(ventana)
    frame_derecho.pack(side=tk.RIGHT, padx=10, pady=10)

    lista_productos = tk.Listbox(frame_derecho, width=80, height=20)
    lista_productos.pack()

    actualizar_lista(lista_productos)
    ventana.mainloop()

main(2)
