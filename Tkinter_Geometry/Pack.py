# Tkinter pack() method

from tkinter import *

root = Tk()

redButton = Button(root, text="Red", fg="red")
redButton.pack(side=LEFT)

greenButton = Button(root, text="Green", fg="green")
greenButton.pack(side=RIGHT)

blueButton = Button(root, text="Blue", fg="blue")
blueButton.pack(side=TOP)

blackButton = Button(root, text="Black", fg="black")
blackButton.pack(side=BOTTOM)

root.mainloop()