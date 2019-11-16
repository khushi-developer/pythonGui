# from oopGui import GUI

# window=GUI()
# window.createButton("i clicked the button of GUI")
# window.mainloop()

from tkinter import *
class GUI1(Tk):
    def sbar(self):
        self.sb=Scrollbar(self)
        self.sb.pack(side=RIGHT,fill=Y)
        self.lbx=Listbox(self)
        for i in range(100):
            self.lbx.insert(END,f"item {i}")
        self.lbx.pack()
        self.sb.config(command=self.lbx.yview)
        
    def creteLabel(self):
        self.lbl=Label(self,text="This is simple label ",relief=SUNKEN)
        self.lbl.pack()
    

if __name__ == "__main__":
    window1=GUI1()
    window1.geometry("400x250")
    window1.creteLabel()
    window1.sbar()
    window1.mainloop()
    


