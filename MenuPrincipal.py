import tkinter as tk
from tkinter import messagebox
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename


def menu_ventas(nivel, ventana,id):
    import Clases.Productos as prod
    if prod.is_empty():
        messagebox.showerror("Cuidado...","No se pueden realizar ventas sin ningun producto registrado")
    else:
        ventana.destroy()
        import VistaVentas as vv
        vv.main(nivel, id)


def menu_inventarios(nivel, ventana,id):
    ventana.destroy()
    import VistaProductos as vp
    vp.main(nivel,id)


def generacion_reportes(nivel,ventana, id):
    ventana.destroy()
    import VistaReportes as vrp
    vrp.main(nivel,id)


def gestion_usuarios(nivel,ventana, id):
    ventana.destroy()
    import VistaUsuarios as vu
    vu.main(nivel, id)


def gestion_clientes(nivel,ventana, id):
    ventana.destroy()
    import VistaClientes as vc
    vc.main(nivel, id)


def registro_actividades(nivel, ventana, id):
    ventana.destroy()
    import VistaRegistros as vr
    vr.main(nivel, id)


def cerrar_sesion(ventana):
    import Loggin as lg  # Importación dentro de la función para evitar importación circular
    messagebox.showinfo("Cerrar Sesión", "Has cerrado sesión.")
    ventana.destroy()
    lg.main()


def salir(ventana):
    messagebox.showinfo("Adios", "Saliendo....")
    ventana.destroy()


def main(nivel,id):
    ventana = tk.Tk()
    ventana.title("Menú de Opciones")
    ventana.geometry("300x400")

    btn_menu_ventas = tk.Button(ventana, text="Menú de Ventas", command=lambda: menu_ventas(nivel, ventana,id))
    btn_menu_ventas.pack(pady=10)

    btn_menu_inventarios = tk.Button(ventana, text="Menú de Inventarios",
                                     command=lambda: menu_inventarios(nivel, ventana,id))
    btn_menu_inventarios.pack(pady=10)

    if nivel >= 2:
        btn_generacion_reportes = tk.Button(ventana, text="Generación de Reportes", command=lambda:generacion_reportes(nivel,ventana,id))
        btn_generacion_reportes.pack(pady=10)

    if nivel == 3:
        btn_gestion_usuarios = tk.Button(ventana, text="Gestión de Usuarios", command=lambda:gestion_usuarios(nivel, ventana,id))
        btn_gestion_usuarios.pack(pady=10)

    btn_gestion_clientes = tk.Button(ventana, text="Gestión de Clientes", command=lambda:gestion_clientes(nivel, ventana,id))
    btn_gestion_clientes.pack(pady=10)

    if nivel == 3:
        btn_registro_actividades = tk.Button(ventana, text="Registro de Actividades",
                                             command=lambda : registro_actividades(nivel, ventana, id))
        btn_registro_actividades.pack(pady=10)

    btn_cerrar_sesion = tk.Button(ventana, text="Cerrar Sesión", command=lambda: cerrar_sesion(ventana))
    btn_cerrar_sesion.pack(pady=10)

    btn_salir = tk.Button(ventana, text="Salir", command=lambda: salir(ventana))
    btn_salir.pack(pady=10)

    ventana.mainloop()

