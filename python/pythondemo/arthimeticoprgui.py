from tkinter import *

app=Tk()
app.title("TYPING MASTER  PRO")
app.geometry("500x500+500+100")
app.config(bg="lightblue")

def clickresult():
    username=str(text1.get())
    password=str(text2.get())
    view=username+" "+password
    lbloutput.config(text=view ,fg="Red")
    
lblTitlee=Label(app,text="TYPING MASTER  PRO ",fg="red",font=("arial black",26))
lblTitlee.grid(row=0,column=5)   
    
lblTitle=Label(app,text="USER NAME ")
lblTitle.grid(row=4,column=2)

text1=Entry(app,width=30)
text1.grid(row=4,column=4)
    
    
lblTitle1=Label(app,text="PASSWORD")
lblTitle1.grid(row=6, column=2)

text2=Entry(app,width=30)
text2.grid(row=6, column=4)
    
lbloutput=Label(app,width=30)
lbloutput.grid(row=7,column=4,padx=10,pady=20)


clickme=Button(app, text="viewdatas", command=clickresult)
clickme.grid(row=7, column=6, padx=40, pady=40)



app.mainloop()

