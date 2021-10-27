# Window

from tkinter import *
import random

root = Tk()
root.title("Window")
root.geometry("200x200")

def draw_line():
    points = [
        random.randrange(-10, 200),
        random.randrange(-10, 200),
        random.randrange(-10, 200),
        random.randrange(-10, 200)
    ]
    can.create_line(points)


can = Canvas(root, width=200, height=200)
can.pack()

widget = Button(can, text="Draw Line", command=draw_line)
widget.pack()
can.create_window(100, 190, window=widget)
root.mainloop()