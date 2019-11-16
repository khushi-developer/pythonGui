from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry("730x430")

image = Image.open("pycharm.jpg")
photo = ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()

# photo = PhotoImage(file="pycharm.png")
# label=Label(image=photo)
# label.pack()

root.mainloop()
