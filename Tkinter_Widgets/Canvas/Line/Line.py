# draw a line

from tkinter import *

root = Tk()
root.title("Line")

canvas = Canvas(root)
canvas.pack()

canvas.create_line(10, 10, 150, 50)

root.mainloop()
