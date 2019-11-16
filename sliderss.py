from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("700x500")
root.title("slider")

def getdollars():
    tmsg.showinfo("Congratulation",f"you get {slider.get()} dollars")
    

Label(root,text="How many dollars you want?").pack()
slider=Scale(root,orient=HORIZONTAL,tickinterval=50)
slider.set(10)
slider.pack()


Button(root,text="Get doller!",command=getdollars).pack()

root.mainloop()