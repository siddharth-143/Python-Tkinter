from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("200x100")

def fun():
    messagebox.showinfo("Hello", "Green Button clicked")


b1 = Button(root, text='Green', command=fun, fg="green", activebackground="pink")
b1.pack(side=TOP)

b2 = Button(root, text="Yellow", fg="yellow", activebackground="red")
b2.pack(side=BOTTOM)

b3 = Button(root, text="Red", fg="red", activebackground="orange")
b3.pack(side=LEFT)

b4 = Button(root, text="Blue", fg="blue", activebackground="black")
b4.pack(side=RIGHT)

root.mainloop()