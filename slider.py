from tkinter import *


root = Tk()
root.title("Slider")
root.geometry("300x300")
root.resizable(width=False,height=False)

#vertical slide
vertical = Scale(root, from_=0, to=400)
vertical.pack()

#horizontal slide
horizontal = Scale(root, from_=0, to=400,orient=HORIZONTAL)
horizontal.pack()

#get the values of the horizontal slide
my_label_horizontal = Label(root, text=horizontal.get())
my_label_horizontal.pack()

#horizontal function
def slide():
  #get the values of the horizontal slide
  my_label_horizontal = Label(root, text=horizontal.get())
  my_label_horizontal.pack()
  root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

#btn for horizontal slide
btn = Button(root, text="Click Me", command=slide)
btn.pack()

root.mainloop()