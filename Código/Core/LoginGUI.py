from tkinter import ttk
from .draw import DrawingApplication
from .MySQLEngine import MySQLEngine

class LoginGUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.makeForm()

    def makeForm(self):
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
        sgbd = MySQLEngine()
        sgbd.authentication(self.name.get(),self.password.get())
        if(sgbd.connectionCheck()):
            self.goToDraw()
        else:
            print("Nel perro")

    def goToDraw(self):
        self.destroy()
        DrawingApplication(self.master)
