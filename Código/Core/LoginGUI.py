from re import template
from tkinter import PhotoImage, Tk, ttk
from .draw import DrawingApplication
from .MySQLEngine import MySQLEngine
from tkinter import messagebox

"""
Frame que representa el login de la aplicación
@author mdomgeza@unah.hn
@version 3.0
"""
class LoginGUI(ttk.Frame):
    """
    Constructor de la clase.
    @param parent: Master contenedor del frame de la clase.
    """
    def __init__(self, parent=None):
        if not parent:
            parent = Tk()
            parent.title("Picasso")
            parent.resizable(0,0)
            logo = PhotoImage(file="Core/LogoProyecto.png")
            parent.iconphoto(False,logo)


        super().__init__(parent)
        self.pack()
        self.makeForm()
        self.master.mainloop()

    """
    Crea los widgets en el marco.
    """
    def makeForm(self):
        dataLabelFont = ('Kollektif','20','normal')
        ttk.Label(self,text="Picasso",font=('Kollektif', '60', 'italic'), padding="50").pack()
        self.name = ttk.Entry(self)
        self.name.pack()
        ttk.Label(self,text="User Name",font=dataLabelFont).pack()
        self.password = ttk.Entry(self)
        self.password.pack()
        ttk.Label(self,text="Password",font=dataLabelFont).pack()
        ttk.Button(self,text="Login", style='W.TButton', command=self.verify).pack(pady=15)


    """
    Verifica se realize correctamente una conexión con la base de datos.
    """
    def verify(self):

        self.sgbd = MySQLEngine()
        userData = self.getUserData()
        response = None

        if userData:
            response = self.sgbd.authentication(userName=userData["name"], password=userData["password"])
        else:
            messagebox.showwarning(title="Wrong data",message="You should write you User name and you password.")
            return False
        

        print(response)

        if response["status"]:
            self.goToDraw(self.sgbd)
        
        elif response["message"] == "Wrong data":
            messagebox.showerror(title="Login Error",message="Wrong user data")
        
        else:
            messagebox.showerror(title="Something went wrong", message="We can not connect to the database.")
            
    """
    Obtiene los datos del usuario escritos en el inicio de sesión retornándolos en un JSON.
    """
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

    """
    Instancia la aplicación de dibujo y envia al usuario a ella.
    """
    def goToDraw(self, sgbd):
        """
        Go to the draw GUI
        """
        self.destroy()
        drawing = DrawingApplication(self.master)
        drawing.sgbd = sgbd 
        drawing.buildWindow()

