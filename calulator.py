from tkinter import *
root=Tk()
root.geometry("400x500")

def click(event):
    global textval
    text = event.widget.cget("text")
    print(text) 

    if text=="=":
        if txtval.get().isdigit():
            value= txtval.get()
        else:
            try:
                value=eval(entervalue.get())
            except Exception as e:
                value = "Error"
        txtval.set(value)
        entervalue.update()

    elif text=="c":
        txtval.set("")
        entervalue.update()

    else:
        txtval.set(txtval.get()+text)
        entervalue.update()
        

txtval=StringVar()
entervalue=Entry(root,textvariable=txtval,font="lucida 19 bold")
entervalue.pack(fill=X,padx=10,pady=10)

f=Frame(root,bg="gray")
b=Button(f,text="9",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="8",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="7",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5)

f.pack()

f=Frame(root,bg="gray")
b=Button(f,text="6",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="5",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="4",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)
f.pack()

f=Frame(root,bg="gray")
b=Button(f,text="3",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="2",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="1",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)
f.pack()

f=Frame(root,bg="gray")
b=Button(f,text="0",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="+",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="-",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)
f.pack()

f=Frame(root,bg="gray")
b=Button(f,text="*",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="/",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="%",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)
f.pack()

f=Frame(root,bg="gray")
b=Button(f,text="=",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="c",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)

b=Button(f,text="]",padx=10,pady=10)
b.bind("<Button-1>",click)
b.pack(padx=5,pady=5,side=RIGHT)
f.pack()
root.mainloop()