import tkinter as tk
from tkinter import messagebox

def menu_ventas(nivel,ventana):
    ventana.destroy()
    import VistaProductos as vv
    vv.main(nivel)

def menu_inventarios():
    messagebox.showinfo("Menú de Inventarios", "Aquí puedes gestionar los inventarios.")

def generacion_reportes():
    messagebox.showinfo("Generación de Reportes", "Aquí puedes generar reportes.")

def gestion_usuarios():
    messagebox.showinfo("Gestión de Usuarios", "Aquí puedes gestionar los usuarios.")

def gestion_clientes():
    messagebox.showinfo("Gestión de Clientes", "Aquí puedes gestionar los clientes.")

def registro_actividades():
    messagebox.showinfo("Registro de Actividades", "Aquí puedes registrar actividades.")

def cerrar_sesion(ventana):
    import Loggin as lg  # Importación dentro de la función para evitar importación circular
    ventana.destroy()
    messagebox.showinfo("Cerrar Sesión", "Has cerrado sesión.")
    lg.main()

def salir(ventana):
    ventana.destroy()
    messagebox.showinfo("Adios", "Saliendo....")


def main(nivel):
    ventana = tk.Tk()
    ventana.title("Menú de Opciones")
    ventana.geometry("300x400")

    btn_menu_ventas = tk.Button(ventana, text="Menú de Ventas", command=lambda:menu_ventas(nivel,ventana))
    btn_menu_ventas.pack(pady=10)

    btn_menu_inventarios = tk.Button(ventana, text="Menú de Inventarios", command=lambda:menu_inventarios)
    btn_menu_inventarios.pack(pady=10)

    if nivel >= 2:
        btn_generacion_reportes = tk.Button(ventana, text="Generación de Reportes", command=lambda:generacion_reportes)
        btn_generacion_reportes.pack(pady=10)

    if nivel == 3:
        btn_gestion_usuarios = tk.Button(ventana, text="Gestión de Usuarios", command=lambda:gestion_usuarios)
        btn_gestion_usuarios.pack(pady=10)

    btn_gestion_clientes = tk.Button(ventana, text="Gestión de Clientes", command=lambda:gestion_clientes)
    btn_gestion_clientes.pack(pady=10)

    if nivel == 3:
        btn_registro_actividades = tk.Button(ventana, text="Registro de Actividades", command=lambda:registro_actividades)
        btn_registro_actividades.pack(pady=10)

    btn_cerrar_sesion = tk.Button(ventana, text="Cerrar Sesión", command=lambda:cerrar_sesion(ventana))
    btn_cerrar_sesion.pack(pady=10)

    btn_salir = tk.Button(ventana, text="Salir", command=lambda:salir(ventana))
    btn_salir.pack(pady=10)

    ventana.mainloop()

