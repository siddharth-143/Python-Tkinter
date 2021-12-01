from tkinter import *

root = Tk()
root.geometry('200x250')

menubutton = Menubutton(root, text='Language', relief=FLAT)
menubutton.grid()

menubutton.menu = Menu(menubutton)
menubutton['menu'] = menubutton.menu

menubutton.menu.add_checkbutton(label='Hindi', variable=IntVar())
menubutton.menu.add_checkbutton(label='English', variable=IntVar())
menubutton.pack()
root.mainloop()