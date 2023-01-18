#Create a simple log in page in Tkinter that has a username and password field, as well as a 'log in' button.

from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Simple Login Page")
root.geometry("300x150")
def logIn():
    username = username_entry.get()
    password = password_entry.get()
  
    if username == 'admin' and password == 'admin':
        messagebox.showinfo("Success", "You have logged in successfully!")
        root.destroy()

username_entry = Entry(root)
username_entry.grid(row=0, column=0)
password_entry = Entry(root, show='*')
password_entry.grid(row=1, column=0)
button = Button(root, text="Log In", command=logIn)
button.grid(row=2, column=0)
root.mainloop()
