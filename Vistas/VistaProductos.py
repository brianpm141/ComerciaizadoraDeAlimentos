import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Clases import Productos as pr


def formulario_productos(id_usuario, actualizar_lista_callback):
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

        # Validaciones
        if not nombre or not tipo or not peso or not precio or not cantidad:
            messagebox.showerror("Error", "¡Introduce todos los campos!")
            root.lift()
            root.attributes("-topmost", True)
            root.after_idle(root.attributes, "-topmost", False)
        elif len(nombre) > 40:
            messagebox.showerror("Error", "El nombre no puede tener más de 40 caracteres.")
            root.lift()
            root.attributes("-topmost", True)
            root.after_idle(root.attributes, "-topmost", False)
        elif not es_entero(precio) or len(precio) > 3:
            messagebox.showerror("Error", "El precio debe ser un numero menor a 999.")
            root.lift()
            root.attributes("-topmost", True)
            root.after_idle(root.attributes, "-topmost", False)
        elif not es_entero(peso) or len(peso) > 3:
            messagebox.showerror("Error", "El peso debe un numero menor a 999.")
            root.lift()
            root.attributes("-topmost", True)
            root.after_idle(root.attributes, "-topmost", False)
        elif not es_entero(cantidad) or len(cantidad) > 3:
            messagebox.showerror("Error", "La cantidad debe ser un numero menor a 999.")
            root.lift()
            root.attributes("-topmost", True)
            root.after_idle(root.attributes, "-topmost", False)
        elif tipo not in tipo_dict:
            messagebox.showerror("Error", "Debe seleccionar una categoría válida.")
            root.lift()
            root.attributes("-topmost", True)
            root.after_idle(root.attributes, "-topmost", False)
        else:
            # Si todas las validaciones pasan, registrar el producto
            messagebox.showinfo("Registro exitoso", "El producto se registro correctamente")
            pr.crear_Producto(id_usuario, nombre, tipo_dict[tipo], peso, precio, cantidad)
            actualizar_lista_callback()  # Llama a la función de actualización
            root.destroy()

    root = tk.Toplevel()
    root.title("Nuevo Producto")

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

    btn_salir = tk.Button(root, text="Cancelar", command=salir)
    btn_salir.grid(row=5, column=1, padx=10, pady=10)


def menuprincipal(ventana, nivel,id):
    ventana.destroy()
    import Vistas.MenuPrincipal as mp
    mp.main(nivel,id)

def actualizar_lista(lista_productos):
    # Actualiza la lista de productos en la interfaz
    lista_productos.delete(0, tk.END)
    if pr.is_empty():
        lista_productos.insert(tk.END, "No existe ningún producto registrado")
    else:
        for producto in pr.lista_produtos:
            if producto.getstatus() == 1:
                lista_productos.insert(tk.END, str(producto))

def eliminar_prod(id_usuario,actualizar_lista_wrapper):
    def confirmar():
        try:
            valor = int(entry.get())
            estado = pr.eliminar_producto(id_usuario,valor)
            if estado:
                messagebox.showinfo("Eliminado", "El producto fue eliminado exitosamente")
                actualizar_lista_wrapper()
            else:
                messagebox.showerror("Error", "El producto introducido no existe.")
            dialog.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número válido.")

    def cancelar():
        dialog.destroy()

    dialog = tk.Toplevel()
    dialog.title("Eliminar Producto")

    label = tk.Label(dialog, text="Por favor, introduce el id del producto que desea eliminar:")
    label.pack(padx=20, pady=10)

    entry = tk.Entry(dialog)
    entry.pack(padx=20, pady=10)

    button_frame = tk.Frame(dialog)
    button_frame.pack(padx=20, pady=10)

    confirmar_button = tk.Button(button_frame, text="Confirmar", command=confirmar)
    confirmar_button.grid(row=0, column=0, padx=10)

    cancelar_button = tk.Button(button_frame, text="Cancelar", command=cancelar)
    cancelar_button.grid(row=0, column=1, padx=10)

