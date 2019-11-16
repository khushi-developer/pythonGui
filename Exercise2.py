from tkinter import *

def submit():
    val1=widthvalue.get()
    val2=Heightvalue.get()
    root.geometry(f"{val1}x{val2}")

root=Tk()
root.title("This is gui window resizing")
root.geometry(f"{520}x{220}")

widthvalue=StringVar()
Heightvalue=StringVar()

widthentry=Entry(root,textvariable=widthvalue).grid(row=0,column=0)
Heightentry=Entry(root,textvariable=Heightvalue).grid(row=1,column=0)



B1=Button(text="submit",command=submit).grid()

root.mainloop()