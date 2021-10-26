from tkinter import *

root = Tk()
root.title("Canvas")

canvas = Canvas(root)
canvas.pack()

canvas.create_oval(20, 20, 100, 100)

root.mainloop()