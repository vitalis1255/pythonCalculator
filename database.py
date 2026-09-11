from tkinter import *
import sqlite3


root = Tk()
root.title("Using Databases")
root.geometry("320x500")
root.resizable(width=False,height=False)


#create table
#cursor.execute("""CREATE TABLE addresses(
        #first_name text,
        #last_name text,
        #address text,
        #  city text,
          #  state text,
          #  zipcode integer
#)
#""")

#Edited function
def save_edited():
  #create a data base or connect to one
  conn = sqlite3.connect('address_book.db')
      
  #create a cursor
  cursor = conn.cursor()

  record_id = delete_box.get()

  #first_name is the column, while :first is the key.
  cursor.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
          'first':f_name_editor.get(),
          'last':l_name_editor.get(),
          'address':address_editor.get(),
          'city':city_editor.get(),
          'state':state_editor.get(),
          'zipcode':zipcode_editor.get(),
          'oid':record_id
        }
        )
  
  #commit to database
  conn.commit()
    
  #close connection to database
  conn.close()

  editor.destroy()#To close editor window



#create update function
def edit():
  global editor
  #create new window
  editor = Tk()
  editor.title("Update A Record")
  editor.geometry("300x180")
  editor.resizable(width=False,height=False)
  

  #create a data base or connect to one
  conn = sqlite3.connect('address_book.db')
    
  #create a cursor
  cursor = conn.cursor()

  record_id = delete_box.get()

  #query database
  cursor.execute("SELECT * FROM addresses WHERE oid = " + record_id)#oid is a primary key for identification of each item.
  records = cursor.fetchall()

  #create global variables for text box names
  global f_name_editor
  global l_name_editor
  global address_editor
  global city_editor
  global state_editor
  global zipcode_editor
  
  #create Text Entry widgets for the GUI
  f_name_editor = Entry(editor, width=30)
  f_name_editor.grid(row=0, column=1, padx=20,pady=(10,0))
  l_name_editor = Entry(editor, width=30)
  l_name_editor.grid(row=1, column=1)
  address_editor = Entry(editor, width=30)
  address_editor.grid(row=2, column=1)
  city_editor = Entry(editor, width=30)
  city_editor.grid(row=3, column=1)
  state_editor = Entry(editor, width=30)
  state_editor.grid(row=4, column=1)
  zipcode_editor = Entry(editor, width=30)
  zipcode_editor.grid(row=5, column=1)
  


  #create text labels
  f_name_label = Label(editor, text="First Name")
  f_name_label.grid(row=0,column=0,pady=(10,0))
  l_name_label = Label(editor, text="Last Name")
  l_name_label.grid(row=1,column=0)
  address_label = Label(editor, text="Address")
  address_label.grid(row=2,column=0)
  state_label = Label(editor, text="State")
  state_label.grid(row=3,column=0)
  city_label = Label(editor, text="City")
  city_label.grid(row=4,column=0)
  zipcode_label = Label(editor, text="Zipcode")
  zipcode_label.grid(row=5,column=0)

  #loop through results
  for record in records:
    f_name_editor.insert(0, record[0])
    l_name_editor.insert(0, record[1])
    address_editor.insert(0, record[2])
    city_editor.insert(0, record[3])
    state_editor.insert(0, record[4])
    zipcode_editor.insert(0, record[5])

  #Create a save button to save edited record
  edit_button = Button(editor, text="Save Record",command=save_edited)
  edit_button.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=50)

  

#Create a delete function
def Delete():

  #Databases
  #create a data base or connect to one
  conn = sqlite3.connect('address_book.db')
  
  #create a cursor
  cursor = conn.cursor()

  #delete query
  cursor.execute("DELETE from addresses WHERE oid = " + delete_box.get())
  delete_box.delete(0, END)#performs the delete action.
  
  #commit to database
  conn.commit()
  
  #close connection to database
  conn.close()


#create submit function
def submit():
  #Databases
  #create a data base or connect to one
  conn = sqlite3.connect('address_book.db')

  #create a cursor
  cursor = conn.cursor()

  #Insert into table
  cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name,:address, :state, :city, :zipcode)",
                 {
                   'f_name':f_name.get(),
                   'l_name':l_name.get(),
                   'address':address.get(),
                   'state':state.get(),
                   'city':city.get(),
                   'zipcode':zipcode.get()
                 })

  #commit to database
  conn.commit()

  #close connection to database
  conn.close()

  #create text boxes
  #delete(0,END)text disappear after clicking submit.
  f_name.delete(0, END)
  l_name.delete(0, END)
  address.delete(0, END)
  state.delete(0, END)
  city.delete(0, END)
  zipcode.delete(0, END)


#output the insert texts on the screen
def query():
  #Databases
  #create a data base or connect to one
  conn = sqlite3.connect('address_book.db')
  
  #create a cursor
  cursor = conn.cursor()

  #query database
  cursor.execute("SELECT *,oid FROM addresses")#oid is a primary key for identification of each item.
  records = cursor.fetchall()

  #loop through results
  print_records = ''
  for record in records:
    print_records += str(record[0]) + " " + str(record[1]) + " " + " \t" + str(record[6]) + "\n"

  records_label = Label(root, text= print_records)
  records_label.grid(row=13,column=0,columnspan=2)
  #print(records)

  #commit to database
  conn.commit()
  
  #close connection to database
  conn.close()
  

#create Text Entry widgets for the GUI
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20,pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)


#create text labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1,column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2,column=0)
state_label = Label(root, text="State")
state_label.grid(row=3,column=0)
city_label = Label(root, text="City")
city_label.grid(row=4,column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5,column=0)
delete_label = Label(root, text="Select ID")
delete_label.grid(row=9,column=0,pady=5)


#create a submit button
submit_button = Button(root, text="Add Record To Database",command=submit)
submit_button.grid(row=6,column=0,columnspan=2, pady=10)#ipadx=100ipadx stretches along x axis.

#Create a Query button
query_btn = Button(root, text="Show Records To Screen",command=query)
query_btn.grid(row=7, column=0,columnspan=2,padx=10,pady=10)# ipadx=137         

#Exit button
exit_button = Button(root, text="Quit",command=root.quit)
exit_button.grid(row=8,column=0,padx=100,pady=10,columnspan=2)#ipadx=137

#Create a delete button
delete_button = Button(root, text="Delete Record",command=Delete)
delete_button.grid(row=10,column=0,columnspan=2,pady=10)#ipadx=137

#create update button
edit_button = Button(root, text="Edit Record",command=edit)
edit_button.grid(row=12,column=0,columnspan=2,pady=10)

root.mainloop()