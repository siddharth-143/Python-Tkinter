from tkinter import *

root = Tk()
root.geometry('250x250')

lbl = Label(root, text='List of countries')
listbox = Listbox(root)

listbox.insert(1, 'India')
listbox.insert(2, 'USA')
listbox.insert(3, 'Japan')
listbox.insert(4, 'Austrelia')

lbl.pack()
listbox.pack()


root.mainloop()