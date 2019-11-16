from tkinter import *
from datetime import datetime
root=Tk()
root.geometry("600x600")
label1=Label(text="INDIA-NEWS",font="comicsansns 19 bold")
label1.pack()
label2=Label(text=f"Date {datetime.now().date()}",font="comicsansns 19 bold")
label2.pack()
j=int(input("Enter How many,,png file you have"))
for i in range(j):
    file=open(f"{i+1}.txt")
    for line in (x.strip() for x in file):
        label3 = Label(text=f"{i+1}.{line}", font="comicsansns 15 italic")
        label3.pack(anchor="nw")
    file.close()
root.mainloop()