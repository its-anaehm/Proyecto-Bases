from tkinter import *
from tkinter import ttk

"""
GUI que muestra dibujos almacenados en la base de datos.
@author mdgomeza@unah.hn
@version 4.2
"""
class LoadDrawGUI(ttk.Frame):
    """
    Constructor de la clase.
    @param parent: Objeto master contenedor del frame.
    @param dta
    """
    def __init__(self, parent, data=None):
        super().__init__(parent)
        self.draws = self.getDraws()
        if data:
            self.data = data
        else:
            self.data =["Hola mundo %s" % i for i in range(50)]

        self.makeWidgets(self.data)

        self.pack(pady=20, padx=20)
    
    """
    Obtiene un usuario junto a su dibujo y el nombre del mismo.
    """
    def getDraws(self):
        return ('User', 'Name',"Data")*20


    def makeWidgets(self,data):
        self.data = data

        ttk.Label(self,text="Choose a draw", font=('Kollektif', '30', 'normal')).pack()
        self.listDraw = Listbox(self)

        num = 1
        for i in data:
            self.listDraw.insert(num, i)
            num = num + 1

        self.listDraw.pack(fill=BOTH)

        ttk.Button(self, text="Get", command=self.getCurrent).pack()

    """
    Obtiene el dibujo
    """
    def getCurrent(self):
        self.selection =  self.data[self.listDraw.curselection()[0]]
        self.master.destroy()


root = Tk()
root.title("Load a Draw")
load = LoadDrawGUI(root)
root.mainloop()
print(load.selection)

