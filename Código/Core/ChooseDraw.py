#-*- coding:utf8 -*-
import tkinter
from tkinter import TkVersion, ttk
from tkinter import Tk
from typing import ValuesView

class ChooseDraw(ttk.Frame):
    """
    GUI que muestra datos de los dibujos
    """
    def __init__(self, parent, sgbd, function=None):
        super().__init__(parent)
        self.sgbd = sgbd
        self.pack()

        if function:
            self.master.title(function)

        ttk.Label(self,text="Choose a draw", font=('Times', '30', 'normal')).pack()

        self.treeView = ttk.Treeview(self,columns=(0,1,2,3), show="headings", height="5")
        self.treeView.heading(0, text="Id")
        self.treeView.heading(1, text="Name")
        self.treeView.heading(2, text="Date")
        self.treeView.heading(3, text="Time")
        self.treeView.pack()

        self.fillTreeView()

        ttk.Button(self,text="Choose Draw",command=self.getSelected).pack()
    
    def fillTreeView(self):
        print(self.sgbd.retrieveDraws())
        for draw in self.sgbd.retrieveDraws():
            self.treeView.insert('','end',values=draw)

    def getSelected(self):
        self.itemID = self.treeView.item(self.treeView.selection()[0])["values"][0]
        self.master.quit()
