# draw a flower arc

from tkinter import *
import tkinter as ttk

root = Tk()
root.title("Canvas")

canvas = Canvas(root)
canvas.pack()

canvas.create_arc(20, 20, 100, 100, extent=45, start=60)
canvas.create_arc(20, 20, 100, 100, extent=45, start=180)
canvas.create_arc(20, 20, 100, 100, extent=45, start=300)

root.mainloop()