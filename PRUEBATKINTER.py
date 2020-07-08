import tkinter as Tk
from tkinter import *
from tkinter import ttk

class formwindow_iniciarSesion:
    ventana = Tk()
    ventana.title("Iniciar sesion")
    ventana.geometry("325x200")
    usernameLABEL = Label(ventana, text="Nombre de usuario:").place(x=10,y=10)
    usernameENTRY = Entry(ventana, bg = "white", width = 20).place(x=10,y=30)
    passwordLABEL = Label(ventana, text="Clave:").place(x=10,y=60)
    passwordENTRY = Entry(ventana, bg = "white", width = 20, show = "*").place(x=10,y=80)
    serverLABEL = Label(ventana, text="Servidor:").place(x=10,y=110)
    serverENTRY = Entry(ventana, bg = "white", width = 15).place(x=10,y=130)
    portLABEL = Label(ventana,text="Puerto:").place(x=140,y=130)
    portENTRY = Entry(ventana, bg = "white", width = 15).place(x = 185,y = 130)
    loginBUTTON = Button(ventana, text="Iniciar Sesion").place(x=10,y=170)
