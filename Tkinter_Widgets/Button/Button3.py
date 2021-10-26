# import package
from tkinter import *

root = Tk()
root.geometry("100x100")

b = Button(root, text="Button",bd="5", command=root.destroy)
b.pack(side="top")

root.mainloop()