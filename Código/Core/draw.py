# -*- coding:utf-8 -*-
# The imports include turtle graphics and tkinter modules.
# The colorchooser and filedialog modules let the user
# pic a color and a filename.
import json
import os
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import tkinter.simpledialog as simpleDialog
import turtle
from tkinter import Tk
from tkinter import messagebox

from Core.ChooseDraw import ChooseDraw
from Core.MySQLEngine import MySQLEngine
from Core.MySQLEngineBackUp import MySQLEngineBackup
from Core.SettingsGUI import SettingsGUI


# The following classes define the different commands that
# are supported by the drawing application.
class GoToCommand:
    def __init__(self,x,y,width=1,color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    # The draw method for each command draws the command
    # using the given turtle
    def draw(self,turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x,self.y)
    
    # The __str__method is a special method that is called
    # when a command is converted to a string. The string
    # version of the command is how it appears in the graphic
    # file format.
    def __str__(self, tab=0):
        return '%s{"command": "GoTo", "x": %s, "y": %s, "width": %s,"color": "%s" }' % ("\t"*tab, self.x, self.y, self.width, self.color)
        
    def toDict(self):
        return {
            "command": "GoTo",
            "x": str(self.x),
            "y": str(self.y),
            "width": str(self.width),
            "color": str(self.color)
        }

class CircleCommand:
    def __init__(self,radius,width=1,color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self,turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)   
        turtle.circle(self.radius)
    
    def __str__(self, tab=0):
        return '%s{"command": "Circle", "radius": %s, "width": %s,"color": "%s" }' % ("\t"*tab, self.radius,
        self.width, self.color)

        # return "<Command radius="" + str(self.radius) + "" width="" + str(self.width) + "" color="" + self.color + "">Circle</Command>"

    def toDict(self):
        return {
            "command": "Circle",
            "radius": str(self.radius),
            "width": str(self.width),
            "color": str(self.color)
        }

class BeginFillCommand:
    def __init__(self,color):
        self.color = color
    
    def draw(self,turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()
    
    def __str__(self, tab=0):
        return '%s{"command": "BeginFill", "color": "%s" }' % ("\t"*tab, self.color)

        # return "<Command color="" + self.color + "">BeginFill</Command>"

    def toDict(self):
        return {
            "command": "BeginFill",
            "color": str(self.color)
        }
    
class EndFillCommand:
    def __init__(self):
        pass

    def draw(self,turtle):
        turtle.end_fill()
    
    def __str__(self, tab=0):
        return '%s{"command": "EndFill"}' % ("\t"*tab)

        # return "<Command>EndFill</Command>"

    def toDict(self):
        return {
            "command": "EndFill"
        }
        
class PenUpCommand:
    def __init__(self):
        pass
    
    def draw(self, turtle):
        turtle.penup()
    
    def __str__(self, tab=0):
        return '%s{"command": "PenUp"}' % ("\t"*tab)

        # return "<Command>PenUp</Command>"
    
class PenDownCommand:
    def __init__(self):
        pass
    
    def draw(self, turtle):
        turtle.pendown()    

    def __str__(self, tab=0):
        return '%s{"command": "PenDown"}' % ("\t"*tab)

        # return "<Command>PenDown</Command>"

    def toDict(self):
        return {
            "command": "PenDown"
        }
    
# This is the PyList container object. ItgraphicsCommands is meant to hold a
class PyList:
    def __init__(self):
        self.gcList = []
    
    #The append method is used to add commands to the sequence.
    def append(self,item):
        self.gcList = self.gcList + [item]
    
    # This method is used by the undo function. It slices the sequence.
    # to remove the last item
    def removeLast(self):
        self.gcList = self.gcList[:-1]
    
    # This special method is called when iterating over the sequence.
    # Each time yield is called another element of the sequence is returned
    # to the iterator (i.e. the for loop that called this.)
    def __iter__(self):
        for c in self.gcList:
            yield c
        
    # This is called when the len function is called on the sequence.
    def __len__(self):
        return len(self.gcList)

# This class defines the drawing application. The following line says that
# the DrawingApplication class inherits from the Frame class. This means
# that a DrawingApplication is like a Frame object except for the code
# written here wich redefines/extends the behavior of a Frame.
class DrawingApplication(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.sgbd:MySQLEngine = None
        self.graphicsCommands = PyList()


    # This method is called to create all the widgets, place them in the GUI,column
    # and define the event handlers for the application.
    def buildWindow(self):

        # The master is the root window. The title is set as below.
        self.master.title("Picasso")

        # Here isi how to create a menu bar. The tearoff=0 means that menus
        # can"t be separated from the window which is a feature of tkinter.
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)

        # This code is called by the "New" menu item below when it is selected.
        # The same applies for loadFile, addFile, and saveFile below. The
        # "Exit" menu item below calls quit on the "master" or root window.
        def newWindow():
            # This sets up the turtle to be ready for a new picture to be
            # drawn. It also sets the sequence back to empty. It is necessary
            # for the graphicsCommands sequence to be in the object (i.e. 
            # self.graphicsCommands) because otherwise the statement:
            # graphicsCommands = PyList()
            # would make this variable a local variable in the newWindow
            # method. If it werelocal, it would not be set anymore once the
            # newWindow method returned.
            theTurtle.clear()
            theTurtle.penup()
            theTurtle.goto(0,0)
            theTurtle.pendown()
            screen.update()
            screen.listen()
            self.graphicsCommands = PyList()

        fileMenu.add_command(label="New",command=newWindow)

        # The parse function adds the contents of an XML file to the sequence
        def parse(JSONString):

            if type(JSONString) == str:
                JSONData = json.loads(JSONString)
            else:
                JSONData = JSONString

            graphicsCommands = JSONData["Draw"]

            for commandElement in graphicsCommands:
                command = commandElement["command"]

                if command == "GoTo":
                    x = commandElement["x"]
                    y = commandElement["y"]
                    width = commandElement["width"]
                    color = commandElement["color"]
                    cmd = GoToCommand(x,y,width,color)
            
                elif command == "Circle":
                    radius = commandElement["radius"]
                    width = commandElement["width"]
                    color = commandElement["color"]
                    cmd = CircleCommand(radius,width,color)
                
                elif command == "BeginFill":
                    color = commandElement["color"]
                    cmd = BeginFillCommand(color)
                
                elif command == "EndFill":
                    cmd = EndFillCommand()
                
                elif command == "PenUp":
                    cmd = PenUpCommand()
                
                elif command == "PenDown":
                    cmd = PenDownCommand()
                elif command == "end":
                    pass
                else:
                    raise RuntimeError("Unknown command: " + command)
                
                self.graphicsCommands.append(cmd)

        def loadFile():

            #filename = tkinter.filedialog.askopenfilename(title="Select a Graphics File")
            #self.destroy()

            root = Tk()
            chooseDraw = ChooseDraw(root,self.sgbd)
            root.mainloop()

            root.destroy()
            newWindow()
            # This re-initializes the sequence for the new picture.
            self.graphicsCommands = PyList()

            # calling parse will read the graphics commands from the file.
            parse(chooseDraw.itemJSON)

            for cmd in self.graphicsCommands:
                    cmd.draw(theTurtle)
                
            # This line is necessary to update the window after the picture is drawn.
            screen.update()
            self.sgbd.selectRegister(self.sgbd.user)
            

        fileMenu.add_command(label="Load...",command=loadFile)
        """
        # The write function writes an XML file to the given filename
        def write(filename):
            file = open(filename, "w")
            file.write("<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n"")
            file.write("<GraphicsCommands>\n")
            for cmd in self.graphicsCommands:
                file.write("    "+str(cmd)+"\n")
            
            file.write("</GraphicsCommands>\n"")

            file.close()
        """

        def drawToJSON():
            result = []
            result.append('{"Draw":[')

            for cmd in self.graphicsCommands:
                result.append("%s%s" %(str(cmd),","))
            result.append('{"command":"end"}')
            result.append("]}")

            return "".join(result)
        """
        def write(filename, formated=False, tab=1):
            file = open(filename,"w")
            if (formated):
                file.write('{\n%s"Draw":[\n' % ("\t"*tab))
                for cmd in self.graphicsCommands:
                    file.write("%s%s\n" % (cmd.__str__(tab+1),","))
                file.write('\t\t{"command":"end"}')
                file.write("\n\t]\n}")
            else:              
                file.write('{"Draw":[')
                for cmd in self.graphicsCommands:
                    file.write("%s%s" %(str(cmd),","))
                file.write('{"command":"end"}')
                file.write("]}")
            file.close()
        """
        def saveFile():
            #filename = tkinter.filedialog.asksaveasfilename(title="Save Picture As...")
            filename = simpleDialog.askstring("Save draw","Write the name of the draw.")
            JSONDraw = drawToJSON()

            backUp = MySQLEngineBackup(self.sgbd)
            backUp.connect(filename = "Core/connectionConfigBackup.ini")

            if filename:
                result = self.sgbd.insertDraw(drawName=filename, drawConfig=JSONDraw)
                backUp.insertDraw(self.sgbd.mysql_userId,filename,JSONDraw)

                if result["status"]:
                    fileAbsPath = os.path.join(os.path.abspath("."),"%s.json" % filename)
                    print(fileAbsPath)
                else:
                    question = messagebox.askyesno(title="Save Draw", message="Draw %s already exists, do you want overwrite it?." % filename)
                    if question:
                        self.sgbd.modifyDraw(result["drawId"], drawToJSON())
                        backUp.modifyDraw(result["drawId"], drawToJSON())
        
        fileMenu.add_command(label="Save As...",command=saveFile)



        bar.add_cascade(label="File",menu=fileMenu)

        # This tells the root window to display the newly created menu bar.
        self.master.config(menu=bar)

        # Here several widgets are created. The canvas is the drawing area on
        # the left side of the window.
        canvas = tkinter.Canvas(self,width=600,height=600)
        canvas.pack(side=tkinter.LEFT)

        # By creating a RawTurtle, we can have the turtle draw on this canvas.
        # Otherwise, a RawTurtle and a Turtle are exactly the same.
        theTurtle = turtle.RawTurtle(canvas)

        # This makes the shape of the turtle a circle.
        theTurtle.shape("circle")
        screen = theTurtle.getscreen()

        # This causes the application to not update the screen unless
        # screen.update() is called. This is necessary for the ondrag event
        # handlre below. Without it, the program bombs after dragging the
        # turtle around for a while.
        screen.tracer(0)

        # This is the area on the right side of the window where all the
        # buttons, labels, and entry boxes are located. The pad creates some empty
        # space around the side. The side puts the sideBara on the right side of the
        # this frame. The fill tells it to fill in all space available on the right
        # side.
        sideBar = tkinter.Frame(self, padx=5, pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        # This is a label widget. Packing it puts it at the top of the sidebar.
        pointLabel = tkinter.Label(sideBar,text="Width")
        pointLabel.pack()

        # This entry widget allows the user to pic a width for their lines.
        # With the widthSize variable below you can write widthSize.get() to get
        # the contents of the entry widget and widthSize.set(val) to set the value
        # of the entry widget to val. Initially the widthSize is set to 1. str(1) is
        # needed because the entry widget must be given a string.
        widthSize = tkinter.StringVar()
        widthEntry = tkinter.Entry(sideBar,textvariable=widthSize)
        widthEntry.pack()
        widthSize.set(str(1))
    
        radiusLabel = tkinter.Label(sideBar,text="Radius")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar,textvariable=radiusSize)
        radiusSize.set(str(10))
        radiusEntry.pack()

        # A button widget calls an event handler when it is pressed. The circle Handler
        # function below is the event handler when the Draw Circle button is pressed.
        def circleHandler():
            # When drawing, a command is created and then the command is drawn by calling
            # the draw method. Adding the command to the graphics Commands sequence means the 
            # application will remember the picture.
            cmd = CircleCommand(float(radiusSize.get()), float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

            # These two lines are needed to update the screen and to put the focus back
            # in the drawing canvas. This is necessary because when pressing "u" to undo,
            # the screen must have focus to receive the key press.
            screen.update()
            screen.listen()

        # This creates the button widget in the sideBar. The fill=tkinter.BOTH causes the button
        # to expand to fill the entire width of the sideBar.
        circleButton = tkinter.Button(sideBar, text = "Draw Circle", command=circleHandler)
        circleButton.pack(fill=tkinter.BOTH)

        # The color mode 255 below allows colors to be specified in RGB form (i.e. Red/
        # Green/Blue). The mode allows the Red value to be set by a two digit hexadecimal
        # number ranging from 00-FF. The same applies for Blue and Green calues. The
        # color choosers below return a string representing the selected color and a slice
        # is taken to extract the #RRGGBB hexadecimal string that the color choosers return.
        screen.colormode(255)
        penLabel = tkinter.Label(sideBar, text="Pen Color")
        penLabel.pack()
        penColor = tkinter.StringVar()
        penEntry = tkinter.Entry(sideBar,textvariable=penColor)
        penEntry["state"] = tkinter.NORMAL if self.sgbd.isAdmin() else tkinter.DISABLED

        penEntry.pack()
        # This is the color from the DB.
        penColor.set(self.sgbd.retrieveColorConfig()[0])

        def getPenColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                penColor.set(str(color)[-9:-2])
        
        penColorButton = tkinter.Button(sideBar, text = "Pick Pen Color", command=getPenColor)
        penColorButton["state"] = tkinter.NORMAL if self.sgbd.isAdmin() else tkinter.DISABLED
        penColorButton.pack(fill=tkinter.BOTH)

        fillLabel = tkinter.Label(sideBar,text="Fill Color")
        fillLabel.pack()
        fillColor = tkinter.StringVar()
        fillEntry = tkinter.Entry(sideBar,textvariable=fillColor)
        fillEntry["state"] = tkinter.NORMAL if self.sgbd.isAdmin() else tkinter.DISABLED

        fillEntry.pack()
        fillColor.set(self.sgbd.retrieveColorConfig()[1])

        def getFillColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                fillColor.set(str(color)[-9:-2])
        
        fillColorButton = tkinter.Button(sideBar,text="Pick Fill Color", command=getFillColor)
        fillColorButton["state"] = tkinter.NORMAL if self.sgbd.isAdmin() else tkinter.DISABLED
        fillColorButton.pack(fill=tkinter.BOTH)


        def beginFillHandler():
            cmd = BeginFillCommand(fillColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
        
        beginFillButton = tkinter.Button(sideBar, text = "Begin Fill", command=beginFillHandler)
        beginFillButton.pack(fill=tkinter.BOTH)

        def endFillHandler():
            cmd = EndFillCommand()
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
        
        endFillButton = tkinter.Button(sideBar, text = "End Fill", command=endFillHandler)
        endFillButton.pack(fill=tkinter.BOTH)

        penLabel = tkinter.Label(sideBar, text="Pen Is Down")
        penLabel.pack()

        def penUpHandler():
            cmd = PenUpCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Pen Is Up")
            self.graphicsCommands.append(cmd)
        
        penUpButton = tkinter.Button(sideBar, text = "Pen Up", command=penUpHandler)
        penUpButton.pack(fill=tkinter.BOTH)

        def penDownHandler():
            cmd = PenDownCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Pen Is Down")
            self.graphicsCommands.append(cmd)
        
        penDownButton = tkinter.Button(sideBar, text = "Pen Down", command=penDownHandler)
        penDownButton.pack(fill=tkinter.BOTH)

        # Here is another event handler. This one handles mouse clicks on the screen.
        def clickHandler(x,y):
            # When a mouse click occurs, get the widthSize entry value and set the width of teh
            # pen to the widthSize value. Te float(widthSize.get()) is needed because
            # the width is a float, but the entry widget stores it as a string.
            cmd = GoToCommand(x,y,float(widthSize.get()),penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()
        
        # Here is how we tie the clickHandler to mouse clicks.
        screen.onclick(clickHandler)

        def dragHandler(x,y):
            cmd = GoToCommand(x,y,float(widthSize.get()),penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()
        
        theTurtle.ondrag(dragHandler)

        # the undoHandler undoes the last command by removing it from the
        # sequence and then dredrawing the entire picture.
        def undoHandler():
            if len(self.graphicsCommands) > 0:
                self.graphicsCommands.removeLast()
                theTurtle.clear()
                theTurtle.penup()
                theTurtle.goto(0,0)
                theTurtle.pendown()
                for cmd in self.graphicsCommands:
                    cmd.draw(theTurtle)
                screen.update()
                screen.listen()
        

        def dropDraw():
            root = Tk()
            root.title("Delete a draw")
            chooseDraw = ChooseDraw(root,self.sgbd)
            root.mainloop()
            root.destroy()
            backup = MySQLEngineBackup(self.sgbd)
            backup.connect(filename = "Core/connectionConfigBackup.ini")
            
            backup.deleteDraw(chooseDraw.itemID)
            self.sgbd.dropDraw(chooseDraw.itemID)

        fileMenu.add_command(command=dropDraw, label="Drop draw")

        def settings():
            root = Tk()
            SettingsGUI(root,self.sgbd)
            root.title("Settings")
            root.mainloop()

        if self.sgbd.isAdmin():
            fileMenu.add_command(label="Configure", command=settings)

        def downloadDraw():
            backUp = MySQLEngineBackup(self.sgbd)
            backUp.connect(filename = "Core/connectionConfigBackup.ini")
            root = Tk()
            root.title("Download a Draw")
            chooseDraw = ChooseDraw(root,self.sgbd)
            root.mainloop()
            root.destroy()
            backUp.download(chooseDraw.itemID)

        fileMenu.add_command(label="Download Draw", command=downloadDraw)

        def quitApp():
            self.sgbd.closeDatabase()
            self.master.destroy()

        fileMenu.add_command(label="Exit",command=quitApp)



        screen.onkeypress(undoHandler, "u")
        screen.listen()

# The main function in our GUI program is very simple. It creates the
# root window. Then it creates the DrawingApplication frame which creates
# all the widgets and has the logic for the event handlers. Calling mainloop
# on the frames makes it start listening for events. The mainloop function will
# return when the application is exited.
def main():
    root = tkinter.Tk()
    drawingApp = DrawingApplication(root)
    
    drawingApp.mainloop()
    print("Program Execution Completed.")

if __name__ ==  "__main__":
    main()