from tkinter import *
root=Tk()
root.geometry("700x500")
f1=Frame(root,bg="gray",borderwidth=10,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

l1=Label(f1,text="tkinter programs-pycharm")
l1.pack(pady=142)

f1=Frame(root,bg="gray",borderwidth=10,relief=SUNKEN)
f1.pack(side=TOP,fill="x")

l1=Label(f1,text="Welcome khushi",fg="green")
l1.pack(padx=142)



root.mainloop()