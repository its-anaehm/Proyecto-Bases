from re import template
from tkinter import ttk
from .draw import DrawingApplication
from .MySQLEngine import MySQLEngine
from tkinter import messagebox

class LoginGUI(ttk.Frame):
    """
    Frame que representa el login de la aplicación
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.makeForm()

    def makeForm(self):
        """
        Crea los widgets en el marco.
        """
        dataLabelFont = ('Times','20','normal')
        ttk.Label(self,text="Picasso",font=('Times', '60', 'italic'), padding="50").pack()
        self.name = ttk.Entry(self)
        self.name.pack()
        ttk.Label(self,text="User Name",font=dataLabelFont).pack()
        self.password = ttk.Entry(self)
        self.password.pack()
        ttk.Label(self,text="Password",font=dataLabelFont).pack()
        ttk.Button(self,text="Login", style='W.TButton', command=self.verify).pack(pady=15)

    def verify(self):
        """
        Verifica si el usuario está correctamente registrado
        
        sgbd = MySQLEngine()
        sgbd.authentication(self.name.get(),self.password.get())
        if(sgbd.connectionCheck()):
            sgbd.userLoginRegister(self.name.get())
            self.goToDraw(sgbd)
        else:
            print("Nel perro")
        """
        self.sgbd = MySQLEngine()
        userData = self.getUserData()
        response = None

        if userData:
            response = self.sgbd.authentication(userName=userData["name"], password=userData["password"])
        else:
            messagebox.showwarning(title="Wrong data",message="You should write you User name and you password.")
            return False
        
        if response[0]:
            self.goToDraw(self.sgbd)
        
        elif response[1] == "Wrong data":
            messagebox.showerror(title="Login Error",message="Wrong user data")
        
        else:
            messagebox.showerror(title="Something went wrong", message="We can not connect to the database.")
            

    def getUserData(self) -> dict:
        name = self.name.get()
        password = self.password.get()
        if name and password:
            return {
                "name" : name,
                "password": password
            }
        else:
            return {}

    def goToDraw(self, sgbd):
        """
        Go to the draw GUI
        """
        self.destroy()
        drawing = DrawingApplication(self.master)
        drawing.sgbd = sgbd
        drawing.buildWindow()

