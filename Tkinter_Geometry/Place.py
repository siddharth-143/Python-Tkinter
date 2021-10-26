# Tkinter place method

from tkinter import *

root = Tk()
root.geometry("400x250")

name = Label(root, text="Name").place(x=30, y=50)
e1 = Entry(root).place(x=80, y=50)

email = Label(root, text="Email").place(x=30, y=90)
e2 = Entry(root).place(x=80, y=90)

password = Label(root, text="Password").place(x=30, y=130)
e3 = Entry(root).place(x=95, y=130)

root.mainloop()