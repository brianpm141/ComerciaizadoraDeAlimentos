import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import Clases.Ventas as vnt
import Clases.Pedidos as ped
import Clases.Productos as prod
import Clases.Clientes as cli

def menuprincipal(ventana, nivel, id):
    ventana.destroy()
    import MenuPrincipal as mp
    mp.main(nivel, id)

def actualizar_lista(lista_aux, opcion, label):
    lista_aux.delete(0, tk.END)
    label.config(text=f"Se está mostrando: {opcion}")
    if opcion == "Ventas":
        if vnt.is_empty():
            lista_aux.insert(tk.END, "No existe ninguna venta registrada")
        else:
            for venta in vnt.listaVentas:
                lista_aux.insert(tk.END, str(venta))
    elif opcion == "Pedidos":
        if vnt.is_empty():
            lista_aux.insert(tk.END, "No existe ningún pedido registrado")
        else:
            for pedido in ped.listaPedidos:
                lista_aux.insert(tk.END, str(pedido))


def mostrar_detalles(event):
    print("hola mundo")



def nuevaVenta(id, actualizar_lista_callback):
    listaProductos = prod.lista_produtos
    root = tk.Tk()
    root.title("Carrito de Compras")

    carrito = {}  # Cambiado a un diccionario para almacenar la cantidad de cada producto
    subtotal = [0.0]  # Usamos una lista para permitir la modificación dentro de las funciones internas

    def adr_articulo():
        nueva_ventana = tk.Toplevel(root)
        nueva_ventana.title("Añadir Producto")

        # Lista de productos
        lista = tk.Listbox(nueva_ventana, width=100)
        for i, producto in enumerate(listaProductos):
            if producto.getstatus() == 1:
                lista.insert(i, str(producto))
        lista.pack(pady=5)

        # Cuadro de texto para cantidad
        label_cantidad = tk.Label(nueva_ventana, text="Cantidad:")
        label_cantidad.pack()
        entry_cantidad = tk.Entry(nueva_ventana)
        entry_cantidad.pack()

        def agregar_producto():
            try:
                cantidad = entry_cantidad.get()
                if not cantidad:
                    messagebox.showerror("Error", "Ingrese la cantidad de productos")
                    nueva_ventana.lift()
                else:
                    cantidad = int(cantidad)
                    index = lista.curselection()
                    if cantidad < 1:
                        messagebox.showerror("Error", "La cantidad debe ser mayor a 0")
                        nueva_ventana.lift()
                    elif not index:
                        messagebox.showerror("Error", "Debe de seleccionar un producto")
                        nueva_ventana.lift()
                    else:
                        producto = listaProductos[index[0]]
                        nombre = producto.nombre
                        precio = producto.precio
                        cantidad_disponible = producto.getcantidad()

                        if cantidad > cantidad_disponible:
                            messagebox.showerror("Error",
                                                 f"No hay suficiente stock. Solo hay {cantidad_disponible} unidades disponibles.")
                            nueva_ventana.lift()
                        else:
                            if nombre in carrito:
                                if carrito[nombre]['cantidad'] + cantidad > cantidad_disponible:
                                    messagebox.showerror("Error",
                                                         f"No hay suficiente stock. Solo hay {cantidad_disponible - carrito[nombre]['cantidad']} unidades disponibles adicionales.")
                                    nueva_ventana.lift()
                                    return
                                carrito[nombre]['cantidad'] += cantidad
                            else:
                                carrito[nombre] = {'id': producto.id, 'precio': precio, 'cantidad': cantidad}

                            subtotal[0] += precio * cantidad
                            actualizar_carrito()
                            nueva_ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        btn_agregar = tk.Button(nueva_ventana, text="Agregar al carrito", command=agregar_producto)
        btn_agregar.pack(pady=10)

        btn_cancelar = tk.Button(nueva_ventana, text="Cancelar", command=lambda: nueva_ventana.destroy())
        btn_cancelar.pack(pady=10)

    def actualizar_carrito():
        text_carrito.delete(1.0, tk.END)
        for producto, detalles in carrito.items():
            text_carrito.insert(tk.END,
                                f"{producto}: ${detalles['precio']:.2f} x {detalles['cantidad']} = ${detalles['precio'] * detalles['cantidad']:.2f}\n")
        label_subtotal.config(text=f"Subtotal: ${subtotal[0]:.2f}")

    def confirmar_compra():
        if not carrito:
            messagebox.showerror("Error", "El carrito está vacío")
        else:
            def confirmar():
                metodo_pago = combo_metodo_pago.get()
                id_producto = []
                cantidad = []
                for producto, detalles in carrito.items():
                    id_producto.append(detalles['id'])
                    cantidad.append(detalles['cantidad'])
                vnt.crearVenta(id, id, id_producto, cantidad, subtotal, metodo_pago)
                messagebox.showinfo("Confirmar", "Compra confirmada")
                root2.destroy()
                root.destroy()
                actualizar_lista_callback()  # Llamar a la función para actualizar la lista

            def cancelar():
                root2.destroy()

            root2 = tk.Toplevel(root)
            root2.title("Método de Pago")

            # Etiqueta y lista desplegable para método de pago
            label_metodo_pago = tk.Label(root2, text="Método de Pago:")
            label_metodo_pago.grid(column=0, row=0, padx=10, pady=10)
            combo_metodo_pago = ttk.Combobox(root2, values=["Tarjeta", "Efectivo"])
            combo_metodo_pago.grid(column=1, row=0, padx=10, pady=10)
            combo_metodo_pago.current(0)  # Seleccionar el primer elemento por defecto

            label_subtotal = tk.Label(root2, text=f"Subtotal: {subtotal[0]:.2f}")
            label_subtotal.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

            # Botón de confirmar
            button_confirmar = tk.Button(root2, text="Confirmar", command=confirmar)
            button_confirmar.grid(column=0, row=2, padx=10, pady=10)

            # Botón de cancelar
            button_cancelar = tk.Button(root2, text="Cancelar", command=cancelar)
            button_cancelar.grid(column=1, row=2, padx=10, pady=10)

            root2.mainloop()

    def cancelar():
        messagebox.showinfo("Cancelando", "Compra cancelada")
        root.destroy()

    # Frame para los productos en el carrito
    frame_carrito = tk.Frame(root)
    frame_carrito.pack(padx=10, pady=10)

    label_carrito = tk.Label(frame_carrito, text="Productos en el carrito:")
    label_carrito.pack(anchor="w")

    text_carrito = tk.Text(frame_carrito, height=10, width=50)
    text_carrito.pack()

    # Label para mostrar el subtotal
    label_subtotal = tk.Label(root, text="Subtotal: $0.00")
    label_subtotal.pack(pady=5)

    # Frame para los botones
    frame_botones = tk.Frame(root)
    frame_botones.pack(pady=10)

    boton_adr = tk.Button(frame_botones, text="Añadir Artículo", command=adr_articulo)
    boton_adr.grid(row=1, column=0, padx=5)

    boton_confirmar = tk.Button(frame_botones, text="Confirmar Compra", command=confirmar_compra)
    boton_confirmar.grid(row=1, column=1, padx=5, pady=5)

    boton_cancelar_compra = tk.Button(frame_botones, text="Cancelar", command=cancelar)
    boton_cancelar_compra.grid(row=1, column=2, padx=5, pady=5)

    root.mainloop()


