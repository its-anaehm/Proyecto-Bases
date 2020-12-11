#-*- coding:utf8 -*-

from tkinter.messagebox import showwarning
from Core.MySQLEngine import MySQLEngine
from tkinter import ttk
import tkinter.simpledialog as simpleDialog
from tkinter import *
import tkinter


"""
GUI para seleccionar el usuario a alterar
@author mdgomeza@unah.hn
@version 2.0
"""
class ChoseUserToAlterGUI(ttk.Frame):

    """
    Constructor de la clase.
    @param parent: Objeto master contenedor del Frame
    @param sgbd: Objeto MySQLEngine usado para ejecutar acciones con la base de datos.
    """
    def __init__(self, parent, sgbd) -> None:

        super().__init__(parent)
        self.pack(padx=20, pady=20)
        self.master.title("Alter user")
        self.sgbd:MySQLEngine = sgbd

        ttk.Label(self,text="Chose an User", font=('Kollektif', '30', 'normal')).pack()

        self.userList = Listbox(self, selectmode=SINGLE)
        self.users = []

        ttk.Button(self,text="Alter User", command=self.goToAlterUser).pack()

        self.fillUserList()

        self.userList.pack()

    """
    Recupera los datos de usuarios para mostrarlos en una lista.
    """
    def fillUserList(self):
        self.users = self.sgbd.retrieveUsers()

        for i in range(len(self.users)):
            self.userList.insert(i, self.users[i])

    """
    Toma los datos y envia al editor de usuario
    """
    def goToAlterUser(self):
        name = self.userList.get(self.userList.curselection())[0]
        root = Tk()
        ChangeUserData(root, self.sgbd, name, self.users)
        root.title("Change user values")
        self.master.destroy()
        root.mainloop()



"""

"""
class ChangeUserData(ttk.Frame):
    def __init__(self,parent, sgbd, userName, usersList):
        super().__init__(parent)
        self.parent = parent
        self.sgbd = sgbd
        self.userName = userName
        self.usersList = usersList

        self.pack(padx=20, pady=20)
        ttk.Label(self,text="Change de values of the user %s" % self.userName, font=('Kollektif', '30', 'normal')).pack()
        
        ttk.Button(self,text="Change name", command=self.changeName).pack()
        ttk.Button(self,text="Change Password", command=self.changePassword).pack()

    """
    Determina el procesamiento del cambio de nombre de usuario de un usuario desde la interfaz
    """
    def changeName(self):
        newName = simpleDialog.askstring("New User Name","Write the new user name from %s" % self.userName)

        if newName in self.usersList:
            showwarning(title="Error user name", message="The user %s already exist" % newName)
        elif newName:
            self.sgbd.alterUser(userName=self.userName, newUserName=newName)
            self.master.destroy()

    """
    Determina el procesamiento del cambio de contraseña de un usuario desde la interfaz.
    """
    def changePassword(self):
        newPassword = simpleDialog.askstring("New password", "Write new password for %s" % self.userName)
        if newPassword:
            self.sgbd.alterUser(userName=self.userName, password=newPassword)
            self.master.destroy()