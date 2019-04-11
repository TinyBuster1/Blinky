import pyodbc
import os
from shutil import copyfile
import sys
import GUIandDBCommunication
import Tkinter as tk
import tkMessageBox
import datetime


global conn
global cursor
global prog_call
global prog_location

prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
loginFlag = 0

def createCursor():
    global conn
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-L7B6A755;'
                          'Database=BlinkyDB;'
                          'Trusted_Connection=yes;')
    global cursor
    cursor = conn.cursor()

def userChecker(id, password):
    global cursor
    params = (id, password)
    sql = '''SELECT * FROM BlinkyDB.dbo.Admins WHERE id=? AND password=?'''
    cursor.execute(sql, params)
    for row in cursor:
        if row.id == id and row.password == password:
            print('Wellcome back Admin ' + row.id)
            return 1
    sql = '''SELECT * FROM BlinkyDB.dbo.Mentor WHERE mid=? AND password=?'''
    cursor.execute(sql, params)
    for row in cursor:
        if row.mid == id and row.password == password:
            print('Hello Mentor ' + row.mid)
            return 2
    sql = '''SELECT * FROM BlinkyDB.dbo.[User] WHERE uid=? AND password=?'''
    cursor.execute(sql, params)
    for row in cursor:
        if row.uid == id and row.password == password:
            print('Wellcome ' + row.uid)
            return 3
    return 0

def login(userid, password):
        userType = userChecker(userid, password)
        if userType == 1:
            # here do the transfer to admin page
            print("Admin login success!")
        elif userType == 2:
            # here do the transfer to mentor page
            print("Mentor login success!")
        elif userType == 3:
            # here do the transfer to user page
            print("User login success!")
        else:
            print("wrong id or password please try again!")

def loginMentor(userid, password):
    cursor.execute('SELECT * FROM BlinkyDB.dbo.[Mentor] WHERE id=? AND password=?', (userid, password))
    for data in cursor:
        if data.id == userid and data.password == password:
            print("login success!")
        else:
            print("wrong id or password please try again!")

def loginUser(userid, password):
    cursor.execute('SELECT * FROM BlinkyDB.dbo.[User] WHERE id=? AND password=?', (userid, password))
    for data in cursor:
        if data.id == userid and data.password == password:
            print("login success!")
        else:
            print("wrong id or password please try again!")
            tkMessageBox.showinfo("error", "wrong id or password please try again!")

def midCheck(mid):
    global conn
    global cursor
    sql = '''SELECT mid FROM BlinkyDB.dbo.Mentor WHERE mid=?'''

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-L7B6A755;'
                          'Database=BlinkyDB;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    #row = cursor.fetchone()

    cursor.execute(sql, mid)
    for row in cursor:
        if row.mid == mid:
            return False
    return True

def registerMentor(mid, password, conpassword, firstName, lastName, phone):
    if password != conpassword:
        tkMessageBox.showinfo("error", 'password not match!, please repeat the password again.')
        return 1
    if midCheck(mid):
        sql1 = '''INSERT INTO BlinkyDB.dbo.Mentor (mid, password, firstName, lastName, phone) VALUES (?,?,?,?,?)'''
        params = (mid, password, firstName, lastName, phone)  # tuple containing parameter values
        cursor.execute(sql1, params)
        conn.commit()
        tkMessageBox.showinfo("", 'mentor register successfully!')
        return 0
    else:
        tkMessageBox.showinfo("error", 'mid already used by other mentor, please choose a different one!')

def uidCheck(uid):

    sql = '''SELECT uid FROM BlinkyDB.dbo.[User] WHERE uid=?'''

    global conn
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-L7B6A755;'
                          'Database=BlinkyDB;'
                          'Trusted_Connection=yes;')
    global cursor
    cursor = conn.cursor()
    cursor.execute(sql, uid)

    row=cursor.fetchone()

    for row in cursor:
        if row.uid == uid:
            return False
    return True

