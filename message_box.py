from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.geometry("400x400")
root.resizable(width=False,height=False)

def popup():
  title = "Error"
  message = "This is type error"
  details = "This form will not be submitted because of the error encountered"
  response = messagebox.showwarning(title=title,message=message,detail=details)
  Label(root, text=response).pack()
  if response == "ok":
    Label(root, text="You clicked OK").pack()
  else:
    Label(root, text="You clicked No").pack()

Button(root, text="Popup",command=popup).pack()
Button(root,text="Quit",command=root.quit).pack()


root.mainloop()