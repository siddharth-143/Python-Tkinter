# import tkiner module
from tkinter import *

from tkinter.ttk import *

root = Tk()
root.geometry("100x100")

b = Button(root, text="Click Me", command=root.destroy)
b.pack(side="top")

root.mainloop()