def registerUser(uid, password, firstName, lastName, mid, age, gender, birthday, phone, address, contact1, contact2, medical, diet):
    global cursor
    if uidCheck(uid) and not midCheck(mid):
        sql1 = '''INSERT INTO BlinkyDB.dbo.[User] (uid, password, firstName, lastName, mid, age, gender, birthday, phone, address, contact1, contact2, medical, diet) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        params = (uid, password, firstName, lastName, mid, age, gender, birthday, phone, address, contact1, contact2, medical, diet)  # tuple containing parameter values
        cursor.execute(sql1, params)
        conn.commit()
        sql2 = '''INSERT INTO BlinkyDB.dbo.Patients VALUES (?,?)'''
        params = (uid, mid)  # tuple containing parameter values
        cursor.execute(sql2, params)
        conn.commit()
        tkMessageBox.showinfo("",'user register successfully!')
        return 0
    elif(uidCheck(uid)==False):
        tkMessageBox.showinfo("error",'user id already used by other user, please choose a different one!')
    elif(midCheck(mid)==True):
        tkMessageBox.showinfo("error",'mentor id is not exist!, please provide a valid mentor.')

def patientsCheck(uid, mid):
    global cursor
    sql = '''SELECT uid, mid FROM BlinkyDB.dbo.Patients WHERE uid=? AND mid=?'''
    cursor.execute(sql, (uid, mid))
    for row in cursor:
        if row.uid == uid and row.mid == mid:
            return True
    return False

def imageCheck(imagesID):
    sql = '''SELECT imagesID FROM BlinkyDB.dbo.Images WHERE imagesID=?'''
    cursor.execute(sql, imagesID)
    for row in cursor:
        if row.imagesID == imagesID:
            return True
    return False

def uploadImage(imagesID, name, role, link, uid, mid):
    global cursor
    if not uidCheck(uid) and not midCheck(mid):
        if patientsCheck(uid, mid) and not imageCheck(imagesID):
            sql1 = '''INSERT INTO BlinkyDB.dbo.Images (imagesID, name, role, link, uid, mid) VALUES (?,?,?,?,?,?)'''
            params = (imagesID, name, role, link, uid, mid)  # tuple containing parameter values
            cursor.execute(sql1, params)
            conn.commit()
            print('image uploaded successfully!')
        else:
            print('please make sure that the user patient under the specific mentor.')
    else:
        print('please check user id and mentor id.')

def signPatient(uid, mid):
    if not uidCheck(uid) and not midCheck(mid) and not patientsCheck(uid, mid):
        sql1 = '''INSERT INTO BlinkyDB.dbo.Patients (uid, mid) VALUES (?,?)'''
        params = (uid, mid)  # tuple containing parameter values
        cursor.execute(sql1, params)
        conn.commit()
        sql2 = '''UPDATE BlinkyDB.dbo.[User] SET mid=?'''
        cursor.execute(sql2, mid)
        conn.commit()
        print('patient added successfully!')
    else:
        print('please check user id and mentor id.')

def titleCheck(titleID, uid):
    sql = '''SELECT titleID FROM BlinkyDB.dbo.[Titles] WHERE titleID=? AND uid=?'''
    cursor.execute(sql, (titleID, uid))
    for row in cursor:
        if row.titleID == titleID:
            return True
    return False

def uploadTitle(titleID, action, uid, mid, role):
    if not uidCheck(uid) and not midCheck(mid):
        if patientsCheck(uid, mid) and not titleCheck(titleID, uid):
            sql1 = '''INSERT INTO BlinkyDB.dbo.Titles (titleID, phrase, uid, mid, role) VALUES (?,?,?,?,?)'''
            params = (titleID, action, uid, mid, role)  # tuple containing parameter values
            cursor.execute(sql1, params)
            conn.commit()
            print('title uploaded successfully!')
        elif patientsCheck(uid, mid)== False:
            print('please make sure that the user patient under the specific mentor.')
        elif titleCheck(titleID, uid) == True:
            print('this title is already in use please ')
    else:
        print('please check user id and mentor id.')

def defaultTitleCheck(titleID):
    sql = '''SELECT titleID FROM BlinkyDB.dbo.[Titles] WHERE titleID=?'''
    cursor.execute(sql, titleID)
    for row in cursor:
        if row.titleID == titleID:
            return True
    return False

def uploadDefaultTitle(titleID, phrase):
    if not defaultTitleCheck(titleID):
        sql1 = '''INSERT INTO BlinkyDB.dbo.Titles (titleID, phrase) VALUES (?,?)'''
        params = (titleID, phrase)  # tuple containing parameter values
        cursor.execute(sql1, params)
        conn.commit()
        print('title uploaded successfully!')
    else:
        print('this title is already in use please ')

def uploadDefaultImage(imagesID, name, link):
    if not imageCheck(imagesID):
        sql1 = '''INSERT INTO BlinkyDB.dbo.Images (imagesID, name, link) VALUES (?,?,?)'''
        params = (imagesID, name, link)  # tuple containing parameter values
        cursor.execute(sql1, params)
        conn.commit()
        print('image uploaded successfully!')
    else:
        print('please make sure that the user patient under the specific mentor.')
        
def UpdateChosenPic(UserID,ChangeList,top):

    path = "pics/" + ChangeList["NewPicsBox"].get() + ".gif"
    ChangeList["path"] = path
    params = (ChangeList["picIDcomboBox"].get(),ChangeList["NewPicsBox"].get(), path, UserID, ChangeList["picIDcomboBox"].get())
    sql = '''UPDATE BlinkyDB.dbo.Images set role=?,name=?,link=? WHERE uid=? AND role=?'''
    rows = cursor.execute(sql, params)
    conn.commit()
    if rows.rowcount == 0:
        mid = -1
        imagesID = -1
        sql = '''SELECT * FROM BlinkyDB.dbo.[User] WHERE uid=?'''
        cursor.execute(sql, UserID)
        for row in cursor:
            if row.uid ==UserID:
                mid =row.mid


        sql1 = '''SELECT * FROM BlinkyDB.dbo.Images WHERE uid is NULL AND name=?'''
        cursor.execute(sql1, ChangeList["NewPicsBox"].get())
        for row in cursor:
            if row.name == ChangeList["NewPicsBox"].get():
                imagesID =row.imagesID
        sql2= '''INSERT INTO BlinkyDB.dbo.Images (imagesID, name, role, link, uid, mid) VALUES (?,?,?,?,?,?)'''
        params = (imagesID, ChangeList["NewPicsBox"].get(), ChangeList["picIDcomboBox"].get(), path, UserID, mid)  # tuple containing parameter values
        cursor.execute(sql2, params)
        conn.commit()

    GUIandDBCommunication.GUIandDB.RefreshUserPic(ChangeList, top)

def UpdateChosenPhrase(UserID,ChangeList,top):

    role = ChangeList["PhraseIDCombobox"].get()
    phrase = ChangeList["NewPhrasesBox"].get()

    params = (phrase,UserID,role)
    sql = '''UPDATE BlinkyDB.dbo.Titles set phrase=? WHERE uid=? AND role=?'''
    rows = cursor.execute(sql, params)
    conn.commit()
    if rows.rowcount == 0:
        mid = -1
        titleID = -1
        sql = '''SELECT * FROM BlinkyDB.dbo.[User] WHERE uid=?'''
        cursor.execute(sql, UserID)
        for row in cursor:
            if row.uid == UserID:
                mid = row.mid
        sql1 = '''SELECT * FROM BlinkyDB.dbo.Titles WHERE uid is NULL and role=?'''
        cursor.execute(sql1,role)
        for row in cursor:
            if row.role == role:
                titleID =row.titleID
        sql2= '''INSERT INTO BlinkyDB.dbo.Titles (titleID, phrase, uid, mid,role) VALUES (?,?,?,?,?)'''
        params = (titleID,phrase,UserID,mid,role)  # tuple containing parameter values
        cursor.execute(sql2, params)
        conn.commit()

    GUIandDBCommunication.GUIandDB.RefreshUserPhrase(ChangeList, top)
 
def takePhrase(uid,role):
    params = (uid,role)
    sql = '''SELECT * FROM BlinkyDB.dbo.Titles WHERE uid=? AND role=?'''
    cursor.execute(sql, params)
    for row in cursor:
        if row.uid == uid and row.role == role:
            return row.phrase
    sql = '''SELECT * FROM BlinkyDB.dbo.Titles WHERE TitleID=? AND role=?'''
    cursor.execute(sql,(role, role))
    for row in cursor:
        if row.role == role:
            return row.phrase

def loadAllPhrases(UserID):
    AllPhrases = []
    sql = '''SELECT * FROM BlinkyDB.dbo.Titles WHERE uid=?'''
    cursor.execute(sql, UserID)
    for row in cursor:
        if row.uid == UserID:
            AllPhrases.append(row.phrase)

    sql = '''SELECT * FROM BlinkyDB.dbo.Titles WHERE uid is NULL'''
    cursor.execute(sql)
    for row in cursor:
        AllPhrases.append(row.phrase)
    return AllPhrases

def loadAllPic(UserID):
    AllPicList = []
    sql = '''SELECT * FROM BlinkyDB.dbo.Images WHERE uid=?'''
    cursor.execute(sql, UserID)
    for row in cursor:
        if row.uid == UserID:
            string = str(row.link)
            string1 = string.replace("pics/", "")
            string2 = string1.replace('.gif', '')
            AllPicList.append(string2)
            
    sql = '''SELECT link FROM BlinkyDB.dbo.Images WHERE uid is NULL'''
    cursor.execute(sql)
    for row in cursor:
        string = str(row.link)
        string1 = string.replace("pics/","")
        string2 = string1.replace('.gif','')
        AllPicList.append(string2)
    return AllPicList
               
def takePic(uid,role):
    params = (uid,role)
    sql = '''SELECT * FROM BlinkyDB.dbo.Images WHERE uid=? AND role=?'''
    cursor.execute(sql, params)
    for row in cursor:
        if row.uid == uid and row.role == role:
            return row.link
    sql = '''SELECT * FROM BlinkyDB.dbo.Images WHERE ImagesID=? AND role=?'''
    cursor.execute(sql,(role,role))
    for row in cursor:
        if row.role == role:
            return row.link
          
def allMentors():
    global cursor
    MentorList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.Mentor'''
    cursor.execute(sql)
    for row in cursor:
        MentorList.append(row.mid)
    return MentorList

