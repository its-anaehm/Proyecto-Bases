#-*- coding:utf8 -*-

from tkinter import ttk
from tkinter import *
import tkinter


class ChoseUserToAlterGUI(ttk.Frame):
    """
    GUI para seleccionar el usuario a alterar
    """
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.pack(padx=20, pady=20)
        self.master.title("Alter user")

        ttk.Label(self,text="Chose an User", font=('Times', '30', 'normal')).pack()

        self.userList = Listbox(self, selectmode=SINGLE)

        ttk.Button(self,text="Alter User", command=self.goToAlterUser)

    
    def goToAlterUser(self):
        """
        Toma los datos y envia al editor de usuario
        """

        name = self.userList.get(self.userList.curselection())
