# Draw a line

from tkinter import *

root = Tk()
root.title("Canvas Line Example")
root.geometry("400x400")

canvas = Canvas(root, bg="blue", height=400, width=400)
canvas.create_line(15, 25, 200, 25)
canvas.create_line(100, 50, 400, 50)
canvas.pack()

root.mainloop()