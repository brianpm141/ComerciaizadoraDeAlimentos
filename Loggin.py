import tkinter as tk
from tkinter import messagebox
from Clases import Usuarios as usr
import MenuPrincipal as mp


def login(entry_usuario,entry_psw,ventana):
    usuario = entry_usuario.get()
    psw = entry_psw.get()
    pswaux,nivel,id = usr.buscarUsuario(usuario)

    if not usuario or not psw:
        messagebox.showerror("Error", "¡Introduce nombre de usuario y contraseña!")
    elif psw is None or psw != pswaux:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    elif psw == pswaux:
        ventana.destroy()
        mp.main(nivel,id)

def main():
    ventana = tk.Tk()
    ventana.title("Inicio de Sesión")
    ventana.geometry("300x200")
    ventana.lift()
    ventana.attributes('-topmost', True)

    label_usuario = tk.Label(ventana, text="Usuario:")
    label_usuario.pack(pady=5)
    entry_usuario = tk.Entry(ventana)
    entry_usuario.pack(pady=5)

    label_psw = tk.Label(ventana, text="Contraseña:")
    label_psw.pack(pady=5)
    entry_psw = tk.Entry(ventana, show="*")
    entry_psw.pack(pady=5)


    btn_ac = tk.Button(ventana, text="Accept",command=lambda:login(entry_usuario,entry_psw,ventana))
    btn_ac.pack(pady=20)

    ventana.mainloop()
