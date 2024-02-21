from tkinter import *
import mysql.connector

win=Tk()

win.title("Insert into MySQL DB Demo")
win.geomentry("500x500")

frameleft=Frame(win,bg="black",width=500, height=50,padx=30,pady=30)
frameleft.pack(side=LEFT)

frameright=Frame(win,bg="black",width=500, height=50)
frameright.pack(side=RIGHT)

lbl_Title_of_Operation=Label(frameleft,text="Insert into MYSQL DB Demo")
lbl_Title_of_Operation.grid(row=0,columnspan=5)

lblName=Label(frameleft,text="Name").pack(side=LEFT,padx=30,pady=10)
lblName.grid(row=2,column=1,padx=30,pady=10)
lblTamil=Label(frameleft,text="Tamil").pack(side=LEFT,padx=30,pady=10)
lblTamil.grid(row=2,column=1,padx=30,pady=10)


win.mainloop()