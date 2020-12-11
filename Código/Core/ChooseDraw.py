#-*- coding:utf8 -*-
import tkinter
from tkinter import TkVersion, ttk
from tkinter import Tk
from typing import ValuesView
from Core.Encryptor import Encryptor

"""
GUI que muestra los dibujos y permite realizar una selección.
@author mdgomeza@unah.hn
@version 2.0
"""
class ChooseDraw(ttk.Frame):
    """
    Constructor del objeto.
    @param parent: Objeto master del frame.
    @param sgbd: Objeto MySQLEngine para ejecutar acciones con la base de datos.
    @param function: String que será el titulo de la ventana
    """
    def __init__(self, parent, sgbd, function=None):
        super().__init__(parent)
        self.sgbd = sgbd
        self.pack()

        if function:
            self.master.title(function)

        ttk.Label(self,text="Choose a draw", font=('Kollektif', '30', 'normal')).pack()

        self.treeView = ttk.Treeview(self,columns=(0,1,2,3), show="headings", height="5")
        self.treeView.heading(0, text="Id")
        self.treeView.heading(1, text="Name")
        self.treeView.heading(2, text="Date")
        self.treeView.heading(3, text="Time")
        self.treeView.pack()

        self.fillTreeView()

        ttk.Button(self,text="Choose Draw",command=self.getSelected).pack()
    
    """
    Recupera información de la base de datos y los introduce en el objeto treeView.
    """
    def fillTreeView(self):
        encryptor = Encryptor()
        for draw in self.sgbd.retrieveDraws():
            draw[1] = encryptor.decrypt(draw[1])
            self.treeView.insert('','end',values=draw)
    """
    Establece como atributo la selección del usuario y destruye la 
    renderización de la ventana.
    """
    def getSelected(self):
        self.itemID = self.treeView.item(self.treeView.selection()[0])["values"][0]
        self.itemName = self.treeView.item(self.treeView.selection()[0])["values"][1]
        self.itemJSON = self.sgbd.retrieveDrawJSON(self.itemID)
        self.master.quit()
