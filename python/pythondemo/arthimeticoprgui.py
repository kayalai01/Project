
from tkinter import *

win=Tk()
win.title("CALCULATOR")
win.geometry("500x500+500+100")
win.config(bg="lightblue")


def names():
    fn=str(a.get())
    ln=str(b.get())
    fullname=fn+" "+ln
    print(fullname)
    labeloutput1.config(text=fullname)

def Add():
    fn=int(a.get())
    ln=int(b.get())
    fullname=fn+ln
    print(fullname)
    labeloutput1.config(text=fullname)

def Sub():
    fn=int(a.get())
    ln=int(b.get())
    fullname=fn-ln
    print(fullname)
    labeloutput1.config(text=fullname)

def Multiple():
    fn=int(a.get())
    ln=int(b.get())
    fullname=fn*ln
    print(fullname)
    labeloutput1.config(text=fullname)

def Divid():
    fn=int(a.get())
    ln=int(b.get())
    fullname=fn/ln
    print(fullname)
    labeloutput1.config(text=fullname)
    
def modulus():
    fn=int(a.get())
    ln=int(b.get())
    fullname=fn%ln
    print(fullname)
    labeloutput1.config(text=fullname)
    
def Exponentiation():
    fn=int(a.get())
    ln=int(b.get())
    fullname=fn**ln
    print(fullname)
    labeloutput1.config(text=fullname)  
  
def Floordivision():
    fn=int(a.get())
    ln=int(b.get())
    fullname=fn//ln
    print(fullname)
    labeloutput1.config(text=fullname)
    

    
labelTitle =Label(win,text="ARTHEMITIC OPERATION",fg="Brown",font=("Algerian",24))
labelTitle.grid(row=0,column=20,padx=60,pady=50)

labelmsg=Label(win,text="Enter a value:",fg="blue",font=("Cooper Black",12))
labelmsg.grid(row=2,column=10)

a=Entry(win,width=50,fg="red",font=("12"))
a.grid(row=2,column=20)

labelmsg=Label(win,text="Enter b value:",fg="blue",font=("Cooper Black",12))
labelmsg.grid(row=5,column=10)

b=Entry(win,width=50,fg="red",font=("12"))
b.grid(row=5,column=20)

outputbox=Label(win,text="Output:",fg="blue",font=("Cooper Black",12))
outputbox.grid(row=8,column=10)

labeloutput1=Label(win,width=50,font=("12"))
labeloutput1.grid(row=8,column=20)
    
btncnct1=Button(win,text="Concatenate",command=names,fg="orange",font=("Cooper Black",12))
btncnct1.grid(row=30,column=4)

btncnct2=Button(win,text="Addition",command=Add,fg="orange",font=("Cooper Black",12))
btncnct2.grid(row=30,column=6)

btncnct3=Button(win,text="Subtraction",command=Sub,fg="orange",font=("Cooper Black",12))
btncnct3.grid(row=30,column=8)

btncnct4=Button(win,text="Multiplication",command=Multiple,fg="orange",font=("Cooper Black",12))
btncnct4.grid(row=30,column=10)

btncnct5=Button(win,text="Divition",command=Divid,fg="orange",font=("Cooper Black",12))
btncnct5.grid(row=30,column=12)

btncnct6=Button(win,text="modulus",command=Divid,fg="orange",font=("Cooper Black",12))
btncnct6.grid(row=30,column=14)
  
btncnct7=Button(win,text="Exponentiation",command=Divid,fg="orange",font=("Cooper Black",12))
btncnct7.grid(row=30,column=16)

btncnct8=Button(win,text="Floordivision",command=Divid,fg="orange",font=("Cooper Black",12))
btncnct8.grid(row=30,column=18)
  
  
win.mainloop()    



  







  


