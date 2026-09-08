from tkinter import *
from PIL import ImageTk,Image
#using images with PIL(Python Imaging Library)


root = Tk()#create root window

my_img = ImageTk.PhotoImage(Image.open("NYSC.jpg"))#process of getting the image.
my_label = Label(image=my_img)#put the image in a label
my_label.pack()

root.mainloop()