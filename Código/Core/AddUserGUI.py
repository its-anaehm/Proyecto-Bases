from tkinter import ttk
from tkinter import Tk

class AddUserGUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.dataLabelFont = ('Times','20','normal')
        self.pack(pady=20,padx=20)
        self.makeWidgets()

    def makeWidgets(self):
        self.titleLabel = ttk.Label(self, text="Add User", font=('Times', '40', 'normal')).pack()
        self.nameEntryWidget = ttk.Entry(self).pack()
        self.nameLabel = ttk.Label(self, text="User name", font=self.dataLabelFont).pack()
        self.passwordEntryWidget = ttk.Entry(self).pack()
        self.passwordLabel = ttk.Label(self, text="Password", font=self.dataLabelFont).pack()
        self.addButton = ttk.Button(self, text="Add user").pack(pady=10)

