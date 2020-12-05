from Core.WelcomePage import *
from tkinter import Tk
from tkinter import PhotoImage

root = Tk()
root.title("Picasso")
photo = PhotoImage(file="Core/piolin.png")
root.iconphoto(False,photo)
welcome = WelcomeGUI(root)
root.resizable(0,0)
root.mainloop()

