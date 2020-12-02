from tkinter import ttk
from draw import DrawingApplication

class LoginGUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.makeForm()

    def makeForm(self):
        dataLabelFont = ('Times','20','normal')
        ttk.Label(self,text="Picasso",font=('Times', '60', 'italic'), padding="50").pack()
        ttk.Entry(self).pack()
        ttk.Label(self,text="User Name",font=dataLabelFont).pack()
        ttk.Entry(self).pack()
        ttk.Label(self,text="Password",font=dataLabelFont).pack()
        ttk.Button(self,text="Login", style='W.TButton', command=self.goToDraw).pack(pady=15)

    def goToDraw(self):
        self.destroy()
        DrawingApplication(self.master)
