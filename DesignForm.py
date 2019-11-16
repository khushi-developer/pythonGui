from tkinter import *
root=Tk()
root.geometry("644x344")

def getvals():
    with open("record.txt","a") as f:
        f.write(f"{namevalue.get()} , {phonevalue.get()} , {addressvalue.get()} , {emergencyvalue.get()} , {gendervalue.get()} ,{paymentmodevalue.get()} , {foodservicevalue.get()}\n")
    print(f"{namevalue.get()} ,\n {phonevalue.get()} ,\n {addressvalue.get()} , \n{emergencyvalue.get()} , \n{gendervalue.get()} ,\n{paymentmodevalue.get()} , \n{foodservicevalue.get()}")

Label(text="Welcome to our first form",font="Arebian 13 bold").grid(row=0,column=3)

name=Label(root,text="Name").grid()
phone=Label(root,text="phone").grid()
Address=Label(root,text="Adress").grid()
emergency=Label(root,text="emergency").grid()
gender=Label(root,text="gender").grid()
paymentmode=Label(root,text="paymentmode").grid()

namevalue=StringVar()
phonevalue=StringVar()
addressvalue=StringVar()
emergencyvalue=StringVar()
gendervalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(textvariable=namevalue).grid(row=1,column=2)
phoneentry=Entry(root,textvariable=phonevalue).grid(row=2,column=2)
addressentry=Entry(root,textvariable=addressvalue).grid(row=3,column=2)
emergencyentry=Entry(root,textvariable=emergencyvalue).grid(row=4,column=2)
genderentry=Entry(root,textvariable=gendervalue).grid(row=5,column=2)
paymententry=Entry(root,textvariable=paymentmodevalue).grid(row=6,column=2)

foodserviceentry=Checkbutton(text="Do you want to prebook food",variable=foodservicevalue).grid(row=7,column=2)

Button(text="Submit",command=getvals).grid(row=8,column=2)

root.mainloop()