def allUsers():
    global cursor
    UserList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.[User]'''
    cursor.execute(sql)
    for row in cursor:
        UserList.append(row.uid)
    return UserList

def allAdmins():
    global cursor
    adminList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.Admins'''
    cursor.execute(sql)
    for row in cursor:
        adminList.append(row.id)
    return adminList
    
def deleteMentor(mid):
    sql = '''DELETE FROM BlinkyDB.dbo.Mentor WHERE mid=?'''
    cursor.execute(sql, (mid["MentorIDBox"].get()))
    conn.commit()
    mid["MentorIDBox"]['values'] = allMentors()
    File_path = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
    f = open(File_path, "a")
    now = datetime.datetime.now()
    line = "mid: " + str(mid["MentorIDBox"].get()) + " is deleted at: " + now.day.__str__() + "/" + now.month.__str__()
    line += "/" + now.year.__str__() + " at: " + now.time().__str__()
    f.write(line + "%d\r\n" % (1))
    f.close()
    tkMessageBox.showinfo("", "Mentor is deleted!")

def AdminAddImage(tempdir,AdminList):
    picDir = tempdir["tempdir"].split('/')
    picName = picDir[-1]
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0] + "\pics"+"\\"+picName
    copyfile(tempdir["tempdir"], prog_location)
    maxImg = -1
    sql = '''SELECT MAX(imagesID) as imagesID FROM BlinkyDB.dbo.Images'''
    cursor.execute(sql)
    for row in cursor:
        maxImg = row.imagesID
    sql1= '''INSERT INTO BlinkyDB.dbo.Images (imagesID, name, role, link) VALUES (?,?,?,?)'''
    
    params = (maxImg+1,(picName.split('.'))[0],0,"pics/"+picName)
    cursor.execute(sql1, params)
    conn.commit()
    AdminList["RemoveImage"]['values'] = allImages()
    tkMessageBox.showinfo("", "Image Added!")
    
