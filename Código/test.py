from tkinter import *
from tkinter import filedialog, messagebox
import mysql.connector
import os

mydb = mysql.connector.connect(host="localhost", user="admin", passwd="admin", database="sample", auth_plugin="mysql_native_password")
cursor = mydb.cursor()


def savedata():
    fn = filedialog.askopenfilename(title="Select File")
    with open(fn, "rb") as f:
        data = f.read() # this is our binary data
    sql = "INSERT INTO files(id, file_data, date) VALUES(NULL, %s, NOW())"    
    cursor.execute(sql, (data, ))
    mydb.commit()	
    messagebox.showinfo("Success!", "Your file has been saved to database")

def readdata():
    fn = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save File")
    sql = "SELECT file_data FROM files LIMIT 1"
    cursor.execute(sql)
    r = cursor.fetchall()
    for i in r:
    	data = i[0] # this is the binary from database
    with open(fn,"wb") as f:
	    f.write(data)
    f.close()
    messagebox.showinfo("Success", "File has been saved")

win = Tk()

Button(win, text="Save File To Database", command=savedata).pack()
Button(win, text="Read File From Database", command=readdata).pack()

win.geometry("200x200")
win.title("Binary Data Read/Write to MYSQL")
win.mainloop()