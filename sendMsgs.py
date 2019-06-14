import AdminPanel
import GUI
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import pyodbc
import BlinkyDataBaseManagment
import LoginAuth
import hashlib
import RSA



def globalFeedBack(feedBackList):
    msg = feedBackList["FeedbackText"].get()
    if len(msg) > 0:
        messagebox.showinfo("", "your feedback have been sent!")
    else:
        messagebox.showinfo("", "cant send an empty feedback!")
        return False
    BlinkyDataBaseManagment.createCursor()
    allAdmins = BlinkyDataBaseManagment.allAdmins()
    for admin in allAdmins:
        GUI.msgDict[admin] = (admin, msg)
    return True

def sendMsgtoMentorFromAdmin(adminID,adminList):
    if len(adminList) == 0:
        return False
    #GUI.msgDict[adminList["MentorIDBox"].get()] = (adminID, adminList["EntryMsgToMentors"].get())
    #messagebox.showinfo("", "your message have been sent!")


    #######################################
    msgList = []
    originalMsg = adminList["EntryMsgToMentors"].get()
    key = b' \x0b' * 20
    #hashing the message
    result = hmac_sha1(key, originalMsg.encode('utf-8'))
    #building the msglist => KEY,ORIGINAL MSG, ENCRYPTED MSG, SENDER NAME.
    msgList.append(key)
    msgList.append(originalMsg)
    msgList.append(result.hex())
    msgList.append(adminID)
    GUI.msgDict[adminList["MentorIDBox"].get()] = (msgList) # sending the msg
    messagebox.showinfo("", "your message have been sent!")


    return True

def sendMsgtoUserFromMentor(mentorID,mentorList):
    if len(mentorList) == 0:
        return False
    msgList = []
    RSAlist = RSA.runRSA(mentorList["EntryMessageUser"].get())
    msgList.append(mentorID)
    msgList.append(RSAlist)
    GUI.msgDict[mentorList["UserComboBox"].get()] = msgList
    messagebox.showinfo("", "your message have been sent!")
    return True

def sendMsgtoMentorFromUser(userID,userList):
    if len(userList) == 0:
        return False
    global conn
    global cursor

    sql = '''SELECT mid FROM BlinkyDB.dbo.[User] WHERE uid=?'''
    conn = pyodbc.connect(BlinkyDataBaseManagment.mySQLserver)
    cursor = conn.cursor()
    mentorID = -1
    cursor.execute(sql, userID)
    for row in cursor:
        mentorID = row.mid
    msgList = []
    msgList.append(userID)
    msgList.append(userList["MedicalOrDiet"].get())
    GUI.msgDict[mentorID] = (msgList)
    messagebox.showinfo("", "your message have been sent!")
    return True

def sendEMERGENCYtoMentorFromUser(userID):
    if userID == "":
        return False
    global conn
    global cursor
    mentorID = -1
    mentorEMail = -1

    sql = '''SELECT mid FROM BlinkyDB.dbo.[User] WHERE uid=?'''
    conn = pyodbc.connect(BlinkyDataBaseManagment.mySQLserver)
    cursor = conn.cursor()
    cursor.execute(sql, userID)
    for row in cursor:
        mentorID = row.mid

    sql = '''SELECT email FROM BlinkyDB.dbo.[Mentor] WHERE mid=?'''
    conn = pyodbc.connect(BlinkyDataBaseManagment.mySQLserver)
    cursor = conn.cursor()
    cursor.execute(sql, mentorID)
    for row in cursor:
        mentorEMail = row.email

    LoginAuth.sendEMERGENCY(mentorEMail,userID)

    GUI.msgDict[mentorID] = (userID, "PRESSED EMERGENCY BUTTON")
    messagebox.showinfo("", "your message have been sent!")
    return True


def sendFeedbackToContacts(mentorID, mentorList):
    if len(mentorList) == 0:
        return False
    feedBackMSG = mentorList["SendFeedbackEntry"].get()
    userID =  mentorList["UserComboBox"].get()
    contact1 = ""
    contact2 = ""
    contactList = []

    sql = '''SELECT contact1 FROM BlinkyDB.dbo.[User] WHERE uid=?'''
    conn = pyodbc.connect(BlinkyDataBaseManagment.mySQLserver)
    cursor = conn.cursor()
    cursor.execute(sql, userID)
    for row in cursor:
        contact1 = row.contact1


    sql2 = '''SELECT contact2 FROM BlinkyDB.dbo.[User] WHERE uid=?'''
    conn = pyodbc.connect(BlinkyDataBaseManagment.mySQLserver)
    cursor = conn.cursor()
    cursor.execute(sql2, userID)
    for row in cursor:
            contact2 = row.contact2

    contactList.append(contact1)
    contactList.append(contact2)
    for i in contactList:
        LoginAuth.sendFeedbackToContact(i, userID, feedBackMSG)
    return True

import hashlib

# XOR function
def xor(x, y):
    return bytes(x[i] ^ y[i] for i in range(min(len(x), len(y))))

#HMAC function with hashing
def hmac_sha1(key_K, data):
    if len(key_K) > 64:
        raise ValueError('The key must be <= 64 bytes in length')
    padded_K = key_K + b'\x00' * (64 - len(key_K))
    ipad = b'\x36' * 64
    opad = b'\x5c' * 64
    h_inner = hashlib.sha1(xor(padded_K, ipad))
    h_inner.update(data)
    h_outer = hashlib.sha1(xor(padded_K, opad))
    h_outer.update(h_inner.digest())
    return h_outer.digest()
