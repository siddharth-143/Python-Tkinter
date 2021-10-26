# draw a arrows
import tkinter as ttk
from tkinter import *

root = Tk()
root.title("Line")

canvas = Canvas(root)
canvas.pack()

canvas.create_line(10, 15, 200, 15, arrow=ttk.LAST)
canvas.create_line(10, 35, 200, 35, arrow=ttk.BOTH)
canvas.create_line((10, 55, 200, 55), arrow=ttk.FIRST, arrowshape=[5, 5, 5])

root.mainloop()
