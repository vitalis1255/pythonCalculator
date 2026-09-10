from tkinter import *
import sqlite3


root = Tk()
root.title("Using Databases")
root.geometry("300x300")
root.resizable(width=False,height=False)

#Databases

#create a data base or connect to one
conn = sqlite3.connect('address_book.db')

#create a cursor
cursor = conn.cursor()

#create table
cursor.execute("""CREATE TABLE addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
)
""")

#commit to database
conn.commit()

#close connection to database
conn.close()


root.mainloop()