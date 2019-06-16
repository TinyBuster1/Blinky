#import Tkinter as tk
from time import localtime

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import sys
import os
import BlinkyDataBaseManagment

global prog_call
global prog_location

prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]

def FeedbackReport():
    global prog_location
    root = tk.Tk()
    root.title("Feedback Report")
    root.geometry("500x500")
    reports = prog_location + "\Reports" + "\\" + "FeedbackReport.txt"
    with open(reports, "r") as f:
        tk.Label(root, text=f.read()).pack()
    root.mainloop()
    f.close()

def wrongPassword():
    global prog_location
    root = tk.Tk()
    root.title("Wrong Password")
    #root.geometry("500x500")
    root.geometry("600x600")
    reports = prog_location + "\Reports" + "\\" + "wrongPasswordReport.txt"
    with open(reports, "r") as f:
        tk.Label(root, text=f.read()).pack()
    root.mainloop()
    f.close()

def exceptionReport():
    global prog_location
    root = tk.Tk()
    root.title("Exception report")
    #root.geometry("500x500")
    root.geometry("600x600")

    reports = prog_location + "\Reports" + "\\" + "exceptionReport.txt"
    with open(reports, "r") as f:
        tk.Label(root, text=f.read()).pack()
    root.mainloop()
    f.close()

def statisticsReport():
    global prog_location
    root = tk.Tk()
    root.title("Statistics report")
    #root.geometry("500x500")
    root.geometry("600x600")
    reports = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
    tk.Label(root, text="Deleted:").pack()
    with open(reports, "r") as f:
        tk.Label(root, text=f.read()).pack()
    # allImages = BlinkyDataBaseManagment.getAllImages()
    # allTitles = BlinkyDataBaseManagment.getAllTitles()
    # tk.Label(root, text="----------------").pack()
    # tk.Label(root, text="Images:").pack()
    # tk.Label(root, text=allImages).pack()
    # tk.Label(root, text="total:").pack()
    # tk.Label(root, text=len(allImages)).pack()
    # tk.Label(root, text="----------------").pack()
    # tk.Label(root, text="Phrases:").pack()
    # for phrase in allTitles:
    #     tk.Label(root, text=phrase).pack()
    # tk.Label(root, text="total:").pack()
    # tk.Label(root, text=len(allTitles)).pack()
    # tk.Label(root, text="----------------").pack()
    root.mainloop()
    f.close()

def onlineUsers():
    root = tk.Tk()
    root.title("Online users")
    #root.geometry("600x600")
    root.geometry("700x700")

    allUsers = BlinkyDataBaseManagment.allUsers()
    allMentors = BlinkyDataBaseManagment.allMentors()
    allAdmins = BlinkyDataBaseManagment.allAdmins()
    tk.Label(root, text="Admins:").pack()
    tk.Label(root, text=allAdmins).pack()
    tk.Label(root, text="total:").pack()
    tk.Label(root, text=BlinkyDataBaseManagment.returnNumOfAdmins()).pack()
    tk.Label(root, text="----------------").pack()
    tk.Label(root, text="Mentors:").pack()
    tk.Label(root, text=allMentors).pack()
    tk.Label(root, text="total:").pack()
    tk.Label(root, text=BlinkyDataBaseManagment.returnNumOfMentors()).pack()
    tk.Label(root, text="----------------").pack()
    tk.Label(root, text="Users:").pack()
    tk.Label(root, text=allUsers).pack()
    tk.Label(root, text="total:").pack()
    tk.Label(root, text=BlinkyDataBaseManagment.returnNumOfUsers()).pack()
    tk.Label(root, text="----------------").pack()
    root.mainloop()


def track(x,y):
    alarms=[]
    count=[]
    temp=0
    setalarms=0
    f = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
    f.write("entry-time", localtime())
    f.close()


    if(x=='U'):
       if y in alarms:
           index1=alarms.index(y)
           temp=count.pop(index1)
           temp=temp+1
           count.insert(index1,temp)
           if(temp>3):
               setsetalarms=1
               f = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
               f.write("name-",y,"Tried to connect more than 3 times","time",localtime() )
               f.close()
               BlinkyDataBaseManagment.closeSQLconnection();
       else:
           alarms.append(y)
           count.append(1)
    elif(x=='DEL-M'):
        if y in alarms:
            index1 = alarms.index(y)
            temp = count.pop(index1)
            temp = temp + 1
            count.insert(index1, temp)
            if (temp > 3):
                setsetalarms = 1
                f = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
                f.write("name-", y, "delete mentor", "time", localtime())
                f.close()
                BlinkyDataBaseManagment.closeSQLconnection();
        else:
            alarms.append(y)
            count.append(1)
    elif(x=='DEL-U'):
        if y in alarms:
            index1 = alarms.index(y)
            temp = count.pop(index1)
            temp = temp + 1
            count.insert(index1, temp)
            if (temp > 3):
                setsetalarms = 1
                f = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
                f.write("name-", y, "delete user", "time", localtime())
                f.close()
                BlinkyDataBaseManagment.closeSQLconnection();
        else:
            alarms.append(y)
            count.append(1)
    elif (x == 'DL_PIC'):
        if y in alarms:
            index1 = alarms.index(y)
            temp = count.pop(index1)
            temp = temp + 1
            count.insert(index1, temp)
            if (temp > 3):
                setsetalarms = 1
                f = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
                f.write("name-", y, "delete pic", "time", localtime())
                f.close()
                BlinkyDataBaseManagment.closeSQLconnection();
        else:
            alarms.append(y)
            count.append(1)
    elif (x == 'UP_PIC'):
        if y in alarms:
            index1 = alarms.index(y)
            temp = count.pop(index1)
            temp = temp + 1
            count.insert(index1, temp)
            if (temp > 3):
                setsetalarms = 1
                f = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
                f.write("name-", y, "upload picture", "time", localtime())
                f.close()
                BlinkyDataBaseManagment.closeSQLconnection();
        else:
            alarms.append(y)
            count.append(1)
    elif (x == 'USER INFO'):
        if y in alarms:
            index1 = alarms.index(y)
            temp = count.pop(index1)
            temp = temp + 1
            count.insert(index1, temp)
            if (temp > 3):
                setsetalarms = 1
                f = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
                f.write("name-", y, "user information", "time", localtime())
                f.close()
                BlinkyDataBaseManagment.closeSQLconnection();
        else:
            alarms.append(y)
            count.append(1)
    elif (x == 'MEDICL_IN'):
        if y in alarms:
            index1 = alarms.index(y)
            temp = count.pop(index1)
            temp = temp + 1
            count.insert(index1, temp)
            if (temp > 3):
                setsetalarms = 1
                f = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
                f.write("name-", y, "medical information", "time", localtime())
                f.close()
                BlinkyDataBaseManagment.closeSQLconnection();
        else:
            alarms.append(y)
            count.append(1)
    elif (x == 'MEDICL_UP'):
        if y in alarms:
            index1 = alarms.index(y)
            temp = count.pop(index1)
            temp = temp + 1
            count.insert(index1, temp)
            if (temp > 3):
                setsetalarms = 1
                f = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
                f.write("name-", y, "medical update", "time", localtime())
                f.close()
                BlinkyDataBaseManagment.closeSQLconnection();
        else:
            alarms.append(y)
            count.append(1)
    else:
        pass
