from tkinter import *
import wikipedia


def get_me():
      entry_value=entry.get()
      text_value=wikipedia.summary(entry_value)
      text.insert(INSERT, text_value)

root=Tk()

frame=Frame(root)

entry=Entry(frame)


button=Button(frame,text='search',command=get_me)


entry.pack()

button.pack()

frame.pack(side=TOP)

##########

frame=Frame(root)

scroll=Scrollbar(frame)

text=Text(frame, yscrollcommand=scroll.set,wrap=WORD)


scroll.config(command=text.yview)




scroll.pack(side=RIGHT,fill=Y)

text.pack(side=LEFT)


frame.pack()

mainloop()