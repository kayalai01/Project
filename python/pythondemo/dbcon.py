from tkinter import *
import mysql.connector

mk=Tk()
mk.title("SSLC DB")
mk.geometry("500x500+500+100") 
mk.config(bg="white")


def MyDBConnection():
    dbcon=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_kayal"
    )
    return dbcon

dbcon=MyDBConnection()
print("connected",dbcon)
    
def insertf():
    stdname=str(name.get())
    Tamil=int(tbTamil.get())
    English=int(tbEnglish.get())
    Maths=int(tbMaths.get())
    Science=int(tbScience.get())
    Social=int(tbSocial.get())
    Total=int(tbTotal.get())
    
    e_con=MyDBConnection()
    result=e_con.cursor()
    
    statement="insert into Student_DB(Std_name,Tamil,English,Maths,Science,Social,Total) values (%s,%s,%s,%s,%s,%s,%s);"
    valuepass=(stdname,Tamil,English,Maths,Science,Social,Total)
    result.execute(statement,valuepass)
    e_con.commit()
    
    print (result.rowcount,"rowinsert")
    
    
    
    
def updatef():
    pass
def deletef():
    pass
def resetf():
    pass
def submitf():
    pass

 

labelTitle=Label(text="Student_DB",fg="brown",font=("Algerian",24))
labelTitle.grid(row=0,column=20,padx=60,pady=50)

stdname=Label(mk,text="Std_Name:",fg="blue",font=("Cooper Black",12))
stdname.grid(row=2,column=10)

name=Entry(mk,width=20,fg="red",font=("12"))
name.grid(row=2,column=20)

sub1=Label(mk,text="Tamil:",fg="blue",font=("Cooper Black",12))
sub1.grid(row=3,column=10)

tbTamil=Entry(mk,width=20,fg="red",font=("12"))
tbTamil.grid(row=3,column=20)

sub2=Label(mk,text="English:",fg="blue",font=("Cooper Black",12))
sub2.grid(row=4,column=10)

tbEnglish=Entry(mk,width=20,fg="red",font=("12"))
tbEnglish.grid(row=4,column=20)

sub3=Label(mk,text="Maths:",fg="blue",font=("Cooper Black",12))
sub3.grid(row=5,column=10)

tbMaths=Entry(mk,width=20,fg="red",font=("12"))
tbMaths.grid(row=5,column=20)

sub4=Label(mk,text="Science:",fg="blue",font=("Cooper Black",12))
sub4.grid(row=6,column=10)

tbScience=Entry(mk,width=20,fg="red",font=("12"))
tbScience.grid(row=6,column=20)

sub5=Label(mk,text="Social:",fg="blue",font=("Cooper Black",12))
sub5.grid(row=7,column=10)

tbSocial=Entry(mk,width=20,fg="red",font=("12"))
tbSocial.grid(row=7,column=20)

Tl=Label(mk,text="Total:",fg="blue",font=("Cooper Black",12))
Tl.grid(row=8,column=10)

tbTotal=Entry(mk,width=20,fg="red",font=("12"))
tbTotal.grid(row=8,column=20)

button1=Button(text="Insert",command=insertf).grid(row=12,column=21)
button2=Button(text="Update",command=updatef).grid(row=12,column=22)
button3=Button(text="Delete",command=deletef).grid(row=12,column=24)
button4=Button(text="Reset",command=resetf).grid(row=12,column=26)
button5=Button(text="Submit",command=submitf).grid(row=12,column=28)

  
mk.mainloop()  