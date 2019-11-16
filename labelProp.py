from tkinter import *
root=Tk()
root.geometry("755x555")
#importatnt label atributes
#text
#fg
#bg
#font
# 1.font=("Arebian,19,bold")
# 2.font="Arebian 19 bold"
#padx
#pady
#relief

lbl=Label(text="This is label wich represents label properties",bg="Red",fg="green",
padx="45",pady="30",font="Arebian 19 bold italic",borderwidth=10)

#important pack attributes
#anchor
#side - TOP BOTTOM LEFT RIGHT
#fill
#padx
#pady

# lbl.pack(side=TOP,anchor="nw",fill=X)
lbl.pack(side=LEFT,fill=Y,padx="20",pady="20")
# lbl.pack(side=BOTTOM,anchor="sw")
# lbl.pack(side=BOTTOM,anchor="se")


root.mainloop()