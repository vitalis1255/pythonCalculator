from tkinter import *

root = Tk()
root.title("Radio Buttons")
root.geometry("400x400")
root.resizable(width=False, height=False)

#declare r variable
#r = IntVar()#store value=1 and value=2 here
#r.set("2")

MODES = [
  #("properties","values")
  ("Pepperonl","Pepperonl"),
  ("Cheese","Cheese"),
  ("Mushroom","Mushroom"),
  ("Onions","Onions"),
]

pizza = StringVar()#store the modes here
pizza.set("Pepperonl")

for properties, values in MODES:
  Radiobutton(root, text=properties,variable=pizza,value=values,anchor=W).pack()#pizza will be selecting the values when the radio button is clicked.

def clicked(value):
  mylabel = Label(root, text=value)
  mylabel.pack()

#create a radio button
#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r,  value=2,command=lambda: clicked(r.get())).pack()#variable is what brings out when you click radio button while value=1 and value=2 will be displaying.



#display the value
#mylabel = Label(root, text=r.get())
#mylabel.pack()

#display the lists of for loop
mylabel = Label(root, text=pizza.get())
mylabel.pack()

myButton = Button(root, text="Click Me",command=lambda:clicked(pizza.get()))
myButton.pack()


root.mainloop()