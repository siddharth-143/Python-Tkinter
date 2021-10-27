# Draw a line polygon

from tkinter import *
import random

root = Tk()
root.title("Line Polygon")

can = Canvas(root)
can.pack()

points = [
    random.randrange(0, 200),
    random.randrange(0, 200),
    random.randrange(0, 200),
    random.randrange(0, 200),
    random.randrange(0, 200),
    random.randrange(0, 200),
    random.randrange(0, 200),
    random.randrange(0, 200),
    random.randrange(0, 200),
    random.randrange(0, 200)
]

can.create_polygon(points, fill="", outline="black")
root.mainloop()