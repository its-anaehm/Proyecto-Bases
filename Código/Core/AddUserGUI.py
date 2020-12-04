from Core.MySQLEngine import MySQLEngine
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk
from tkinter import *


class AddUserGUI(ttk.Frame):
    """
    GUI para agregar usuarios
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.dataLabelFont = ('Times', '20', 'normal')
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

    def toggleOption(self):
        """
        modifica el valor del la variable que establece si el
        usuario se crearó como admin o no.
        """
        self.checkVar.set(not self.checkVar.get())

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

    def makeWidgets(self):
        """
        Empaqueta los widgets en la ventana
        """
        ttk.Label(self, text="Add User", font=('Times', '40', 'normal')).pack()

        self.nameEntryWidget = ttk.Entry(self)
        self.nameEntryWidget.pack()
        ttk.Label(self, text="User name", font=self.dataLabelFont).pack()

        self.passwordEntryWidget = ttk.Entry(self)
        self.passwordEntryWidget.pack()
        ttk.Label(self, text="Password", font=self.dataLabelFont).pack()

        ttk.Button(self, text="Add user", command=self.addUser).pack(pady=10)

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
