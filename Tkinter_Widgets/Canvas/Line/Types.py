# draw a types of line

from tkinter import *

root = Tk()
root.title("Line")

canvas = Canvas(root)
canvas.pack()

canvas.create_line(10, 15, 200, 15, dash=[2, 5])
canvas.create_line(10, 35, 200, 35, fill="green")
canvas.create_line(10, 55, 200, 55, width=4)

root.mainloop()