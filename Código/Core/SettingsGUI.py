from Core.DropUserGUI import DropUserGUI
from Core.AddUserGUI import AddUserGUI
from Core.AlterUserGUI import ChoseUserToAlterGUI
from Core.MySQLEngine import *

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import Tk
import tkinter.colorchooser
class SettingsGUI(ttk.Frame):
    def __init__(self, parent, sgbd):
        super().__init__(parent)
        self.pack(padx=20, pady=20)
        self.sgbd = sgbd

        self.drawingSetting = ttk.Frame(self)
        self.drawingSetting.pack()

        ttk.Label(self.drawingSetting,text="Drawing settings", font=('Kollektif', '30', 'normal')).pack(padx=10,pady=10)
        ttk.Button(self.drawingSetting,text="Change pen color", command=self.changePenColor).pack(padx=10,pady=10,side=tkinter.LEFT)
        ttk.Button(self.drawingSetting,text="Change fill color", command=self.changeFillColor).pack(padx=10,pady=10,side=tkinter.RIGHT)

        ttk.Separator(self,orient=tkinter.HORIZONTAL).pack(fill=tkinter.BOTH)

        ttk.Label(self,text="User Settings", font=('Kollektif', '30', 'normal')).pack(padx=10,pady=10)
        ttk.Button(self,text="Add User",command=self.addUser).pack(padx=10,pady=10, fill=tkinter.BOTH)
        ttk.Button(self,text="Change Name and password to User",command=self.alterUser).pack(padx=10,pady=10,fill=tkinter.BOTH)
        ttk.Button(self,text="Delete User",command=self.deleteUser).pack(padx=10,pady=10,fill=tkinter.BOTH)

    def addUser(self):
        root2 = Tk()
        root2.title("Add User")
        addUserGUI = AddUserGUI(root2)
        addUserGUI.sgbd = self.sgbd
        root2.mainloop()

    def alterUser(self):
        root = Tk()
        root.title("Change user values")
        ChoseUserToAlterGUI(root, self.sgbd)
        root.mainloop()

    def deleteUser(self):
        root = Tk()
        root.title("Drop User")
        dropUserGui = DropUserGUI(root,self.sgbd)
        root.mainloop()

    def changePenColor(self):
        color = tkinter.colorchooser.askcolor()
        if color[0] != None:
            hexaColor = color[1]
            try:
                self.mysql_sendPenColor = "UPDATE drawsConfig SET var_penColor = '%s'" % (hexaColor)
                self.sgbd.link.execute(self.mysql_sendPenColor)
                self.sgbd.con.commit()
            except mysql.connector.Error as error:
                print("La configuración no pudo aplicarse, {}".format(error))

    def changeFillColor(self):
        color = tkinter.colorchooser.askcolor()
        if color[0] != None:
            hexaColor = color[1]
            try:
                self.mysql_sendFillColor = "UPDATE drawsConfig SET var_fillColor = '%s'" % (hexaColor)
                self.sgbd.link.execute(self.mysql_sendFillColor)
                self.sgbd.con.commit()
            except mysql.connector.Error as error:
                print("La configuración no pudo aplicarse, {}".format(error))

