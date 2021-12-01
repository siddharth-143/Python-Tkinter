from tkinter import *

root = Tk()
root.geometry('400x250')

name = Label(root, text='Name').place(x=30, y=50)
email = Label(root, text='Email').place(x=30, y=90)
password = Label(root, text='Password').place(x=30, y=130)
button1 = Button(root, text='Submit', activebackground='pink', activeforeground='blue').place(x=30, y=170)

e1 = Entry(root).place(x=80, y=50)
e2 = Entry(root).place(x=80, y=90)
e3 = Entry(root).place(x=95, y=130)
root.mainloop()