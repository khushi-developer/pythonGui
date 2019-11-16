from tkinter import *
root=Tk()
root.geometry("700x500")
root.title("Scrollbar tutorial")

# for connecting scrollbar to a widget
# 1.widget(yscrollcommand = scrollbar.set)
#2.scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

lbx=Listbox(root,yscrollcommand = scrollbar.set)
for i in range(500):
    lbx.insert(END,f"item {i}")
lbx.pack(fill=BOTH)

scrollbar.config(command = lbx.yview)
root.mainloop()