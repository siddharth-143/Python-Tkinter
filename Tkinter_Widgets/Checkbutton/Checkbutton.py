from tkinter import *

root = Tk()

checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()

ck1 = Checkbutton(root, text="C/C++", variable=checkvar1, onvalue=1, offvalue=0, height=5, width=20)
ck2 = Checkbutton(root, text="Python", variable=checkvar2, onvalue=1, offvalue=0, height=5, width=20)
ck3 = Checkbutton(root, text="Java", variable=checkvar3, onvalue=1, offvalue=0, height=5, width=20)

ck1.pack()
ck2.pack()
ck3.pack()

root.mainloop()