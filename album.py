from tkinter import *

root = Tk()
root.geometry("700x500")

import os
path='D:\Android programs'
p=os.listdir(path)

lbl=Label(text="this are files")
lbl.pack()

for item in p:
    print(item)

print(os.getcwd())  #get current directory path
    

root.mainloop()