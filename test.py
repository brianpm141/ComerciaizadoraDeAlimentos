import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Productos as pr



tipo_dict = {
    "Perros": 1,
    "Gatos": 2,
    "Canarios": 3
}

def salir():
    root.destroy()


# Función para completar el formulario
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
    else:
        pr.crear_Producto(nombre,tipo,peso,precio,cantidad)
        messagebox.showinfo("Datos ingresados",
                        f"Nombre: {nombre}\nTipo: {tipo}\nPeso: {peso}\nPrecio: {precio}\nCantidad: {cantidad}")
        root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Productos")

# Crear y ubicar los elementos del formulario
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

# Crear y ubicar los botones
btn_completar = tk.Button(root, text="Completar", command=completar)
btn_completar.grid(row=5, column=0, padx=10, pady=10)

btn_salir = tk.Button(root, text="Salir", command=salir)
btn_salir.grid(row=5, column=1, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()
