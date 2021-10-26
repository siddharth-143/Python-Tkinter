# draw a square

from tkinter import *

root = Tk()
root.title("Line")

canvas = Canvas(root)
canvas.pack()

canvas.create_line(10, 10, 10, 100, 100, 100, 100, 10, 10, 10)

root.mainloop()