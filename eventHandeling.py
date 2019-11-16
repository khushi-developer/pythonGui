from tkinter import *
root=Tk()
root.geometry("400x300")

def harry(events):
    print(f"Button clicks on {events.x} {events.y}")

#events in tkinter
B1 = Button(root,text="Click me please")
B1.pack()

B1.bind('<Button-1>',harry)
B1.bind('<Double-1>',quit)

root.mainloop()