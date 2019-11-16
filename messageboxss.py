from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("700x500")
root.title("This shows dialogue box and message box")

def myfunc():
    print("this returns myfunc")

def help():
    value = tmsg.showinfo("Help","Khushi will help you")
    print(value)
    
def getval():
    msg=tmsg.askretrycancel("Divya se dosti karlo","Divya nahi manegi")
    if msg:
        print("Divya nahi manegi")
    
    else:
        print("Accha hua cancel kiya varna pitate")
    




mainmenubar=Menu(root)
submenu=Menu(mainmenubar,tearoff=0)
submenu.add_command(label="save",command=myfunc)
submenu.add_command(label="New project",command=myfunc)
submenu.add_separator()
submenu.add_command(label="save as",command=myfunc)
submenu.add_command(label="print",command=myfunc)
root.config(menu=mainmenubar)
mainmenubar.add_cascade(label="file",menu=submenu)


submenu1=Menu(mainmenubar,tearoff=0)
submenu1.add_command(label="cut",command=myfunc)
submenu1.add_command(label="copy",command=myfunc)
submenu1.add_separator()
submenu1.add_command(label="paste",command=myfunc)
submenu1.add_command(label="undo",command=myfunc)
root.config(menu=mainmenubar)
mainmenubar.add_cascade(label="Edit",menu=submenu1)


submenu1=Menu(mainmenubar,tearoff=0)
submenu1.add_command(label="Help",command=help)
submenu1.add_command(label="Befriend",command=getval)

root.config(menu=mainmenubar)
mainmenubar.add_cascade(label="Help",menu=submenu1)


root.mainloop()