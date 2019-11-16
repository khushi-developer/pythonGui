from tkinter import *

root = Tk()

#GUI logic is here

#width x height
root.geometry("680x420")

#width,height
root.minsize(300,50)
root.maxsize(700,900)

label1=Label(text="This is label,nd you have to pack this label")
label1.pack()

root.mainloop()
