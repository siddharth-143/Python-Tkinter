from tkinter import *

root = Tk()
root.geometry("200x200")

c = Canvas(root, bg="pink", height="200", width="200")

arc = c.create_arc((5,10,150,200), start=0, extent=350, fill='white')
c.pack()

root.mainloop()