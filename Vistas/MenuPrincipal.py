import tkinter as tk
from tkinter import messagebox


def menu_ventas(nivel, ventana, id):
    import Clases.Productos as prod
    if prod.is_empty():
        messagebox.showerror(
            "Cuidado...", "No se pueden realizar ventas sin ningun producto registrado")
    else:
        ventana.destroy()
        import Vistas.VistaVentas as vv
        vv.main(nivel, id)


def menu_inventarios(nivel, ventana, id):
    ventana.destroy()
    import Vistas.VistaProductos as vp
    vp.main(nivel, id)


def generacion_reportes(nivel, ventana, id):
    ventana.destroy()
    import Vistas.VistaReportes as vrp
    vrp.main(nivel, id)


def gestion_usuarios(nivel, ventana, id):
    ventana.destroy()
    import Vistas.VistaUsuarios as vu
    vu.main(nivel, id)


def gestion_clientes(nivel, ventana, id):
    ventana.destroy()
    import Vistas.VistaClientes as vc
    vc.main(nivel, id)


def registro_actividades(nivel, ventana, id):
    ventana.destroy()
    import Vistas.VistaRegistros as vr
    vr.main(nivel, id)


def cerrar_sesion(ventana):
    import Vistas.Loggin as lg
    messagebox.showinfo("Cerrar Sesión", "Has cerrado sesión.")
    ventana.destroy()
    lg.main()


def salir(ventana):
    messagebox.showinfo("Adios", "Saliendo....")
    ventana.destroy()


def main(nivel, id):
    ventana = tk.Tk()
    ventana.title("Menú de Opciones")
    ventana.geometry("580x200")

    # Definir el tamaño uniforme para los botones
    btn_width = 20  # Ancho del botón
    btn_height = 2  # Alto del botón

    btn_menu_ventas = tk.Button(
        ventana, text="Menú de Ventas", width=btn_width, height=btn_height,
        command=lambda: menu_ventas(nivel, ventana, id))
    btn_menu_ventas.grid(row=0, column=0, pady=10)

    btn_menu_inventarios = tk.Button(
        ventana, text="Menú de Inventarios", width=btn_width, height=btn_height,
        command=lambda: menu_inventarios(nivel, ventana, id))
    btn_menu_inventarios.grid(row=0, column=1, pady=10)

    btn_gestion_clientes = tk.Button(
        ventana, text="Gestión de Clientes", width=btn_width, height=btn_height,
        command=lambda: gestion_clientes(nivel, ventana, id))
    btn_gestion_clientes.grid(row=0, column=2, pady=10)

    if nivel == 3:
        btn_gestion_usuarios = tk.Button(
            ventana, text="Gestión de Usuarios", width=btn_width, height=btn_height,
            command=lambda: gestion_usuarios(nivel, ventana, id))
        btn_gestion_usuarios.grid(row=0, column=3, pady=10)

    if nivel >= 2:
        btn_generacion_reportes = tk.Button(
            ventana, text="Generación de Reportes", width=btn_width, height=btn_height,
            command=lambda: generacion_reportes(nivel, ventana, id))
        btn_generacion_reportes.grid(row=1, column=1, pady=10)

    if nivel == 3:
        btn_registro_actividades = tk.Button(
            ventana, text="Registro de Actividades", width=btn_width, height=btn_height,
            command=lambda: registro_actividades(nivel, ventana, id))
        btn_registro_actividades.grid(row=1, column=2, pady=10)

    btn_cerrar_sesion = tk.Button(
        ventana, text="Cerrar Sesión", width=btn_width, height=btn_height,
        command=lambda: cerrar_sesion(ventana))
    btn_cerrar_sesion.grid(row=2, column=1, pady=10)

    btn_salir = tk.Button(
        ventana, text="Salir", width=btn_width, height=btn_height,
        command=lambda: salir(ventana))
    btn_salir.grid(row=2, column=2, pady=10)

    ventana.mainloop()


main(2, 2)
