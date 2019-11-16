from tkinter import *
root = Tk()
root.geometry("633x333")

def getval():
    print(uservalue.get())
    print(Passvalue.get())

Username=Label(text="username")
Username.grid()  #By defalut row=0 nd column=0
Password=Label(text="password").grid(row=1)

#variable classes in tkinter
#Booleanvar() ,DoubleVar() , StringVar() , IntVar()
uservalue=StringVar()
Passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue).grid(row=0,column=1)
passentry=Entry(root,textvariable=Passvalue).grid(row=1,column=1)

Button(text="Submit",command=getval).grid()

root.mainloop()