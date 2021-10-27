# Line Ex

from tkinter import *

root = Tk()
root.title("LineEx")
root.geometry("500x500")

can = Canvas(root, bg="blue", height=500, width=500)
line = can.create_line(15, 25, 200, 25, dash=(4, 2))
line1 = can.create_line(100, 50, 400, 50)
tri = can.create_line(55, 85, 155, 85, 105, 180, 55, 85)

can.pack()

root.mainloop()