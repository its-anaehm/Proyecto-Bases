import tkinter
import tkinter.colorchooser
from tkinter import Tk
from tkinter import ttk

from Core.AddUserGUI import AddUserGUI
from Core.AlterUserGUI import ChooseUserToAlterGUI
from Core.BinnacleGUI import BinnacleGUI
from Core.DropUserGUI import DropUserGUI
from Core.MySQLEngine import *

"""
Objeto que se renderiza como la pantalla de configuración
@autor mdgomeza@unah.hn
@version 2.1
"""
class SettingsGUI(ttk.Frame):

    """
    Constructor de la clase
    @param parent Master del frame que representa la ventana.
    @param sgbd Objeto de tipo MySQLEngine utilizado para realizar
        operaciones con la base de datos.
    """
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
        ttk.Button(self,text="Log registred data",command=self.getBinnacle).pack(padx=10,pady=10,fill=tkinter.BOTH)


    """
    Inicia la ejecución de la pantalla que muestra la bitácora.
    """
    def getBinnacle(self):
        BinnacleGUI(self.master,self.sgbd)
        self.destroy()

    """
    Inicia la ejecución de la pantalla para agregar usuarios.
    """
    def addUser(self):
        root2 = Tk()
        root2.title("Add User")
        addUserGUI = AddUserGUI(root2)
        addUserGUI.sgbd = self.sgbd
        root2.mainloop()

    """
    Inicia la ejecución de la pantalla para alterar usuarios.
    """
    def alterUser(self):
        root = Tk()
        root.title("Change user values")
        ChooseUserToAlterGUI(root, self.sgbd)
        root.mainloop()

    """
    Inicia la ejecución de la pantalla para alterar usuarios.
    """
    def deleteUser(self):
        root = Tk()
        root.title("Drop User")
        dropUserGui = DropUserGUI(root,self.sgbd)
        root.mainloop()

    """
    Inicia la ejecución de la pantalla para cambiar el color del lapiz.
    """
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

    """
    Inicia la ejecución de la pantalla para cambiar el fill color.
    """
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

