# Draw shape

from tkinter import *

root = Tk()
root.title("Shape")
root.geometry("500x500")

can = Canvas(root, bg="blue", height=500, width=500)
rect1 = can.create_rectangle(30, 10, 120, 80, fill="red", outline="white")
rect2 = can.create_rectangle(150, 10, 240, 80, fill="red", outline="white")
rect3 = can.create_rectangle(270, 10, 370, 80, fill="white", outline="red", width=4)
rect4 = can.create_rectangle(500, 10, 400, 80, fill="yellow", outline="red")

ovl = can.create_oval(15, 100, 80, 200, fill="red", outline="white", width=10)
can.pack()
root.mainloop()