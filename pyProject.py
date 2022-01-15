from tkinter import *
import tkinter

from tkinter import messagebox
import pymysql

window= tkinter.Tk() #for making the output window
window.geometry("1200x700")
window.configure(bg='white') #background colour
window.title("student info project")
L= Label(window, text="STUDENT INFO ", font=('arial',20), fg='black', anchor=CENTER) #fg is text colour. bg is background colour
L.grid(row=0, column=0, padx=20, pady=20)

# for the text to be displayed
L1= Label(window, text="enter student id: ", font=('arial',20), fg='blue') #fg is text colour. bg is background colour
L1.grid(row=1, column=0)
E= Entry(window, bd=5, width=50)
#for the input column
E.grid(row=1, column=1, padx=20, pady=20)

#for student email

L2= Label(window, text="enter student email: ", font=('arial',20), fg='blue') #fg is text colour. bg is background colour
L2.grid(row=2, column=0)
E1= Entry(window, bd=5, width=50)
E1.grid(row=2, column=1, padx=20, pady=20)


L3= Label(window, text="enter student name: ", font=('arial',20), fg='blue')
L3.grid(row=3, column=0)
E2= Entry(window, bd=5, width=50)
E2.grid(row=3, column=1, padx=20, pady=20)

L4= Label(window, text="enter student password: ", font=('arial',20), fg='blue')
L4.grid(row=4, column=0)
E3= Entry(window, bd=5, width=50)
E3.grid(row=4, column=1, padx=20, pady=20)


#making a function for working of button logic
def myButtonEvent(selection):
    print("student id is: ", E.get())
    print("student email is: ", E1.get())
    print("student name is: ", E2.get())
    print("student password is: ", E3.get())

    #getting values for inserting
    id=E.get()
    email=E1.get()
    name=E2.get()
    password=E3.get()

    if selection in ("Insert"):
        
        con= pymysql.connect(host='localhost',
        user='****', 
        password = "****",
        db='practicepython')     #localhost because it will run in local machine.
                                 #name of database is practicepython
        curr=con.cursor()

    #to test if cursor is working
    #curr.execute("select version()")
    #data=curr.fetchone()
    #print("my sql database version:-- ", data)
        
        query= "create table if not exists newstudent(id int primary key, email char(20) not null unique, name char(30) not null, password char(20) not null)" 
        curr.execute(query)
        con.commit()
        print("create table query executed")
        insertquery="INSERT INTO newstudent (id, email, name, password) VALUES ('%s', '%s', '%s', '%s')"%(id, email, name, password)

        #vals=(E.get(), E1.get(), E2.get())
        try:
            curr.execute(insertquery)
            #if using vals then curr.execute(insertquery, vals)
            con.commit()

            print("insertion query executed: ", id, email, ", ", name,", ", password)
            
            con.close()
            print("------------------------------------------------------------------")
        except Error as e:
            print("error during insertion is ",e)
            con.rollback()
            con.close()
            print("------------------------------------------------------------------")


    #updating student info depending on id
    elif selection in ("Update"):
        try:
            updatequery="update newstudent set name='%s'"%(name)+", password= '%s'"%(password)+", email = '%s'"%(email)+" where id = '%s'"%(id)
          
            con= pymysql.connect(host='localhost',
            user='root', 
            password = "root",
            db='practicepython')
             
            curr=con.cursor()   #declaring cursor ie. curr
            curr.execute(updatequery)
            con.commit()
            con.close()
            print("student updated successfully for mail id: ",id )
            print("------------------------------------------------------------------")

        except Error as e:
            print("error during updation is ",e)
            con.rollback()
            con.close()
            print("------------------------------------------------------------------")


#deleting student data
    elif selection in ("Delete"):
        try:
            deletequery="delete from newstudent where id='%s'"%(id)
          
            con= pymysql.connect(host='localhost',
            user='root', 
            password = "root",
            db='practicepython')
            curr=con.cursor()
            curr.execute(deletequery)
            con.commit()
            con.close()
            print("student deleted successfully for id: ",id )
            print("------------------------------------------------------------------")

        except:
            print("error in delete")
            con.rollback()
            con.close()
            print("------------------------------------------------------------------")

#show student data
    elif selection in ("Select"):
        try:
            selectquery="select * from newstudent where id='%s'"%(id)
          
            con= pymysql.connect(host='localhost',
            user='root', 
            password = "root",
            db='practicepython')
            curr=con.cursor()
            curr.execute(selectquery)
            rows=curr.fetchall()
            email1=''
            name1=''
            password1=''
            for row in rows:
                email1=row[1]
                name1 = row[2]
                password1 =row[3]
            E1.delete(0,END)
            E2.delete(0,END)
            E3.delete(0,END)

            E1.insert(0,email1)
            E2.insert(0,name1)
            E3.insert(0,password1)
           
            con.close()
            print("student details displayed" )
            print("------------------------------------------------------------------")

        except:
            print("error in delete")
            con.close()
            print("------------------------------------------------------------------")


        

            
            
#for the button
BInsert = tkinter.Button(text="Insert student details", fg="black", bg="orange",
                         font=('arial',20,'bold'), command=lambda:myButtonEvent('Insert'))   
BInsert.grid(row=8, column=0, padx=20, pady=20)

BUpdate = tkinter.Button(text="update student", fg="black", bg="orange", font=('arial',20,'bold'), command=lambda:myButtonEvent('Update'))   
BUpdate.grid(row=8, column=2)

BDelete = tkinter.Button(text="delete student with id", fg="black", bg="orange", font=('arial',20,'bold'), command=lambda:myButtonEvent('Delete'))   
BDelete.grid(row=10, column=0)

BSelect = tkinter.Button(text="print student info with id", fg="black", bg="orange", font=('arial',20,'bold'), command=lambda:myButtonEvent('Select'))   
BSelect.grid(row=10, column=2)
                          



mainloop()
