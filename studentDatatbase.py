from tkinter import *

def open():
    top=Toplevel()
    top.title("Details form")
    top.geometry("744x377+120+120")
    label=Label(top,text="Hello world").pack()
    
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Student database system")
        self.geometry("744x377+120+120")
        Button(self,text="Open Form",command=open).pack()

    def filldetails(self):
        Label(self,text="Hello world").pack()


if __name__ == "__main__":
    window=GUI()
    window.filldetails()
    window.mainloop()