from tkinter import *


root = Tk()
root.title("Drop Down Menus")
root.geometry("300x300")
root.resizable(width=False,height=False)


#Drop down boxes
def get_clicked():
  my_label = Label(root, text=clicked.get())
  my_label.pack()

options = [
  "Monday", 
  "Tuesday", 
  "Wednesday", 
  "Thursday", 
  "Friday",
  "Saturday",
  "Sunday"
]

clicked = StringVar()#clicked serves as a variable

#create a default variable that appears first
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)# The use of * is to unpack the list.
drop.pack()

btn = Button(root, text="Show Selection",command=get_clicked)
btn.pack()

root.mainloop()