def nuevoPedido(id, actualizar_lista_callback):
    listaProductos = prod.lista_produtos
    ListaClientes = cli.listaClientes

    root = tk.Tk()
    root.title("Carrito de Compras")

    carrito = {}  # Cambiado a un diccionario para almacenar la cantidad de cada producto
    subtotal = [0.0]  # Usamos una lista para permitir la modificación dentro de las funciones internas

    def adr_articulo():
        nueva_ventana = tk.Toplevel(root)
        nueva_ventana.title("Añadir Producto")

        # Lista de productos
        lista = tk.Listbox(nueva_ventana, width=100)
        for i, producto in enumerate(listaProductos):
            if producto.getstatus() == 1:
                lista.insert(i, str(producto))
        lista.pack(pady=5)

        # Cuadro de texto para cantidad
        label_cantidad = tk.Label(nueva_ventana, text="Cantidad:")
        label_cantidad.pack()
        entry_cantidad = tk.Entry(nueva_ventana)
        entry_cantidad.pack()

        def agregar_producto():
            try:
                cantidad = entry_cantidad.get()
                if not cantidad:
                    messagebox.showerror("Error", "Ingrese la cantidad de productos")
                    nueva_ventana.lift()
                else:
                    cantidad = int(cantidad)
                    index = lista.curselection()
                    if cantidad < 1:
                        messagebox.showerror("Error", "La cantidad debe ser mayor a 0")
                        nueva_ventana.lift()
                    elif not index:
                        messagebox.showerror("Error", "Debe de seleccionar un producto")
                        nueva_ventana.lift()
                    else:
                        producto = listaProductos[index[0]]
                        nombre = producto.nombre
                        precio = producto.precio

                        if nombre in carrito:
                            carrito[nombre]['cantidad'] += cantidad
                        else:
                            carrito[nombre] = {'id': producto.id, 'precio': precio, 'cantidad': cantidad}

                        subtotal[0] += precio * cantidad
                        actualizar_carrito()
                        nueva_ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        btn_agregar = tk.Button(nueva_ventana, text="Agregar al carrito", command=agregar_producto)
        btn_agregar.pack(pady=10)

        btn_cancelar = tk.Button(nueva_ventana, text="Cancelar", command=lambda: nueva_ventana.destroy())
        btn_cancelar.pack(pady=10)

    def actualizar_carrito():
        text_carrito.delete(1.0, tk.END)
        for producto, detalles in carrito.items():
            text_carrito.insert(tk.END,
                                f"{producto}: ${detalles['precio']:.2f} x {detalles['cantidad']} = ${detalles['precio'] * detalles['cantidad']:.2f}\n")
        label_subtotal.config(text=f"Subtotal: ${subtotal[0]:.2f}")

    def confirmar_compra(ventana):
        if not carrito:
            messagebox.showerror("Error", "El carrito está vacío")
            ventana.lift()
        else:
            def confirmar():
                metodo_pago = combo_metodo_pago.get()
                id_cliente = entry_id_cliente.get()
                fecha = entry_fecha.get_date().strftime("%Y-%m-%d")
                # Validar ID del cliente y fecha
                if not id_cliente:
                    messagebox.showerror("Error", "Ingrese el ID del cliente")
                    return
                if not fecha:
                    messagebox.showerror("Error", "Ingrese la fecha")
                    return
                if not cli.buscarClienteid(id_cliente):
                    messagebox.showerror("Error", "El cliente no exite")
                    return

                root2.lift()
                id_producto = []
                cantidad = []
                for producto, detalles in carrito.items():
                    id_producto.append(detalles['id'])
                    cantidad.append(detalles['cantidad'])
                ped.crearPedido(id, id_producto, cantidad,  subtotal, metodo_pago,"Pendiente", id_cliente, fecha)
                messagebox.showinfo("Confirmar", "Pedido confirmado")
                root2.destroy()
                root.destroy()
                actualizar_lista_callback()  # Llamar a la función para actualizar la lista

            def cancelar():
                root2.destroy()

            root2 = tk.Toplevel(root)
            root2.title("Método de Pago")

            # Etiqueta y lista desplegable para método de pago
            label_metodo_pago = tk.Label(root2, text="Método de Pago:")
            label_metodo_pago.grid(column=0, row=0, padx=10, pady=10)
            combo_metodo_pago = ttk.Combobox(root2, values=["Tarjeta", "Efectivo"])
            combo_metodo_pago.grid(column=1, row=0, padx=10, pady=10)
            combo_metodo_pago.current(0)  # Seleccionar el primer elemento por defecto

            # Etiqueta y campo para ID del cliente
            label_id_cliente = tk.Label(root2, text="ID del Cliente:")
            label_id_cliente.grid(column=0, row=1, padx=10, pady=10)
            entry_id_cliente = tk.Entry(root2)
            entry_id_cliente.grid(column=1, row=1, padx=10, pady=10)

            # Etiqueta y campo para fecha usando DateEntry
            label_fecha = tk.Label(root2, text="Fecha:")
            label_fecha.grid(column=0, row=2, padx=10, pady=10)
            entry_fecha = DateEntry(root2, date_pattern='yyyy-mm-dd')
            entry_fecha.grid(column=1, row=2, padx=10, pady=10)

            label_subtotal = tk.Label(root2, text=f"Subtotal: {subtotal[0]:.2f}")
            label_subtotal.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

            # Botón de confirmar
            button_confirmar = tk.Button(root2, text="Confirmar", command=lambda:confirmar())
            button_confirmar.grid(column=0, row=4, padx=10, pady=10)

            # Botón de cancelar
            button_cancelar = tk.Button(root2, text="Cancelar", command=cancelar)
            button_cancelar.grid(column=1, row=4, padx=10, pady=10)

            root2.mainloop()


    def cancelar():
        messagebox.showinfo("Cancelando", "Compra cancelada")
        root.destroy()

    # Frame para los productos en el carrito
    frame_carrito = tk.Frame(root)
    frame_carrito.pack(padx=10, pady=10)

    label_carrito = tk.Label(frame_carrito, text="Productos en el carrito:")
    label_carrito.pack(anchor="w")

    text_carrito = tk.Text(frame_carrito, height=10, width=50)
    text_carrito.pack()

    # Label para mostrar el subtotal
    label_subtotal = tk.Label(root, text="Subtotal: $0.00")
    label_subtotal.pack(pady=5)

    # Frame para los botones
    frame_botones = tk.Frame(root)
    frame_botones.pack(pady=10)

    boton_adr = tk.Button(frame_botones, text="Añadir Artículo", command=adr_articulo)
    boton_adr.grid(row=1, column=0, padx=5)

    boton_confirmar = tk.Button(frame_botones, text="Confirmar Pedido", command=lambda:confirmar_compra(root))
    boton_confirmar.grid(row=1, column=1, padx=5, pady=5)

    boton_cancelar_compra = tk.Button(frame_botones, text="Cancelar", command=cancelar)
    boton_cancelar_compra.grid(row=1, column=2, padx=5, pady=5)

    root.mainloop()


