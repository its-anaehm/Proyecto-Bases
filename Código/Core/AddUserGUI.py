from Core.MySQLEngine import MySQLEngine
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk
from tkinter import *


"""
GUI para la agregación de usuarios.
@author aehernandezm@unah.hn
@versión 3.0
"""
class AddUserGUI(ttk.Frame):

    """
    Constructor de la clase
    @param parent Objeto contenedor del Frame.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.dataLabelFont = ('Kollektif', '20', 'normal')
        self.pack(pady=20, padx=20)
        self.sgbd: MySQLEngine= None
        self.checkVar = BooleanVar()

        self.checkButton = Checkbutton(self,
            text="Create as admin", variable=self.checkVar,
            command=self.toggleOption,
            onvalue=True,
            offvalue=False
        )

        self.makeWidgets()
        self.checkButton.pack()

    """
    modifica el valor del la variable que establece si el
    usuario se crearó como admin o no.
    """
    def toggleOption(self):
        self.checkVar.set(not self.checkVar.get())


    """
    Obtiene los datos de los campos de entrada de la GUI.
    """
    def getUserData(self) -> dict:
        name = self.nameEntryWidget.get()
        password = self.passwordEntryWidget.get()
        if name and password:
            return {
                "name": name,
                "password": password,
                "admin" : self.checkVar.get()
            }
        else:
            return {}

    """
    Empaqueta los widgets en la ventana
    """
    def makeWidgets(self):
        ttk.Label(self, text="Add User", font=('Kollektif', '40', 'normal')).pack()

        self.nameEntryWidget = ttk.Entry(self)
        self.nameEntryWidget.pack()
        ttk.Label(self, text="User name", font=self.dataLabelFont).pack()

        self.passwordEntryWidget = ttk.Entry(self)
        self.passwordEntryWidget.pack()
        ttk.Label(self, text="Password", font=self.dataLabelFont).pack()

        ttk.Button(self, text="Add user", command=self.addUser).pack(pady=10)

    """
    Ejecuta las acciones para agregar el usuario a la base de datos.
    """
    def addUser(self):
        userData = self.getUserData()

        if self.getUserData:
            if self.sgbd.addUser(
                userName=userData["name"],
                userPassword=userData["password"],
                admin=userData["admin"]
            ):
                self.master.destroy()
                return True
            else:
                messagebox.showerror(title="Error to add user", message="Something went wrong. Call support")
        else:
            messagebox.showerror(title="Error User data", message="You should write the User name and the Password.")
        
        return False


"""root = Tk()
root.title("Add User")
addUserGUI = AddUserGUI(root)
root.mainloop()"""