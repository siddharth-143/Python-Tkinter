# Display Image

from tkinter import *
from PIL import ImageTk, Image

base = Tk()
base.title('Start Button')

img = ImageTk.PhotoImage(Image.open("Images/apple.ico"))
lab = Label(image=img)
lab.pack()

button = Button(base, text='exit', command=base.quit)
button.pack()
base.mainloop()