def allImages(uid=None,MentorList=None):
    if uid is None:
        ImagesList = []
        sql = '''SELECT DISTINCT name FROM BlinkyDB.dbo.Images'''
        cursor.execute(sql)
        for row in cursor:
            ImagesList.append(row.name)
        return ImagesList
    if uid == "":
        return ""
    else:
        ImagesList = []
        sql = '''SELECT DISTINCT name FROM BlinkyDB.dbo.Images WHERE uid=?'''
        cursor.execute(sql,uid)
        for row in cursor:
            ImagesList.append(row.name)
        if MentorList is not None:
            MentorList["ImageComboBox"]['values'] = ImagesList
        return ImagesList

def deleteImage(imgList):
    sql = '''DELETE FROM BlinkyDB.dbo.Images WHERE name=?'''
    cursor.execute(sql, (imgList["RemoveImage"].get()))
    conn.commit()
    name = imgList["RemoveImage"].get()
    imgList["RemoveImage"].delete(0, 'end')
    imgList["RemoveImage"]['values'] = allImages()
    File_path = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
    f = open(File_path, "a")
    now = datetime.datetime.now()
    line = "image name: " + str(name) + " is deleted at: " + now.day.__str__() + "/" + now.month.__str__()
    line += "/" + now.year.__str__() + " at: " + now.time().__str__()
    f.write(line + "%d\r\n" % (1))
    f.close()
    tkMessageBox.showinfo("", "image is deleted!")
    
