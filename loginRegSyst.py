from tkinter import *
import os
import tkinter.messagebox as tmsg

def save():
    name_of_note = note_name.get()
    details_of_note = note_detail.get()
    note_file=open(name_of_note,"w")
    note_file.write(details_of_note)
    note_file.close()  

def creates():
    screen4 = Toplevel()
    screen4.title("Welcome to the notes")
    screen4.geometry("700x500+120+120")
    note_nm=StringVar()
    note_details=StringVar()
    global note_name
    global note_detail
    Label(screen4,text="Enter your notes Here",font="calibri 19 bold").pack()
    Label(screen4,text="Enter name of note").pack()
    note_name = Entry(screen4,textvariable=note_nm)
    note_name.pack()
    Label(screen4,text="Enter your note here").pack()
    note_detail=Entry(screen4,textvariable=note_details)
    note_detail.pack()
    Button(screen4,text="Save", command=save).pack()
    screen4.mainloop()

def display_notes():
    global data
    note=your_note.get()
    all_notes= os.listdir()
    if note in all_notes:
        file1=open(note,"r")
        data=file1.read().splitlines()
        for item in data:   
            Label(screen5,text=item+"\n").pack()     
        file1.close()

def view_notes():
    global screen5
    screen5 = Toplevel()
    screen5.title("your Notes")
    screen5.geometry("700x500+120+120")
    Label(screen5,text="Enter name of note yopu wants to show").pack()
    mynote = StringVar()
    global your_note
    your_note=Entry(screen5,textvariable=mynote)
    your_note.pack()
    Button(screen5,text="ok",command=display_notes).pack()
    screen5.mainloop()

def del_note():
    files=os.listdir()
    You_want_delete = note_name.get()
    if You_want_delete in files:
        os.remove(You_want_delete)
        Label(screen6,text="You delete note successfully",font="calibri 15",fg="green").pack()
    else:
        Label(screen6,text="Note not availabel",font="calibri 15",fg="green").pack()

def remove_notes():
    global screen6
    screen6 = Toplevel()
    screen6.title("Remove notes")
    screen6.geometry("700x500+120+120")
    scrollbar=Scrollbar(screen6)
    scrollbar.pack(side=RIGHT,fill=Y)

    Label(screen6,text="please use one of the filename below").pack()
    all_note_files= os.listdir()
    lbx=Listbox(screen6,yscrollcommand = scrollbar.set)
    for notes in all_note_files:
        lbx.insert(END,notes)
    lbx.pack()
    scrollbar.config(command = lbx.yview)

    global note_name
    name = StringVar()
    Label(screen6,text="Delete the note which you want",font="calibri 13").pack()
    Label(screen6,text="Enter name of note you want to remove").pack()
    note_name = Entry(screen6,textvariable=name)
    note_name.pack()
    Button(screen6,text="remove note",command=del_note).pack()
    screen6.mainloop()
    
    

def session():
    screen3 = Toplevel()
    screen3.title("Welcome to the notes")
    screen3.geometry("700x500+120+120")
    Button(screen3,text="create notes",command=creates).pack()
    Button(screen3,text="view notes" , command=view_notes).pack()
    Button(screen3,text="Remove notes",command=remove_notes).pack()
    screen3.mainloop()


def login_success():
    session()

def user_not_found():
    tmsg.showerror("Error","User not found")

def password_not_recongnized():
    tmsg.showerror("Error","Password not recongnized")

def loginHere():
    List_of_files = os.listdir()
    username_of_login = usernameentry1.get()
    if username_of_login in List_of_files:
        file1=open(username_of_login,"r")
        verify=file1.read().splitlines()
        # verify=[f for f in file1]
        value=passwordentry1.get()
        if value in verify:
            login_success()
        else:
            password_not_recongnized()
        file1.close()

    else:
        user_not_found()

def registerHere():
    user_info = usernameentry.get()
    password_info = passwordentry.get()
    file=open(user_info,"w")
    file.write(user_info+"\n")
    file.write(password_info)
    file.close()

    usernameentry.delete(0,END)
    passwordentry.delete(0,END)
    Label(screen1,text="Registration success",font="calibary 10",fg="green").pack()

def register():
    global screen1
    screen1=Toplevel()
    screen1.geometry("700x500+120+120")
    screen1.title("Registration form")
    global username
    global password
    global usernameentry
    global passwordentry
    username=StringVar()
    password=StringVar()

    Label(screen1,text="Enter username").pack()
    usernameentry=Entry(screen1)
    usernameentry.pack()
    Label(screen1,text="Enter password").pack()
    passwordentry=Entry(screen1)
    passwordentry.pack()
    Button(screen1,text="Submit",command=registerHere).pack(pady=20)
    screen1.mainloop()

def login():
    global screen2
    global usernameentry1
    global passwordentry1

    userval=StringVar()
    passwordval=StringVar()

    screen2=Toplevel()
    screen2.geometry("700x500+120+120")
    screen2.title("Log in here")
    Label(screen2,text="Enter login details here",font="calibri 13 bold").pack()
    Label(screen2,text="user name").pack()
    usernameentry1=Entry(screen2,textvariable=userval)
    usernameentry1.pack()
    Label(screen2,text="password").pack()
    passwordentry1=Entry(screen2,textvariable=passwordval)
    passwordentry1.pack()
    Button(screen2,text="Login",command=loginHere).pack()
    screen2.mainloop()


def main_screen():
    screen=Tk()
    screen.geometry("700x500+120+120")
    screen.title("Login nd register")
    Label(text="Here you can login or register",font="Arebian 19").pack(pady=20)
    Button(screen,text="Login",command=login,padx=40,pady=20).pack(pady=20)
    Button(screen,text="Register",command=register,padx=40,pady=20).pack(pady=20)
    screen.mainloop() 

main_screen()