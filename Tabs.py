"""
    Python program to implements tabs using tkinter
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tabs")
root.iconbitmap("apple.ico")
root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=1)

my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="blue tab")
my_notebook.add(my_frame2, text="red tab")

root.mainloop()