def AdminAddPhrase(AdminList):
    maxPhraseID = -1
    sql = '''SELECT MAX(titleID) as titleID FROM BlinkyDB.dbo.Titles'''
    cursor.execute(sql)
    for row in cursor:
        maxPhraseID = row.titleID
    sql1= '''INSERT INTO BlinkyDB.dbo.Titles (titleID, phrase, role) VALUES (?,?,?)'''
    params = (maxPhraseID+1,AdminList["PhraseEntry"].get(),0)
    cursor.execute(sql1,params)
    conn.commit()
    AdminList["RemovePhrase"]['values'] = allPhrases()
    tkMessageBox.showinfo("", "Phrase is added!")
    
def allPhrases(uid=None, MentorList=None):
    if uid is None:
        PhraseList = []
        sql = '''SELECT DISTINCT phrase FROM BlinkyDB.dbo.Titles'''
        cursor.execute(sql)
        for row in cursor:
            PhraseList.append(row.phrase)
        return PhraseList

    if uid == "":
        return ""
    else:
        PhraseList = []
        sql = '''SELECT DISTINCT phrase FROM BlinkyDB.dbo.Titles WHERE uid=?'''
        cursor.execute(sql, uid)
        for row in cursor:
            PhraseList.append(row.phrase)
        if MentorList is not None:
            MentorList["titleCombobox"]['values'] = PhraseList
        return PhraseList

def AdminRemovePhrase(AdminList):
    sql = '''DELETE FROM BlinkyDB.dbo.Titles WHERE phrase=?'''
    cursor.execute(sql, (AdminList["RemovePhrase"].get()))
    conn.commit()
    name = AdminList["RemovePhrase"].get()
    AdminList["RemovePhrase"].delete(0,'end')
    AdminList["RemovePhrase"]['values'] = allPhrases()
    File_path = prog_location + "\Reports" + "\\" + "statisticsReport.txt"
    f = open(File_path, "a")
    now = datetime.datetime.now()
    line = "title: " + str(name) + " is deleted at: " + now.day.__str__() + "/" + now.month.__str__()
    line += "/" + now.year.__str__() + " at: " + now.time().__str__()
    f.write(line)
    f.close()
    tkMessageBox.showinfo("", "Phrase is deleted!")

def loadAllUsers(ID):
    global cursor
    UserList = []
    sql = '''SELECT * FROM BlinkyDB.dbo.[User] WHERE mid=?'''
    cursor.execute(sql,ID)
    for row in cursor:
        if row.mid == ID:
            UserList.append(row.uid)

    return UserList

