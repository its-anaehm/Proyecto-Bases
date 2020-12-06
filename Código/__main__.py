from Core.LoginGUI import LoginGUI
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


top = Tk()
top.title("Picasso")
top.resizable(0,0)


filename = PhotoImage(file = "Core/Logo-Bases.png")
logo = PhotoImage(file="Core/LogoProyecto.png")

C = Canvas(top, bg="blue", height=filename.height(), width=filename.width())
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

top.iconphoto(False,logo)

def goToDraw():
    top.destroy()
    LoginGUI()

ttk.Button(top, text="Login", padding=15, command=goToDraw ).pack(pady=40)

top.mainloop()