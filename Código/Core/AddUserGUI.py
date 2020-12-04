from tkinter import ttk
from tkinter import Tk
from tkinter import *

class AddUserGUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.dataLabelFont = ('Times','20','normal')
        self.pack(pady=20,padx=20)
        self.sgbd = None
        self.checkVar = BooleanVar()
        self.checkButton = Checkbutton(self, text="Create as admin", variable=self.checkVar,
                                           command=self.toggleOption,
                                           onvalue=True,offvalue=False)

        self.makeWidgets()
        self.checkButton.pack()

    def toggleOption(self):
        self.checkVar.set(not self.checkVar.get())


    def makeWidgets(self):
        self.titleLabel = ttk.Label(self, text="Add User", font=('Times', '40', 'normal')).pack()
        self.nameEntryWidget = ttk.Entry(self)
        self.nameEntryWidget.pack()
        self.nameLabel = ttk.Label(self, text="User name", font=self.dataLabelFont).pack()
        self.passwordEntryWidget = ttk.Entry(self)
        self.passwordEntryWidget.pack()
        self.passwordLabel = ttk.Label(self, text="Password", font=self.dataLabelFont).pack()
        self.addButton = ttk.Button(self, text="Add user", command=self.addUser).pack(pady=10)

        #self.adminCheck = ttk.Checkbutton(self, text="Create as admin", variable=self.checkVar,command=self.getValue, onvalue=1, offvalue=0)
    
        #self.adminCheck.pack()

        #self.NoAdmin = 

    def getValue(self):
        print(self.checkVar.get())
    
    def addUser(self):
        print(self.checkVar.get())
        if self.sgbd.addUser(
            self.nameEntryWidget.get(),
            self.passwordEntryWidget.get(),
            True if self.checkVar.get() == 1 else False
        ):
            self.master.destroy()

"""root = Tk()
root.title("Add User")
addUserGUI = AddUserGUI(root)
root.mainloop()"""