def MentorRemoveImagetoUser(MentorID,MentorList):

    sql = '''DELETE FROM BlinkyDB.dbo.Images WHERE uid=? AND mid=? AND name=?'''
    params = (MentorList["UserComboBox"].get(), MentorID, MentorList["ImageComboBox"].get())
    cursor.execute(sql,params)
    conn.commit()
    MentorList["UserComboBox"].delete(0, 'end')
    MentorList["ImageComboBox"].delete(0,'end')
    MentorList["ImageComboBox"]['values'] = allImages(MentorID,MentorList)
    tkMessageBox.showinfo("","the image has been removed.")

def MentorRemovePhrasetoUser(MentorID,MentorList):

    sql = '''DELETE FROM BlinkyDB.dbo.Titles WHERE uid=? AND mid=? AND phrase=?'''
    params = (MentorList["UserComboBox"].get(), MentorID, MentorList["titleCombobox"].get())
    cursor.execute(sql,params)
    conn.commit()
    MentorList["UserComboBox"].delete(0, 'end')
    MentorList["titleCombobox"].delete(0, 'end')
    MentorList["titleCombobox"]['values'] = allPhrases(MentorID,MentorList)
    tkMessageBox.showinfo("", "the phrase has been removed.")

def MentorAddPhrasetoUser(MentorID,MentorList):
    sql = '''UPDATE BlinkyDB.dbo.Titles set role=? WHERE uid=? AND role=? AND mid=?'''
    params = (0,MentorList["UserComboBox"].get(),MentorList["rolecombobox"].get(),MentorID)
    cursor.execute(sql, params)
    conn.commit()
    tkMessageBox.showinfo("", "the phrase had been added.")

    maxPhraseID = -1
    sql1 = '''SELECT MAX(titleID) as titleID FROM BlinkyDB.dbo.Titles'''
    cursor.execute(sql1)
    for row in cursor:
        maxPhraseID = row.titleID

    sql2 = '''INSERT INTO BlinkyDB.dbo.Titles (titleID, phrase, uid, mid, role) VALUES (?,?,?,?,?)'''
    params = (maxPhraseID+1,MentorList["newPhraseEntry"].get(),MentorList["UserComboBox"].get(), MentorID,MentorList["rolecombobox"].get())  # tuple containing parameter values
    cursor.execute(sql2, params)
    conn.commit()

def MentorAddImagetoUser(MentorID, tempdir ,MentorList):
    picDir = tempdir["tempdir"].split('/')
    picName = picDir[-1]
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0] + "\pics" + "\\" + picName
    copyfile(tempdir["tempdir"], prog_location)
    finalpicName = (picName.split('.'))[0]

    sql = '''UPDATE BlinkyDB.dbo.Images set role=? WHERE uid=? AND role=? AND mid=?'''
    params = ("0", MentorList["UserComboBox"].get(), MentorList["rolecombobox"].get(), MentorID)
    cursor.execute(sql, params)
    conn.commit()

    ###

    sql1 = '''UPDATE BlinkyDB.dbo.Images set role=? WHERE uid=? AND mid=? AND name=?'''
    params = (MentorList["rolecombobox"].get(), MentorList["UserComboBox"].get(), MentorID, finalpicName)
    rows = cursor.execute(sql1, params)
    conn.commit()

    if rows.rowcount == 0:
        maxImg = -1
        sql = '''SELECT MAX(imagesID) as imagesID FROM BlinkyDB.dbo.Images'''
        cursor.execute(sql)
        for row in cursor:
            maxImg = row.imagesID

        sql1 = '''INSERT INTO BlinkyDB.dbo.Images (imagesID, name, role, link, uid, mid) VALUES (?,?,?,?,?,?)'''

        params = (maxImg + 1,finalpicName, MentorList["rolecombobox"].get(), "pics/" + picName,
                  MentorList["UserComboBox"].get(),MentorID)
        cursor.execute(sql1, params)
        conn.commit()
        MentorList["ImageComboBox"]['values'] = allImages(MentorID, MentorList)
    tkMessageBox.showinfo("", "the image has been added.")

