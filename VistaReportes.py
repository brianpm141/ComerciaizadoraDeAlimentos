import tkinter as tk

def on_pdf(clase_reporte):
    if clase_reporte == 1:
        print("reporte ventas")
    elif clase_reporte == 2:
        print("reporte pedidos")
    elif clase_reporte == 3:
        print("reporte inventarios")
    else:
        print("reporte movimientos")

def on_csv(clase_reporte):
    if clase_reporte == 1:
        print("reporte ventas")
    elif clase_reporte == 2:
        print("reporte pedidos")
    elif clase_reporte == 3:
        print("reporte inventarios")
    else:
        print("reporte movimientos")
def on_excel(clase_reporte):
    if clase_reporte == 1:
        print("reporte ventas")
    elif clase_reporte == 2:
        print("reporte pedidos")
    elif clase_reporte == 3:
        print("reporte inventarios")
    else:
        print("reporte movimientos")
def on_cancel(root2):
    root2.destroy()

def selectorTipo(clase_reporte):
    root2 = tk.Tk()
    root2.title("Seleccionar Tipo de Archivo")

    # Crear los botones
    btn_pdf = tk.Button(root2, text="PDF", command=lambda:on_pdf(clase_reporte))
    btn_pdf.pack(padx=10, pady=5)

    btn_csv = tk.Button(root2, text="CSV", command=lambda:on_csv(clase_reporte))
    btn_csv.pack(padx=10, pady=5)

    btn_excel = tk.Button(root2, text="Excel", command=lambda:on_excel(clase_reporte))
    btn_excel.pack(padx=10, pady=5)

    btn_cancel = tk.Button(root2, text="Salir", command=lambda:on_cancel(root2))
    btn_cancel.pack(padx=10, pady=5)

    # Ejecutar el bucle principal de la ventana
    root2.mainloop()

def salir(ventana,nivel,id):
    ventana.destroy()
    import MenuPrincipal as mp
    mp.main(nivel,id)


def main(nivel,id):
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Generador de Reportes")
    root.geometry("300x250")

    # Crear y colocar los botones en la ventana
    btn_reporte_ventas = tk.Button(root, text="Generar Reporte de Ventas", command=lambda:selectorTipo(1))
    btn_reporte_ventas.pack(pady=10)

    btn_reporte_pedidos = tk.Button(root, text="Generar Reporte de Pedidos", command=lambda:selectorTipo(2))
    btn_reporte_pedidos.pack(pady=10)

    btn_reporte_inventarios = tk.Button(root, text="Generar Reporte de Inventarios", command=lambda:selectorTipo(3))
    btn_reporte_inventarios.pack(pady=10)

    btn_reporte_movimientos = tk.Button(root, text="Generar Reporte de Movimientos", command=lambda:selectorTipo(4))
    btn_reporte_movimientos.pack(pady=10)

    btnsalir = tk.Button(root, text="Salir al menu principal", command=lambda:salir(root,nivel,id))
    btnsalir.pack(pady=10)

    root.mainloop()
