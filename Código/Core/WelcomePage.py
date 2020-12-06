from tkinter import Canvas, Image, PhotoImage, ttk
import tkinter
from tkinter.constants import NW
from tkinter.ttk import Style
from .LoginGUI import LoginGUI

class WelcomeGUI(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.pack()
        


    def goToLoginPage(self):
        self.destroy()
        LoginGUI(self.master)






