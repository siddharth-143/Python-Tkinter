# draw a 8 line

from tkinter import *

root = Tk()
root.title("Line")

canvas = Canvas(root)
canvas.pack()

point = [10, 10, 10, 100, 100, 100, 100, 10, 10, 10]
canvas.create_line(point, smooth="true", splinesteps=2)

root.mainloop()