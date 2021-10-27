# Display image

from tkinter import *
from tkinter import Canvas, PhotoImage

root = Tk()
root.title("Image")

can = Canvas(root)
can.pack()

logo = PhotoImage(file="Images/apple.ico")
can.create_image(20, 20, image=logo, anchor=NW)
root.mainloop()