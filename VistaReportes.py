import tkinter as tk
import Clases.Ventas as vnt
import Clases.Pedidos as ped
import Clases.Productos as prod
import Clases.Registros as mov
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename


def seleccionar_ruta_guardado(tipo_archivo):
    # Ocultar la ventana principal de Tkinter
    root = Tk()
    root.withdraw()

    # Definir las extensiones y filtros según el tipo de archivo
    if tipo_archivo == 1:
        extension = ".csv"
        filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
    elif tipo_archivo == 2:
        extension = ".pdf"
        filetypes = [("PDF files", "*.pdf"), ("All files", "*.*")]
    elif tipo_archivo == 3:
        extension = ".xlsx"
        filetypes = [("Excel files", "*.xlsx"), ("All files", "*.*")]
    else:
        raise ValueError("Tipo de archivo no válido. Usa 1 para CSV, 2 para PDF, o 3 para Excel.")

    # Abrir la ventana de diálogo para seleccionar la ubicación del archivo
    file_path = asksaveasfilename(
        defaultextension=extension,
        filetypes=filetypes,
        title="Guardar archivo"
    )

    # Retornar la ruta seleccionada
    return file_path


def on_pdf(clase_reporte,ventana):
    if clase_reporte == 1:
        ruta = seleccionar_ruta_guardado(2)
        vnt.generar_pdf(ruta)
        ventana.destroy()
    elif clase_reporte == 2:
        ruta = seleccionar_ruta_guardado(2)
        ped.generar_pdf(ruta)
        ventana.destroy()
    elif clase_reporte == 3:
        ruta = seleccionar_ruta_guardado(2)
        prod.generar_pdf(ruta)
        ventana.destroy()
    elif clase_reporte == 4:
        ruta = seleccionar_ruta_guardado(2)
        mov.generar_pdf(ruta)
        ventana.destroy()


def on_csv(clase_reporte,ventana):
    if clase_reporte == 1:
        ruta = seleccionar_ruta_guardado(1)
        vnt.generarcsv(ruta)
        ventana.destroy()
    elif clase_reporte == 2:
        ruta = seleccionar_ruta_guardado(1)
        ped.generarcsv(ruta)
        ventana.destroy()
    elif clase_reporte == 3:
        ruta = seleccionar_ruta_guardado(1)
        prod.generarcsv(ruta)
        ventana.destroy()
    elif clase_reporte == 4:
        ruta = seleccionar_ruta_guardado(1)
        mov.generarcsv(ruta)
        ventana.destroy()


def on_excel(clase_reporte,ventana):
    if clase_reporte == 1:
        ruta = seleccionar_ruta_guardado(3)
        vnt.gengerarexel(ruta)
        ventana.destroy()
    elif clase_reporte == 2:
        ruta = seleccionar_ruta_guardado(3)
        ped.gengerarexel(ruta)
        ventana.destroy()
    elif clase_reporte == 3:
        ruta = seleccionar_ruta_guardado(3)
        prod.generarexel(ruta)
        ventana.destroy()
    elif clase_reporte == 4:
        ruta = seleccionar_ruta_guardado(3)
        mov.generarexel(ruta)
        ventana.destroy()


def on_cancel(root2):
    root2.destroy()

def selectorTipo(clase_reporte):
    root2 = tk.Tk()
    root2.title("Seleccionar Tipo de Archivo")

    # Crear los botones
    btn_pdf = tk.Button(root2, text="PDF", command=lambda:on_pdf(clase_reporte,root2))
    btn_pdf.pack(padx=10, pady=5)

    btn_csv = tk.Button(root2, text="CSV", command=lambda:on_csv(clase_reporte,root2))
    btn_csv.pack(padx=10, pady=5)

    btn_excel = tk.Button(root2, text="Excel", command=lambda:on_excel(clase_reporte,root2))
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