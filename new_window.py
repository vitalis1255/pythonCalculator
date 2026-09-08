from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("New Window")
root.geometry("300x300")
root.resizable(width=False,height=False)

#opn function
def open():

  global first_image

  #create new window
  top = Toplevel()
  top.title('Create New Window')
  top.geometry("300x300")
  top.resizable(width=False, height=False)
  lbl = Label(top, text="Hello World")
  lbl.pack()
  btn2 = Button(top, text="close window", command=top.destroy)
  btn2.pack()

  original_image = Image.open("mypic.jpg")
  original_image_resized = original_image.resize((50,50))
  first_image = ImageTk.PhotoImage(original_image_resized)
  label = Label(top, image=first_image)
  label.pack()


#using button to control the second window
btn = Button(root, text="open second window", command=open)
btn.pack()


root.mainloop()