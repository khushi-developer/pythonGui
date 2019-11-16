from tkinter import *
root=Tk()
root.geometry("700x500")
root.title("Satusbar tutorial")
def update():
    statusvar.set("Busy..")
    status.update()
    import time
    time.sleep(2)
    statusvar.set("Readynow")

statusvar=StringVar()
statusvar.set("Ready")
status=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")

status.pack(fill=X,side=BOTTOM)

Button(root,text="Upload",command=update).pack()

root.mainloop()