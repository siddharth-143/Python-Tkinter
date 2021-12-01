import tkinter as tk
from functools import partial


def findsum(l3, num1, num2):
    n1 = int(num1.get())
    n2 = int(num2.get())
    n3 = n1 + n2
    l3.config(text="Result = %d" % n3)
    return


root = tk.Tk()
root.title("Xiith.com")
root.geometry("700x500")

number1 = tk.StringVar()
number2 = tk.StringVar()

l1 = tk.Label(root, text="Enter 1st number").place(x=20, y=60)
l2 = tk.Label(root, text="Enter 2nd number").place(x=20, y=120)
t1 = tk.Entry(root, textvariable=number1).place(x=200, y=60)
t2 = tk.Entry(root, textvariable=number2).place(x=200, y=120)

labelResult = tk.Label(root)
labelResult.place(x=250, y=200)

findsum = partial(findsum, labelResult, number1, number2)

b1 = tk.Button(root, text="ADD", command=findsum).place(x=200, y=300)
b2 = tk.Button(root, text="Cancel", command=root.destroy).place(x=250, y=300)

root.mainloop()