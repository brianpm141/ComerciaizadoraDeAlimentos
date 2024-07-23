import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


def solicitar_numero():
    def confirmar():
        try:
            valor = int(entry.get())
            messagebox.showinfo("Éxito", f"Número introducido: {valor}")
            dialog.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número válido.")

    def cancelar():
        dialog.destroy()

    dialog = tk.Tk()
    dialog.title("Introduce un número")

    label = tk.Label(dialog, text="Por favor, introduce el id a modificar:")
    label.pack(padx=20, pady=10)

    entry = tk.Entry(dialog)
    entry.pack(padx=20, pady=10)

    button_frame = tk.Frame(dialog)
    button_frame.pack(padx=20, pady=10)

    confirmar_button = tk.Button(button_frame, text="Confirmar", command=confirmar)
    confirmar_button.grid(row=0, column=0, padx=10)

    cancelar_button = tk.Button(button_frame, text="Cancelar", command=cancelar)
    cancelar_button.grid(row=0, column=1, padx=10)

    dialog.mainloop()


# Llama a la función para mostrar la ventana emergente
solicitar_numero()
