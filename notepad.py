from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root = Tk()
root.geometry("700x500")
root.title("Untitle - Notepad")
root.wm_iconbitmap("pycharm.jpg")

def newFile():
    global file
    root.title("Untitle - Notepad")
    file = None
    textarea.delete(1.0,END)    

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt" , filetypes=[("All files","*.*"),("text document","*.txt")])

    if file == "":
        file = None

    else:
        root.title(os.path.basename(file) + "-Notepad")
        textarea.delete(1.0,END)
        f = open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitle.txt' , filetypes=[("All files","*.*"),("text document","*.txt")])
        if file == "":
            file = None

        else:
            # save as a new file
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + "- Notepad")
            print("File saved")
    else:
        # save the file
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()

def quiteApp():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("About","This notpad is developed by khushi")

menubar=Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New file",command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="save",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quiteApp)
menubar.add_cascade(label="File",menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="cut",command=cut)
editmenu.add_command(label="copy",command=copy)
editmenu.add_command(label="paste",command=paste)
menubar.add_cascade(label="Edit",menu=editmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="about us",command=about)
menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu=menubar)

textarea = Text(root)
file = None
textarea.pack(expand=True,fill=BOTH)

scrollbar = Scrollbar(textarea)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=textarea.yview)
textarea.config(yscrollcommand=scrollbar.set)
root.mainloop()