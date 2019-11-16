from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("700x500")
root.title("Radio Button tutorial")

def order():
    tmsg.showinfo("order",f"You order food {var.get()}")

# var=IntVar()

var = StringVar()
var.set("Radio")
radio=Radiobutton(root,text="Dosa",variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="idaly",variable=var,value="idaly").pack(anchor="w")
radio=Radiobutton(root,text="panir",variable=var,value="panir").pack(anchor="w")
radio=Radiobutton(root,text="samosa",variable=var,value="samosa").pack(anchor="w")

Button(root,text="Order now",command=order).pack()

root.mainloop()