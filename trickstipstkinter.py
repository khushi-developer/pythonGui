from tkinter import *
root=Tk()
root.geometry("700x500")
root.title("Tricks")
root.wm_iconbitmap("pycharm.jpg")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")
root.mainloop()
