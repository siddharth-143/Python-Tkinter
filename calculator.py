from tkinter import *

root=Tk()
root.title('calculator')
root.geometry('300x500+20+20')

def enternum(x):
      if entry_box.get()=='0':            
            entry_box.delete(0,'end')
            entry_box.insert(0,str(x))
      else:
            length=len(entry_box.get())
            entry_box.insert(length,str(x))

# entert
entry_box=Entry(font='verdana 16 bold',width=18,bd=6, justify=RIGHT,bg='#e6e6fa')
entry_box.insert(0,'0')
entry_box.place(x=35,y=50)

btn_num=[ ]
for i in range(10):
      btn_num.append(Button(width=4,text=str(i),bd=6, command=lambda x=i:enternum(x)))

btn_text=9
for i in range(0,3):
      for j in range(0,3):
            btn_num[btn_text].place(x=30+j*170,y=200+i*100)
            btn_text-=1

root.mainloop()