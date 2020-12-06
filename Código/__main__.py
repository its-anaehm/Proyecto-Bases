from Core.WelcomePage import *
from tkinter import Tk
from tkinter import PhotoImage

root = Tk()
root.title("Picasso")
photo = PhotoImage(file="Core/Logo-Bases.png")
root.iconphoto(False,photo)
welcome = WelcomeGUI(root)
root.resizable(0,0)
root.mainloop()

