# draw a lineRectangle

from tkinter import *

root = Tk()
root.title("LineRectangle")

canvas = Canvas(root)
canvas.pack()

canvas.create_rectangle(20, 20, 100, 100)

root.mainloop()