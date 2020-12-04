from tkinter import *
import tkinter
from tkinter import ttk


top = tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()

def xd():
    print(CheckVar1.get(), CheckVar2.get())

ttk.Button(top, command=xd).pack()

top.mainloop()