def compNuevaventa(id, actualizar_lista_callback):
    if prod.is_empty():
        messagebox.showerror("Advertencia","No hay productos registrados, imposible crear pedido")
    else:
        nuevaVenta(id, actualizar_lista_callback)


def compNuevopedido(id, actualizar_lista_callback):
    if cli.is_empty():
        messagebox.showerror("Advertencia", "No hay clientes registrados, imposible crear pedido")
    elif prod.is_empty():
        messagebox.showerror("Advertencia","No hay productos registrados, imposible crear pedido")
    else:
        nuevoPedido(id, actualizar_lista_callback)


def modPedido(id_ses):
    def mostrar_estado_pedido():
        id_pedido = entry_id.get()
        id_pedido = int(id_pedido)
        aux = ped.buscarPedido(id_pedido)
        if not id_pedido:
            messagebox.showerror("Error", "Ingrese el ID del pedido")
        elif aux != False:
            popup.withdraw()

            def guardar_estado():
                estado_seleccionado = estado_var.get()
                messagebox.showinfo("Estado Pedido", f"Pedido con ID: {id_pedido} ahora está {estado_seleccionado}")
                aux.actPedido(estado_seleccionado, id_ses)
                estado_popup.destroy()
                popup.destroy()

            estado_popup = tk.Toplevel(root5)
            estado_popup.title("Estado del Pedido")

            label_estado = tk.Label(estado_popup, text=f"Seleccione el estado para el pedido ID: {id_pedido}")
            label_estado.pack(pady=10)

            estado_var = tk.StringVar(estado_popup)
            estado_var.set("Pendiente")  # Valor predeterminado

            opciones_estado = ["Pendiente", "Completado", "Cancelado"]
            dropdown = tk.OptionMenu(estado_popup, estado_var, *opciones_estado)
            dropdown.pack(pady=5)

            btn_guardar = tk.Button(estado_popup, text="Guardar", command=guardar_estado)
            btn_guardar.pack(pady=5)
        else:
            messagebox.showerror("Error", "El pedido ingresado no existe")

    def cancelar():
        popup.destroy()

    # Crear la ventana principal
    root5 = tk.Tk()
    root5.withdraw()  # Ocultar la ventana principal

    # Crear la ventana emergente inicial
    popup = tk.Toplevel(root5)
    popup.title("Modificar Pedido")

    # Mensaje
    label = tk.Label(popup, text="Ingrese el ID del pedido:")
    label.pack(pady=10)

    # Caja de texto
    entry_id = tk.Entry(popup)
    entry_id.pack(pady=5)

    # Botones
    frame_buttons = tk.Frame(popup)
    frame_buttons.pack(pady=10)

    btn_modificar = tk.Button(frame_buttons, text="Modificar",command=mostrar_estado_pedido)
    btn_modificar.grid(row=0, column=0, padx=5)

    btn_cancelar = tk.Button(frame_buttons, text="Cancelar", command=cancelar)
    btn_cancelar.grid(row=0, column=1, padx=5)

    # Ejecutar la aplicación
    popup.mainloop()


