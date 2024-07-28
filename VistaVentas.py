import tkinter as tk
import Clases.Ventas as vnt
import Clases.Pedidos as ped


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
                if venta.getstatus() == 1:
                    lista_aux.insert(tk.END, str(venta))
    elif opcion == "Pedidos":
        if vnt.is_empty():
            lista_aux.insert(tk.END, "No existe ningún pedido registrado")
        else:
            for pedido in ped.listaPedidos:
                if pedido.getstatus() == 1:
                    lista_aux.insert(tk.END, str(pedido))


def mostrar_detalles(event):
    print("hola mundo")


def main(nivel, id):

    def actualizar_lista_wrapper(*args):
        actualizar_lista(lista_registros, opcion_var.get(), label_mostrando)

    ventana = tk.Tk()
    ventana.title("Menu de ventas")
    ventana.geometry("800x500")

    frame_izquierdo = tk.Frame(ventana)
    frame_izquierdo.pack(side=tk.LEFT, padx=10, pady=10)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Nueva venta",
                                     command=lambda: menuprincipal(ventana, nivel, id))
    boton_menu_principal.pack(pady=5)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Nuevo pedido",
                                     command=lambda: menuprincipal(ventana, nivel, id))
    boton_menu_principal.pack(pady=5)

    boton_menu_principal = tk.Button(frame_izquierdo, text="Gestionar pedido",
                                     command=lambda: menuprincipal(ventana, nivel, id))
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


main(1, 2)
