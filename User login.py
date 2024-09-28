from tkinter import *
#import messagebox.tkinter as messagebox
def login():
    Password=entry1.get()
    Username=entry2.get()
    if(Username=="" and Password==""):
        print("Fill it")
    elif(Username=="Ali" and Password=="1234"):
        print("Successfully login")
    else:
       print("Invalid username and password")

root=   Tk()
root.geometry("400x200")
label=Label(text="User Login",font="Arial 14 bold")
label.pack(pady=10)
label=Label(text="Username")
label.pack(anchor=W)
entry1=Entry(root)
entry1.pack()
label=Label(text="Password")
label.pack()

entry2=Entry(root)
entry2.pack()
b1=Button(root,text="Submit",command=login,padx=20,pady=10,border="3",borderwidth="2",relief=SUNKEN,font="Arial 10")
b1.pack(anchor=E,padx=20)
root.mainloop()
