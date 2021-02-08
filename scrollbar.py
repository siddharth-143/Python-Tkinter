from tkinter import *
root=Tk()

frame=Frame(root)

scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=Y)

text=Text(frame,yscrollcommand=scroll.set)
for i in range(1,101):
      text.insert(END, 'list no : \n ' + str(i))
text.pack(side=LEFT)

scroll.config(command=text.yview)

frame.pack()
root.geometry('200x200')
mainloop()