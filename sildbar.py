from tkinter import *
from tkinter import simpledialog

def print_me():
      s=simpledialog.askstring('input string','entet you name')
      print(s)
root=Tk()

button=Button(root,text='button',command=print_me)
button.pack()

root.geometry('400x400')
root.mainloop()