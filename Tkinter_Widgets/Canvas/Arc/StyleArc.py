# draw a line arc with different

from tkinter import *
import tkinter as ttk

root = Tk()
root.title("Canvas")

canvas = Canvas(root)
canvas.pack()

canvas.create_arc(20, 20, 100, 100, style=ttk.PIESLICE)
canvas.create_arc(20, 70, 100, 150, style=ttk.ARC)
canvas.create_arc(20, 120, 100, 200, style=ttk.CHORD)

root.mainloop()