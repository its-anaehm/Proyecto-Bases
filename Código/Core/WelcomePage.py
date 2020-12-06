from tkinter import ttk
from tkinter.ttk import Style
from .LoginGUI import LoginGUI

class WelcomeGUI(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.NameLabel = ttk.Label(self,text="Welcome to Picasso",font=('Kollektif', '80', 'italic'), padding="50")
        self.UniLabel = ttk.Label(self,text="Universidad Nacional Autónoma de Honduras",font=('Kollektif','20','normal'), border='10')
        self.ClassLabel = ttk.Label(self,text="Bases de datos I por el Ingeniero José Inestroza III PAC 2020", font=('Kollektif','15','normal'), padding='15')

        self.pack()
        self.makeLabels()
        self.makeButtons()
        
    def makeLabels(self):
        self.NameLabel.pack()
        self.UniLabel.pack()
        self.ClassLabel.pack()


    def makeButtons(self):
        style = Style()
        style.configure('W.TButton',font = ('Kollektif','15','normal'))

        ttk.Button(self,text="Login", style='W.TButton', command=self.goToLoginPage).pack(pady=15)

    def goToLoginPage(self):
        self.destroy()
        LoginGUI(self.master)






