from tkinter import *
from PIL import ImageTk ,Image

base = Tk()
base.title('Start Button')

img=ImageTk.PhotoImage(Image.open /storage/emulated/0/Download/apple_logo_PNG19697.png"))
lab=Label(image=img)
lab.pack()

button=Button(base,text='exit',command=base.quit)
button.pack()
base.mainloop()