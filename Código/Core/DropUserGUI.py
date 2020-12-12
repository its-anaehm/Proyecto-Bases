from Core.MySQLEngine import MySQLEngine
from Core.MySQLEngineBackUp import MySQLEngineBackup
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk
from tkinter import *


"""
GUI para eliminar usuarios
@author mdomgeza@unah.hn
@version 4.1
"""
class DropUserGUI(ttk.Frame):
    """
    Construcctor de la clase.
    @param parent: Objeto que funcion como master para el frame que representa la clase.
    @param sgbd: Objeto de tipo MySQLEngine utilizado para ejecutar acciones con la base de datos.
    """
    def __init__(self,parent, sgbd: MySQLEngine):

        super().__init__(parent)
        self.sgbd = sgbd
        self.userList = Listbox(self, selectmode=SINGLE)
        self.makeWidgets()
        self.pack(padx=20, pady=20)

    """
    Crea y empaqueta los elementos en la ventana.
    """
    def makeWidgets(self) -> None:
        ttk.Label(self,text="Drop User", font=('Kollektif', '30', 'normal')).pack()

        self.fillUserList()
        
        self.userList.pack()
        ttk.Button(self,text="Drop User", command=self.drop).pack(padx=10, pady=10)

    """
    Llena la lisbox con los nombres de los usuarios
    """
    def fillUserList(self):
        self.users = self.getUsers()
        if self.users:
            for index in range(len(self.users)):
                self.userList.insert(index +1, self.users[index][1])

    """
    Retorna el id del usuario.
    @param name nombre del usuario
    """
    def getId(self, name):
        for user in self.users:
            if user[1] == name:
                return user[0]
        return -1



    """
    Elimina el usuario selecionado
    """
    def drop(self) -> None:
        name = self.userList.get(self.userList.curselection())
        if self.sgbd.dropUser(name[0]):
            self.userList.delete(0,'end')
            self.fillUserList()
            backup = MySQLEngineBackup(self.sgbd)
            backup.connect(filename = "Core/connectionConfigBackup.ini")
            backup.deleteAllUserDraws(self.getId(name[0]))
            messagebox.showinfo(title="User succesfully deleted", message="%s was deleted" % name[0])
        else:
            messagebox.showerror(title="Error to drop user",message="Something went wrong to drop the user. Call support")

    """
    Ejecuta un query para obtener el nombre de los usuarios.
    """
    def getUsers(self):
        query = "SELECT id, AES_DECRYPT(var_user,'%s') FROM Users" % self.sgbd.adminPass
        return self.sgbd.select(query)
