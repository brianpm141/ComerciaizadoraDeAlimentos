import tkinter as tk
from tkinter import messagebox

def login():
    usuario = entry_usuario.get()
    psw = entry_psw.get()

    if usuario == "admin" and psw == "admin":
        messagebox.showinfo("Inicio de sesión", "¡Inicio de sesión exitoso!")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("300x200")


label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

label_psw = tk.Label(ventana, text="Contraseña:")
label_psw.pack(pady=5)
entry_psw = tk.Entry(ventana, show="*")
entry_psw.pack(pady=5)

btn_ac = tk.Button(ventana, text="Accept", command=login)
btn_ac.pack(pady=20)

ventana.mainloop()
