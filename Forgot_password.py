import pyodbc
import tkinter
from tkinter import messagebox
import LoginAuth
import BlinkyDataBaseManagment
from doctest import master
from functools import partial
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


def Forgot_password_U():
    root = tk.Tk()
    root.title("Forgot Password")
    root.geometry("500x500")


    id_label=tk.Label(root, text="enter id:").pack()
    id_entry=tk.Entry(root,)
    id_entry.pack()

    phone_label=tk.Label(root, text="email:").pack()
    phone_entry=tk.Entry(root)
    phone_entry.pack()

    def test(id_entry,phone_entry):
        id = id_entry.get()
        email = phone_entry.get()
        print(id)
        print(email)


        #start sql
        conn = pyodbc.connect(BlinkyDataBaseManagment.mySQLserver)

        cursor = conn.cursor()


        sql=''' SELECT password
                FROM BlinkyDB.dbo.[User]
                WHERE uid=? AND email=?;'''

        cursor.execute(sql, id, email)
        row = cursor.fetchone()
        print(row)
        if(row!=None):
                LoginAuth.sendRecoveryPassword(id, email, row.password)
                messagebox.showinfo("RECOVER PASSWORD", "your password is sent to your email")
        else:
            messagebox.showinfo("RECOVER MY PASSWORD", "Incorrect password")

    ##ADD BUTTON
    action_with_args = partial(test,id_entry,phone_entry)
    #B_recover_password=tk.Button(root,text="RECOVER PASSWORD", command= action_with_args,height = 5, width =28).pack()
    B_recover_password=tk.Button(root,text="RECOVER PASSWORD", command= action_with_args,height = 5, width =28).pack()






    root.mainloop()


def Forgot_password_M(MentorID):
    root = tk.Tk()
    root.title("Forgot Password")
    root.geometry("500x500")


    UIDname_l=tk.Label(root, text="ENTER USER ID:").pack()
    Unentry=tk.Entry(root,)
    Unentry.pack()


    #temp=UserComboBox.get()

    password_l=tk.Label(root, text="ENTER NEW PASSWORD:").pack()
    password_entry=tk.Entry(root)
    password_entry.pack()

    def test(password_entry,Unentry,MentorID):
        new_password = password_entry.get()
        user_id= Unentry.get()


        conn = pyodbc.connect(BlinkyDataBaseManagment.mySQLserver)

        cursor = conn.cursor()
        sql=''' UPDATE BlinkyDB.dbo.[User]
                SET [User].password=(?)
                WHERE [User].uid=? AND [User].mid=?;'''
        cursor.execute(sql,new_password,user_id,MentorID)
        conn.commit()

        sql='''SELECT password FROM BlinkyDB.dbo.[User]
                WHERE [User].uid=? AND [User].mid=?;'''
        cursor.execute(sql,user_id, MentorID)
        row = cursor.fetchone()

        if(row!=None):
            password=str(row)
            messagebox.showinfo("REST PASSWORD", "Your password is"+password)
        else:
            messagebox.showinfo("REST PASSWORD", "A problem has occurred")



    action_with_args = partial(test, password_entry,Unentry,MentorID)
    B_recover_password=tk.Button(root,text="REST PASWORD", command= action_with_args).pack()




    root.mainloop()


def Forgot_password_A(EntryChangePass,ChooseUserIDBox):
    password=EntryChangePass.get()
    ChoosseUser=ChooseUserIDBox.get()

    conn = pyodbc.connect(BlinkyDataBaseManagment.mySQLserver)
    cursor = conn.cursor()

    sql=''' UPDATE BlinkyDB.dbo.Mentor
            SET Mentor.password=?
            WHERE Mentor.mid=?;'''

    cursor.execute(sql, password, ChoosseUser)
    conn.commit()

    sql=''' SELECT password
            FROM BlinkyDB.dbo.Mentor
            WHERE Mentor.mid=?;'''
    cursor.execute(sql, ChoosseUser)
    row = cursor.fetchone()

    if (row != None):

        messagebox.showinfo("REST PASSWORD", "NEW PASSWORD UPDATE " + password)
    else:
        messagebox.showinfo("REST PASSWORD", "A problem has occurred")