def MentorRemoveUser(MentorID,MentorList):
    sql = '''UPDATE BlinkyDB.dbo.Titles set mid=? WHERE uid=? AND mid=?'''
    params = ("-1",MentorList["UserComboBox"].get(),MentorID)
    cursor.execute(sql, params)
    conn.commit()

    sql = '''UPDATE BlinkyDB.dbo.Images set mid=? WHERE uid=? AND mid=?'''
    params = ("-1",MentorList["UserComboBox"].get(),MentorID)
    cursor.execute(sql, params)
    conn.commit()

    sql = '''UPDATE BlinkyDB.dbo.[User] set mid=? WHERE uid=? AND mid=?'''
    params = ("-1",MentorList["UserComboBox"].get(),MentorID)
    cursor.execute(sql, params)
    conn.commit()

    sql = '''UPDATE BlinkyDB.dbo.Patients set mid=? WHERE uid=? AND mid=?'''
    params = ("-1",MentorList["UserComboBox"].get(),MentorID)
    cursor.execute(sql, params)
    conn.commit()

    MentorList["UserComboBox"]['values'] = loadAllUsers(MentorID)
    tkMessageBox.showinfo("", "the user has been removed.")

def MentorAddUser(MentorID,MentorList):
    sql = '''SELECT * FROM BlinkyDB.dbo.[User] WHERE uid=?'''
    rows = cursor.execute(sql, MentorList["NewUserID"].get())

    if rows.rowcount != 0:
        sql = '''UPDATE BlinkyDB.dbo.Titles set mid=? WHERE uid=?'''
        params = (MentorID,MentorList["NewUserID"].get())
        cursor.execute(sql, params)
        conn.commit()

        sql = '''UPDATE BlinkyDB.dbo.Images set mid=? WHERE uid=?'''
        params = (MentorID,MentorList["NewUserID"].get())
        cursor.execute(sql, params)
        conn.commit()

        sql = '''UPDATE BlinkyDB.dbo.[User] set mid=? WHERE uid=?'''
        params = (MentorID,MentorList["NewUserID"].get())
        cursor.execute(sql, params)
        conn.commit()

        sql = '''UPDATE BlinkyDB.dbo.Patients set mid=? WHERE uid=?'''
        params = (MentorID,MentorList["NewUserID"].get())
        cursor.execute(sql, params)
        conn.commit()

        MentorList["UserComboBox"]['values'] = loadAllUsers(MentorID)
        tkMessageBox.showinfo("", "the user has been added.")
    else:
        tkMessageBox.showinfo("", "invalid data input.")

def closeSQLconnection():
    global cursor
    global conn
    cursor.close()
    del cursor
    conn.close()

def returnNumOfUsers():
    global cursor
    userList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.[User]'''
    cursor.execute(sql)
    for row in cursor:
        userList.append(row.uid)
    return len(userList)

def returnNumOfMentors():
    global cursor
    mentorList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.[Mentor]'''
    cursor.execute(sql)
    for row in cursor:
        mentorList.append(row.mid)
    return len(mentorList)

def returnNumOfAdmins():
    global cursor
    adminList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.[Admins]'''
    cursor.execute(sql)
    for row in cursor:
        adminList.append(row.id)
    return len(adminList)

def returnNumOfPictures():
    global cursor
    imageList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.[Images]'''
    cursor.execute(sql)
    for row in cursor:
        imageList.append(row.ImagesID)
    return len(imageList)

def returnNumOfPhrases():
    global cursor
    phraseList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.[Titles]'''
    cursor.execute(sql)
    for row in cursor:
        phraseList.append(row.titleID)
    return len(phraseList)

def getAllImages():
    global cursor
    imageList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.[Images]'''
    cursor.execute(sql)
    for row in cursor:
        imageList.append(row.name)
    return imageList


def getAllTitles():
    global cursor
    titleList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.[Titles]'''
    cursor.execute(sql)
    for row in cursor:
        titleList.append(row.phrase)
    return titleList
