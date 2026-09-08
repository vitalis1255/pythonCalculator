from tkinter import *
from PIL import ImageTk,Image

root = Tk()#root window
root.title("Image App")
root.geometry("140x110")
root.resizable(width=False, height=False)

#Image one
original_img1 = Image.open("NYSC.jpg")
my_img1_resized = original_img1.resize((50,50))
my_img1 = ImageTk.PhotoImage(my_img1_resized)

#Image two
original_img2 = Image.open("APPLICATION INFO.jpg")
my_img2_resized = original_img2.resize((50,50))
my_img2 = ImageTk.PhotoImage(my_img2_resized)

#Image three
original_img3 = Image.open("ATTESTATION.jpg")
my_img3_resized = original_img3.resize((50,50))
my_img3 = ImageTk.PhotoImage(my_img3_resized)

#Image four
original_img4 = Image.open("Degree.jpg")
my_img4_resized = original_img4.resize((50,50))
my_img4 = ImageTk.PhotoImage(my_img4_resized)

#Image five
original_img5 = Image.open("mypic.jpg")
my_img5_resized = original_img5.resize((50,50))
my_img5 = ImageTk.PhotoImage(my_img5_resized)

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

#bd=border,SUNKEN is used to make a widget pressed down
status = Label(root, text="image 1 of " + str(len(img_list)), bd=2, relief=SUNKEN,padx=10, anchor=E)#anchor=position the label status to East.

#First Image body show
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0,columnspan=3)

def forward(image_number):
  global my_label
  global button_forward
  global button_back
  #global status

  my_label.grid_forget()#makes images to disappear from the screen
  my_label = Label(image=img_list[image_number - 1])
  button_forward = Button(root, text=">>", command=lambda:forward(image_number + 1))
  button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

  if image_number == 5:
    button_forward = Button(root, text=">>", state=DISABLED)

  #update the arrangement of the buttons and label in the forward function
  my_label.grid(row=0, column=0,columnspan=3)
  button_back.grid(row=1, column=0)
  button_forward.grid(row=1, column=2)

  #update the status bar in the forward function
  status = Label(root, text="image" + " " + str(image_number) + " " +  "of " + str(len(img_list)), bd=2, relief=SUNKEN,padx=10, anchor=E)#anchor=position the label status to East.
  status.grid(row=2,column=0, columnspan=3,pady=3,sticky=(W + E))

  
def back(image_number):
  global my_label
  global button_forward
  global button_back

  my_label.grid_forget()
  my_label = Label(image=img_list[image_number - 1])
  button_forward = Button(root, text=">>", command=lambda:forward(image_number + 1))
  button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

   #Disabble if image_number reduced to 1
  if image_number == 1:
    button_back = Button(root, text="<<", state=DISABLED)

  #update arragement of the buttons in the back function
  my_label.grid(row=0, column=0,columnspan=3)
  button_back.grid(row=1, column=0)
  button_forward.grid(row=1, column=2)

  #update status bar in the back function
  status = Label(root, text="image" + " " + str(image_number) +  " " +  "of " + str(len(img_list)), bd=2, relief=SUNKEN,padx=10, anchor=E)#anchor=position the label status to East.
  status.grid(row=2,column=0, columnspan=3,pady=3,sticky=(W + E))

  
#create button
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program",command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

#Arrange the buttons
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2,column=0, columnspan=3,pady=3,sticky=(W + E))



#Execute the program
root.mainloop()