def main(nivel, id):
    def actualizar_lista_wrapper(*args):
        actualizar_lista(lista_registros, opcion_var.get(), label_mostrando)

    ventana = tk.Tk()
    ventana.title("Menu de ventas")
    ventana.geometry("800x500")

    frame_izquierdo = tk.Frame(ventana)
    frame_izquierdo.pack(side=tk.LEFT, padx=10, pady=10)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Nueva venta",
                                     command=lambda: compNuevaventa(id, actualizar_lista_wrapper))
    boton_menu_principal.pack(pady=5)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Nuevo pedido",
                                     command=lambda: compNuevopedido(id, actualizar_lista_wrapper))
    boton_menu_principal.pack(pady=5)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Gestionar pedido",
                                     command=lambda:modPedido(id))
    boton_menu_principal.pack(pady=5)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Regresar al Menú Principal",
                                     command=lambda: menuprincipal(ventana, nivel, id))
    boton_menu_principal.pack(pady=5)

    frame_derecho = tk.Frame(ventana)
    frame_derecho.pack(side=tk.RIGHT, padx=10, pady=10)

    # Agregar el label que indica lo que se está mostrando
    label_mostrando = tk.Label(frame_derecho, text="Se está mostrando: Ventas")
    label_mostrando.pack(pady=5)

    # Agregar un selector de opciones
    opcion_var = tk.StringVar(ventana)
    opcion_var.set("Ventas")  # Valor por defecto
    opciones = ["Ventas", "Pedidos"]
    selector_opcion = tk.OptionMenu(frame_derecho, opcion_var, *opciones, command=actualizar_lista_wrapper)
    selector_opcion.pack(pady=5)

    global lista_registros
    lista_registros = tk.Listbox(frame_derecho, width=100, height=20)
    lista_registros.pack()

    lista_registros.bind('<<ListboxSelect>>', mostrar_detalles)

    actualizar_lista(lista_registros, opcion_var.get(), label_mostrando)
    ventana.mainloop()

main(1,1)