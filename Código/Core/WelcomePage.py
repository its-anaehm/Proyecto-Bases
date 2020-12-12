#-*- coding:utf8 -*-
from tkinter import ttk

from .LoginGUI import LoginGUI


class WelcomeGUI(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.pack()
        

    """
    Ejecuta la ventana de inicio de Sesión.
    """
    def goToLoginPage(self):
        self.destroy()
        LoginGUI(self.master)






