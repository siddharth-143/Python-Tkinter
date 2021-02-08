from tkinter import *
root=Tk()

def open():
      
      print(spin.get())
      
      top=Toplevel(root)
      top.geometry('200x200')
      top.title('siddharth')
      
      btn1=Button(top,text='close',command=top.destroy)
      btn1.pack()
      top.mainloop()

spin=Spinbox(root,from_=0,to=10)
spin.pack()
            
btn=Button(root,text='open',command=open)
btn.pack()

root.geometry('202x202')
root.mainloop()