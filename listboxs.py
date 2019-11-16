from tkinter import *
root=Tk()
root.geometry("700x500")
root.title("Listbox tutorial")

lbx=Listbox(root)
lbx.insert(END,"This is variable")
lbx.pack()

for i in range(10):
    lbx.insert(END,f"item{i}")


root.mainloop()