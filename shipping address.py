
from tkinter import *
root =Tk()
root.geometry('1000x1500+0+0')
root.title("Shipping Address Form")

import mysql.connector

mydb=mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="Akis.123",
  database="mega")



Name=StringVar()

Label1=Label(root,text='Name:',width=20, font=('bold',15))
Label1.place(x=80,y=50)
entry1=Entry(root,textvar=Name, font=(10))
entry1.place(x=260,y=50)

Email=StringVar()
Label2=Label(root,text='Email:',width=20, font=('bold',15))
Label2.place(x=80,y=90)
entry2=Entry(root,textvar=Email, font=(10))
entry2.place(x=260,y=90)

Address=StringVar()
Label3=Label(root,text='Address:',width=20, font=('bold',15))
Label3.place(x=80,y=130)
entry3=Entry(root,textvar=Address, font=(10))
entry3.place(x=260,y=130)

State=StringVar()
Label3=Label(root,text='State:',width=20, font=('bold',15))
Label3.place(x=80,y=170)
entry3=Entry(root,textvar=State, font=(10))
entry3.place(x=260,y=170)

City=StringVar()
Label3=Label(root,text='City:',width=20, font=('bold',15))
Label3.place(x=80,y=210)
entry3=Entry(root,textvar=City, font=(10))
entry3.place(x=260,y=210)

ZipCode=StringVar()
Label3=Label(root,text='ZipCode:',width=20, font=('bold',15))
Label3.place(x=80,y=250)
entry3=Entry(root,textvar=ZipCode, font=(10))
entry3.place(x=260,y=250)

mycursor=mydb.cursor()

'''
mycursor.execute("create table ship(Name varchar(20), \
                  Email varchar(30), Address char(50), State char(20),\
                  City char(20), ZipCode integer)")
'''

def SQLPut():
    sqlName=Name.get()
    sqlEmail=Email.get()
    sqlAddress=Address.get()
    sqlState=State.get()
    sqlCity=City.get()
    sqlZipCode=ZipCode.get()
    details=(sqlName,sqlEmail,sqlAddress,sqlState,sqlCity,sqlZipCode)
    print(details)
    mycursor=mydb.cursor()
    mycursor.execute("insert into ship values(%s,%s,%s,%s,%s,%s)",details) 
    mydb.commit()
    mycursor.execute("select * from ship")

button=Button(root,text="Submit", width=20,font=(20),bg='orange', fg='black',command=SQLPut).place(x=400,y=400)
root.mainloop()