def modificar_producto(id_usuario,actualizar_lista_wrapper):
    def form_modific(prod):
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
            elif len(nombre) > 40:
                messagebox.showerror("Error", "El nombre no puede tener más de 40 caracteres.")
            elif not es_entero(precio) or len(precio) > 3:
                messagebox.showerror("Error", "El precio debe ser un numero menor a 999.")
            elif not es_entero(peso) or len(peso) > 3:
                messagebox.showerror("Error", "El peso debe un numero menor a 999.")
            elif not es_entero(cantidad) or len(cantidad) > 3:
                messagebox.showerror("Error", "La cantidad debe ser un numero menor a 999.")
            elif tipo not in tipo_dict:
                messagebox.showerror("Error", "Debe seleccionar una categoría válida.")
            else:
                prod.modificar_valores(id_usuario,nombre, tipo, peso, precio, cantidad)
                messagebox.showinfo("Modificado", "El producto fue modificado exitosamente")
                actualizar_lista_wrapper()
                root.destroy()

        root = tk.Toplevel()
        root.title("Modificar Producto")

        tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        entry_nombre = tk.Entry(root)
        entry_nombre.grid(row=0, column=1, padx=10, pady=5)
        entry_nombre.insert(0, prod.nombre)  # Prellenar con valor predeterminado

        tk.Label(root, text="Tipo:").grid(row=1, column=0, padx=10, pady=5)
        combo_tipo = ttk.Combobox(root, values=["Perros", "Gatos", "Canarios"])
        combo_tipo.grid(row=1, column=1, padx=10, pady=5)
        combo_tipo.set(prod.tipo)  # Prellenar con valor predeterminado

        tk.Label(root, text="Peso:").grid(row=2, column=0, padx=10, pady=5)
        entry_peso = tk.Entry(root)
        entry_peso.grid(row=2, column=1, padx=10, pady=5)
        entry_peso.insert(0, prod.peso)  # Prellenar con valor predeterminado

        tk.Label(root, text="Precio:").grid(row=3, column=0, padx=10, pady=5)
        entry_precio = tk.Entry(root)
        entry_precio.grid(row=3, column=1, padx=10, pady=5)
        entry_precio.insert(0, prod.precio)  # Prellenar con valor predeterminado

        tk.Label(root, text="Cantidad:").grid(row=4, column=0, padx=10, pady=5)
        entry_cantidad = tk.Entry(root)
        entry_cantidad.grid(row=4, column=1, padx=10, pady=5)
        entry_cantidad.insert(0, prod.cantidad)  # Prellenar con valor predeterminado

        btn_completar = tk.Button(root, text="Modificar", command=completar)
        btn_completar.grid(row=5, column=0, padx=10, pady=10)

        btn_salir = tk.Button(root, text="Cancelar", command=salir)
        btn_salir.grid(row=5, column=1, padx=10, pady=10)

    def confirmar():
        try:
            valor = int(entry.get())
            prod = pr.buscar_producto(valor)
            if prod is not None:
                dialog.destroy()
                form_modific(prod)
            else:
                messagebox.showerror("Error", "El producto introducido no existe.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número válido.")

    def cancelar():
        dialog.destroy()

    dialog = tk.Toplevel()
    dialog.title("Modificar Producto")

    label = tk.Label(dialog, text="Por favor, introduce el id del producto que desea modificar:")
    label.pack(padx=20, pady=10)

    entry = tk.Entry(dialog)
    entry.pack(padx=20, pady=10)

    button_frame = tk.Frame(dialog)
    button_frame.pack(padx=20, pady=10)

    confirmar_button = tk.Button(button_frame, text="Confirmar", command=confirmar)
    confirmar_button.grid(row=0, column=0, padx=10)

    cancelar_button = tk.Button(button_frame, text="Cancelar", command=cancelar)
    cancelar_button.grid(row=0, column=1, padx=10)

def main(nivel,id):
    def actualizar_lista_wrapper():
        actualizar_lista(lista_productos)

    ventana = tk.Tk()
    ventana.title("Gestión de Productos")
    ventana.geometry("650x400")

    frame_izquierdo = tk.Frame(ventana)
    frame_izquierdo.pack(side=tk.LEFT, padx=10, pady=10)

    if nivel >= 2:
        boton_nuevo_producto = tk.Button(frame_izquierdo, text="Nuevo Producto", command=lambda: formulario_productos(id,actualizar_lista_wrapper))
        boton_nuevo_producto.pack(pady=5)


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

