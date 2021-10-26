# draw a color lineRectangle

from tkinter import *

root = Tk()
root.title("LineRectangle")

canvas = Canvas(root)
canvas.pack()

canvas.create_rectangle(20, 20, 100, 100, fill="green", outline="red")

root.mainloop()