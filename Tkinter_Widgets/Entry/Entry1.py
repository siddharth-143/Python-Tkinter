from tkinter import *

root = Tk()
root.geometry('400x400')

name_var = StringVar()
passw_var = StringVar()

def submit():
    name = name_var.get()
    password = passw_var.get()

    print('The name is : ', name)
    print('The Password is : ', password)


name_label = Label(root, text='Username')
name_entry = Entry(root, textvariable=name_var)

passw_label = Label(root, text='Password')
passw_entry = Entry(root, textvariable=passw_var)

sub_btn = Button(root, text='Submit', command=submit)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

root.mainloop()