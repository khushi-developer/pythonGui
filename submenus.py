from tkinter import *

def myfunc():
    print("this is my fun")

root=Tk()
root.geometry("600x400")
root.title("pycharm")

# mymenu = Menu(root)  #create a menu bar
# m1=mymenu.add_command(label="file",command=myfunc)  # in that menubar add commands as File, Edit ,etc
# m1=mymenu.add_command(label="Edit",command=myfunc)  # in that menubar add commands as File, Edit ,etc
# root.config(menu=mymenu)

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

root.mainloop()