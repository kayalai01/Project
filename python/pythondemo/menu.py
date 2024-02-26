import tkinter as tk 

win=tk.Tk()
win.geometry("500x500")
win.title("Student Management System")

def quit():
    win.destroy()

def aboutpage():
    abt=tk.Tk
    abt.title("About us")
    abt.geometry("300x300")
    
    message="""Welcome to Student DB
Info is our student Datas .still
currently update!!

"""
    lntinfo=tk.Label(abt,text=message)
    lntinfo.pack()
    abt.mainloop()


menubar=tk.Menu(win)
filemenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=filemenu, underline=0)
filemenu.add_command(label="New", underline=0, accelerator="Alt+F")
filemenu.add_command(label="New window", underline=4, accelerator="Alt+W")
filemenu.add_command(label="Save", underline=0, accelerator="Alt+S")
filemenu.add_command(label="Save As", underline=4, accelerator="Alt+A")
filemenu.add_separator()
filemenu.add_command(label="Page setup", underline=0, accelerator="Alt+P")
filemenu.add_command(label="print", underline=0, accelerator="Alt+X")
filemenu.add_separator()
filemenu.add_command(label="Exit", underline=0, accelerator="Alt+E")


editmenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu, underline=0)
editmenu.add_command(label="Undo",underline=0, accelerator="ctr+Z")
editmenu.add_command(label="Redo", underline=0, accelerator="ctr+Y")
editmenu.add_separator()
editmenu.add_command(label="Cut",underline=0, accelerator="ctr+X")
editmenu.add_command(label="Copy",underline=0, accelerator="ctr+C")
editmenu.add_command(label="paste",underline=0, accelerator="ctr+V")

viewmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu, underline=0)

helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu,underline=0)
helpmenu.add_command(label="About",underline=0 , command=aboutpage) 

win.config(menu=menubar)

win.mainloop()