from tkinter import *
root=Tk()

CanvasHeight=300
CanvasWidth=500

root.geometry(f"{CanvasWidth}x{CanvasHeight}")
can_widget=Canvas(root,width=CanvasWidth,height=CanvasHeight)
can_widget.pack()

can_widget.create_line(0,0,800,450,fill="red")
can_widget.create_line(0,400,800,0,fill="red")

# can_widget.create_rectangle(0,0,200,200,fill="blue")
can_widget.create_oval(150,20,250,100,fill="orange")

can_widget.create_arc(100,100,250,250,fill="red")


root.mainloop()