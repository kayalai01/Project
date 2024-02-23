import tkinter as tk 

win=tk.Tk()
win.geometry("500x500")
win.title("Student Management System")

def quit():
    win.destroy()

def aboutpage():
    abt=tk.Tk
    



menubar=tk.Menu(win)
filemenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(lable="File",menu=filemenu, underline=0)
filemenu.add_command(lable="New", underline=0, accelerator="Alt+F")
filemenu.add_command(label="New window", underline=4, accelerator="Alt+W")
filemenu.add_command(lable="Save", underline=0, accelerator="Alt+S")
filemenu.add_command(label="Save As", underline=4, accelerator="Alt+A")
filemenu.add_command(lable="Page setup", underline=0, accelerator="Alt+P")
filemenu.add_command(label="New window", underline=4, accelerator="Alt+W")
filemenu.add_command(lable="New", underline=0, accelerator="Alt+F")
filemenu.add_command(label="New window", underline=4, accelerator="Alt+W")
