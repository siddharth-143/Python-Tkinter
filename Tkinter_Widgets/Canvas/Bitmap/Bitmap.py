# Display bitmap

from tkinter import *

root = Tk()
root.title("Bimap")

bitmap = [
    "error",
    "gray75",
    "gray50",
    "gray25",
    "gray12",
    "hourglass",
    "info",
    "questhead",
    "question",
    "warning",
]

can = Canvas(root, width=200, height=len(bitmap) * 32 + 32)
can.pack()

for i in range(0, len(bitmap)):
    can.create_bitmap(100, ((i+1) * 32), bitmap=bitmap[i], anchor=CENTER)

root.mainloop()