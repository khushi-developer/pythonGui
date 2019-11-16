from tkinter import *
root=Tk()
root.geometry("500x500+120+120")

def open():
    top=Toplevel()
    top.geometry("500x500+120+120")
    top.title("second gui window")
    top.mainloop()

Button(root,text="Open window",command=open).pack()
root.mainloop()