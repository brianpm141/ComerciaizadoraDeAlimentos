import tkinter as tk
from tkinter import messagebox

def generar_reporte_ventas():
    messagebox.showinfo("Reporte", "Generando reporte de ventas...")

def generar_reporte_pedidos():
    messagebox.showinfo("Reporte", "Generando reporte de pedidos...")

def generar_reporte_movimientos():
    messagebox.showinfo("Reporte", "Generando reporte de movimientos...")

def generar_reporte_inventarios():
    messagebox.showinfo("Reporte", "Generando reporte de inventarios...")

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Reportes")
root.geometry("300x200")

# Crear y colocar los botones en la ventana
btn_reporte_ventas = tk.Button(root, text="Generar Reporte de Ventas", command=generar_reporte_ventas)
btn_reporte_ventas.pack(pady=10)

btn_reporte_pedidos = tk.Button(root, text="Generar Reporte de Pedidos", command=generar_reporte_pedidos)
btn_reporte_pedidos.pack(pady=10)

btn_reporte_movimientos = tk.Button(root, text="Generar Reporte de Movimientos", command=generar_reporte_movimientos)
btn_reporte_movimientos.pack(pady=10)

btn_reporte_inventarios = tk.Button(root, text="Generar Reporte de Inventarios", command=generar_reporte_inventarios)
btn_reporte_inventarios.pack(pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()
