# draw a line arc

from tkinter import *

root = Tk()
root.title("Canvas")

canvas = Canvas(root)
canvas.pack()

canvas.create_arc(20, 20, 100, 100)

root.mainloop()