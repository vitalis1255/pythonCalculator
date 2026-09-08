from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title("Frame Label")
root.geometry("300x300")
root.resizable(width=False, height=False)

#create a frame
frame = LabelFrame(root, text="This is my frame...",padx=50,pady=50)
frame.pack(padx=10, pady=10)#places widgets at the center

#create a button
btn = Button(frame, text="Clear", bg="green")
btn.grid(row=0,column=0)

Quit = Button(frame, text="Quit",command=root.quit,bg="red")
Quit.grid(row=0, column=1,padx=10)

root.mainloop()