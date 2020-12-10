import tkinter
from tkinter import TkVersion, ttk
from tkinter import Tk
from typing import ValuesView

class BinnacleGUI(ttk.Frame):
    def __init__(self, parent, sgbd):
        super().__init__(parent)
        self.sgbd = sgbd

        self.pack()

        ttk.Label(self,text="Events in Binnable", font=('Kollektif', '30', 'normal')).pack()

        self.treeView = ttk.Treeview(self,columns=(0,1,2,3), show="headings", height="5")
        self.treeView.heading(0, text="User")
        self.treeView.heading(1, text="Event")
        self.treeView.heading(2, text="Date")
        self.treeView.heading(3, text="Time")
        self.treeView.pack()

        self.fillTreeView()

    def fillTreeView(self):
        for draw in self.sgbd.retrieveBinnacleInfo():
            self.treeView.insert('','end',values=draw)

