from tkinter import *

mk=Tk()
mk.title("SSLC DB")
mk.geometry("500x500+500+100") 
mk.config(bg="Aqua")

def insertf():
    pass
def updatef():
    pass
def deletef():
    pass
def resetf():
    pass
def submitf():
    pass

 

labelTitle=Label(text="Student DB",fg="brown",font=("Algerian",24))
labelTitle.grid(row=0,column=20,padx=60,pady=50)

stdname=Label(mk,text="Std Name:",fg="blue",font=("Cooper Black",12))
stdname.grid(row=2,column=10)

name=Entry(mk,width=20,fg="red",font=("12"))
name.grid(row=2,column=20)

sub1=Label(mk,text="Tamil:",fg="blue",font=("Cooper Black",12))
sub1.grid(row=3,column=10)

Tamil=Entry(mk,width=20,fg="red",font=("12"))
Tamil.grid(row=3,column=20)

sub2=Label(mk,text="English:",fg="blue",font=("Cooper Black",12))
sub2.grid(row=4,column=10)

English=Entry(mk,width=20,fg="red",font=("12"))
English.grid(row=4,column=20)

sub3=Label(mk,text="Maths:",fg="blue",font=("Cooper Black",12))
sub3.grid(row=5,column=10)

Maths=Entry(mk,width=20,fg="red",font=("12"))
Maths.grid(row=5,column=20)

sub4=Label(mk,text="Science:",fg="blue",font=("Cooper Black",12))
sub4.grid(row=6,column=10)

Science=Entry(mk,width=20,fg="red",font=("12"))
Science.grid(row=6,column=20)

sub5=Label(mk,text="Social:",fg="blue",font=("Cooper Black",12))
sub5.grid(row=7,column=10)

Social=Entry(mk,width=20,fg="red",font=("12"))
Social.grid(row=7,column=20)

Tl=Label(mk,text="Total:",fg="blue",font=("Cooper Black",12))
Tl.grid(row=8,column=10)

Total=Entry(mk,width=20,fg="red",font=("12"))
Total.grid(row=8,column=20)

button1=Button(text="Insert",command=insertf).grid(row=12,column=21)
button2=Button(text="Update",command=updatef).grid(row=12,column=22)
button3=Button(text="Delete",command=deletef).grid(row=12,column=24)
button4=Button(text="Reset",command=resetf).grid(row=12,column=26)
button5=Button(text="Submit",command=submitf).grid(row=12,column=28)

  
mk.mainloop()  