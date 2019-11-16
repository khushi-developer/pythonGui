from tkinter import *
root = Tk()
root.geometry("633x433")

f1=Frame(bg="gray",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

def hello():
    print("Hello")

def Name():
    print("Khushi")

def address():
    print("Nalegaon")

def aboutyourself():
    print("I m the owner of the multinational company")

B1 = Button(f1,text="Hello",command=hello)
B1.pack(side=LEFT,padx="10")

B2 = Button(f1,text="Tell me your name",command=Name)
B2.pack(side=LEFT,padx="10")

B3 = Button(f1,text="Where u live",command=address)
B3.pack(side=LEFT,padx="10")

B4 = Button(f1,text="About your self",command=aboutyourself)
B4.pack(side=LEFT,padx="10")

root.mainloop()