from tkinter import *


root = Tk()
root.title("Check boxes")
root.geometry("300x300")
root.resizable(width=False,height=False)

var = IntVar()

c = Checkbutton(root, text="check this box, I dare you",variable=var)
c.pack()

c_label = Label(root, text=var.get())
c_label.pack()

#Always in front of command
def checkButton():
  c_label = Label(root, text=var.get())
  c_label.pack()

btn = Button(root,text="Check",command=checkButton)
btn.pack()

root.mainloop()