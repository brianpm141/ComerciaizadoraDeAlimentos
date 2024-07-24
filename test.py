def formulario_productos(id_usuario,actualizar_lista_callback):
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
            pr.crear_Producto(id_usuario,nombre, tipo, peso, precio, cantidad)
            actualizar_lista_callback()  # Llama a la función de actualización
            root.destroy()

    root = tk.Toplevel()
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

    btn_salir = tk.Button(root, text="Cancelar", command=salir)
    btn_salir.grid(row=5, column=1, padx=10, pady=10)

