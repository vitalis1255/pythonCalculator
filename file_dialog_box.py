from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image


root = Tk()
root.title("Open Files Dialog Box")
root.geometry("300x300")
root.resizable(width=False,height=False)




#file usage
#returns name and location of the file
def click():
  root.filename = filedialog.askopenfilename(initialdir="/Desktop/My Credentials",title="Select A File",filetypes=(("png files","*.png"),("all files","*.*"),("pdf files","*.pdf"),("jpg files","*.jpg")))
  my_label = Label(root,text=root.filename)
  my_label.pack()


btn = Button(root, text="Click to select a file", command=click)
btn.pack()
Qt = Button(root, text="Quit",command=root.destroy)
Qt.pack()
root.mainloop()