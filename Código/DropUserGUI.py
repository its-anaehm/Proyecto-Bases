from Core.MySQLEngine import MySQLEngine
from tkinter import ttk
from tkinter import Tk
from tkinter import *


class DropUserGUI(ttk.Frame):
    """
    GUI para eliminar usuarios
    """
    def __init__(self,parent, sgbd: MySQLEngine):
        """
        :param parent: Objeto padre del frame que representa la clase.
        """
        super().__init__(parent)
        self.sgbd = sgbd
        self.userList = Listbox(self, selectmode=SINGLE)
        self.makeWidgets()
        self.pack()

    def makeWidgets(self) -> None:
        """
        Crea y empaqueta los elementos en la ventana.
        """
        ttk.Label(self,text="Drop User", font=('Times', '30', 'normal')).pack()

        self.fillUserList()
        
        self.userList.pack()
        ttk.Button(self,text="Drop User", command=self.drop).pack(padx=10, pady=10)

    def fillUserList(self):
        users = self.getUsers()
        for index in range(len(users)):
            self.userList.insert(index +1, users[index])

    def drop(self) -> None:
        """
        Elimina el usuario selecionado
        """
        name = self.userList.get(self.userList.curselection())
        if self.sgbd.dropUser(name[0]):
            self.userList.delete(0,'end')
            self.fillUserList()
        else:
            print("Tengo que poner un msgbox")

    def getUsers(self):
        """
        Ejecuta un query para obtener el nombre de los usuarios.
        """
        query = "SELECT var_user FROM Users"
        return self.sgbd.select(query)
