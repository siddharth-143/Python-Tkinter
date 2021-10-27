# Display text

from tkinter import *

root = Tk()
root.title("Text")

can = Canvas(root)
can.pack()

can.create_text(20, 20, text="Text")
can.create_text(40, 40, text="Hello World")
root.mainloop()