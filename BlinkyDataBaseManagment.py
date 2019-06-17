import pyodbc
import os
from shutil import copyfile
import sys
import GUIandDBCommunication
import tkinter as tk
from tkinter import messagebox
import datetime
import Pmw
import DataBaseEncryption
global mySQLserver
global conn
global cursor
global prog_call
global prog_location

prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
mySQLserver = 'Driver={SQL Server};''Server=DESKTOP-H3SCR5P\SQLEXPRESS;''Database=BlinkyDB;''Trusted_Connection=yes;'

loginFlag = 0

def createCursor():
    global cursor
    global conn


    #print([x for x in pyodbc.drivers() if x.endswith(' for SQL Server')])
    conn=pyodbc.connect(mySQLserver)



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
    id = DataBaseEncryption.getTranslatedMessage('e', id, 3)
    password = DataBaseEncryption.getTranslatedMessage('e', password, 3)
    params = (id,password)
    cursor.execute(sql, params)
    for row in cursor:
        if row.uid == id and row.password == password:
            print('Wellcome' + row.uid)
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
            messagebox.showinfo("error", "wrong id or password please try again!")

def midCheck(mid):
    global conn
    global cursor
    sql = '''SELECT mid FROM BlinkyDB.dbo.Mentor WHERE mid=?'''

    conn = pyodbc.connect(mySQLserver)

    cursor = conn.cursor()
    #row = cursor.fetchone()

    cursor.execute(sql, mid)
    for row in cursor:
        if row.mid == mid:
            return False
    return True

def registerMentor(mid, password, conpassword, firstName, lastName, phone):
    if password != conpassword:
        messagebox.showinfo("error", 'password not match!, please repeat the password again.')
        return 1
    if midCheck(mid):
        sql1 = '''INSERT INTO BlinkyDB.dbo.Mentor (mid, password, firstName, lastName, phone) VALUES (?,?,?,?,?)'''
        params = (mid, password, firstName, lastName, phone)  # tuple containing parameter values
        cursor.execute(sql1, params)
        conn.commit()
        messagebox.showinfo("", 'mentor register successfully!')
        return 0
    else:
        """
        fix this
        """
        #tkMessageBox.showinfo("error", 'mid already used by other mentor, please choose a different one!')

def uidCheck(uid):

    sql = '''SELECT uid FROM BlinkyDB.dbo.[User] WHERE uid=?'''

    global conn
    conn = pyodbc.connect(mySQLserver)
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

        uid = DataBaseEncryption.getTranslatedMessage('e', uid, 3)
        password = DataBaseEncryption.getTranslatedMessage('e', password, 3)
        firstName = DataBaseEncryption.getTranslatedMessage('e', firstName, 3)
        lastName = DataBaseEncryption.getTranslatedMessage('e', lastName, 3)
        mid = DataBaseEncryption.getTranslatedMessage('e', mid, 3)
        age = DataBaseEncryption.getTranslatedMessage('e', age, 3)
        gender = DataBaseEncryption.getTranslatedMessage('e', gender, 3)
        birthday = DataBaseEncryption.getTranslatedMessage('e', birthday, 3)
        phone =DataBaseEncryption.getTranslatedMessage('e', phone, 3)
        address = DataBaseEncryption.getTranslatedMessage('e', address, 3)
        contact1 = DataBaseEncryption.getTranslatedMessage('e', contact1, 3)
        contact2 = DataBaseEncryption.getTranslatedMessage('e', contact2, 3)
        medical = DataBaseEncryption.getTranslatedMessage('e', medical, 3)
        diet = DataBaseEncryption.getTranslatedMessage('e', diet, 3)
        params = (uid, password, firstName, lastName, mid, age, gender, birthday, phone, address, contact1, contact2, medical, diet)  # tuple containing parameter values
        cursor.execute(sql1, params)
        conn.commit()
        sql2 = '''INSERT INTO BlinkyDB.dbo.Patients VALUES (?,?)'''
        params = (uid, mid)  # tuple containing parameter values
        cursor.execute(sql2, params)
        conn.commit()
        messagebox.showinfo("",'user register successfully!')
        return 0
    elif(uidCheck(uid)==False):
        messagebox.showinfo("error",'user id already used by other user, please choose a different one!')
    elif(midCheck(mid)==True):
        messagebox.showinfo("error",'mentor id is not exist!, please provide a valid mentor.')

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
    temp = ChangeList["NewPhraseEntry"].get()
    temp1 = ChangeList["NewPhrasesBox"].get()
    phrase = ""
    if(temp == ""):
        phrase = temp1
    else:
        phrase = temp
    params = (phrase, UserID, role)
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
        cursor.execute(sql1, role)
        for row in cursor:
            if row.role == role:
                titleID =row.titleID
        sql2= '''INSERT INTO BlinkyDB.dbo.Titles (titleID, phrase, uid, mid,role) VALUES (?,?,?,?,?)'''
        params = (titleID, phrase, UserID, mid, role)  # tuple containing parameter values
        cursor.execute(sql2, params)
        conn.commit()

    GUIandDBCommunication.GUIandDB.RefreshUserPhrase(ChangeList, top)
 
def takePhrase(uid,role):
    params = (uid,role)
    sql = '''SELECT * FROM BlinkyDB.dbo.Titles WHERE uid=? AND role=?'''
    cursor.execute(sql, params)
    for row in cursor:
        if row.uid == uid and row.role == role:
            return DataBaseEncryption.getTranslatedMessage('d', row.phrase, 3)
    sql = '''SELECT * FROM BlinkyDB.dbo.Titles WHERE TitleID=? AND role=?'''
    cursor.execute(sql,(role, role))
    for row in cursor:
        if row.role == role:
            return DataBaseEncryption.getTranslatedMessage('d', row.phrase, 3)

def loadAllPhrases(UserID):
    AllPhrases = []
    sql = '''SELECT * FROM BlinkyDB.dbo.Titles WHERE uid=?'''
    cursor.execute(sql, UserID)
    for row in cursor:
        if row.uid == UserID:
            AllPhrases.append(DataBaseEncryption.getTranslatedMessage('d',row.phrase,3))

    sql = '''SELECT * FROM BlinkyDB.dbo.Titles WHERE uid is NULL'''
    cursor.execute(sql)
    for row in cursor:
        AllPhrases.append(DataBaseEncryption.getTranslatedMessage('d', row.phrase, 3))
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
    messagebox.showinfo("", "Mentor is deleted!")

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
    messagebox.showinfo("", "Image Added!")
    
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
    messagebox.showinfo("", "image is deleted!")
    
def AdminAddPhrase(AdminList):
    maxPhraseID = -1
    sql = '''SELECT MAX(titleID) as titleID FROM BlinkyDB.dbo.Titles'''
    cursor.execute(sql)
    for row in cursor:
        maxPhraseID = row.titleID
    sql1 = '''INSERT INTO BlinkyDB.dbo.Titles (titleID, phrase, role) VALUES (?,?,?)'''
    titleID = getTranslatedMessage('e', AdminList["PhraseEntry"].get(), 3)
    # titleID = encryptDate(key, AdminList["PhraseEntry"].get())
    #    print(titleID)
    params = (maxPhraseID + 1, titleID, 0)
    cursor.execute(sql1, params)
    conn.commit()
    AdminList["RemovePhrase"]['values'] = allPhrases()
    messagebox.showinfo("", "Phrase is added!")



def allPhrases(uid=None, MentorList=None):
    if uid is None:
        PhraseList = []
        sql = '''SELECT DISTINCT phrase FROM BlinkyDB.dbo.Titles'''
        cursor.execute(sql)
        for row in cursor:

            PhraseList.append(DataBaseEncryption.getTranslatedMessage('d',row.phrase, 3 ))
        return PhraseList
    if uid == "":
        return ""
    else:
        PhraseList = []
        sql = '''SELECT DISTINCT phrase FROM BlinkyDB.dbo.Titles WHERE uid=?'''
        cursor.execute(sql, uid)
        for row in cursor:
            PhraseList.append(DataBaseEncryption.getTranslatedMessage('d', row.phrase, 3))
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
    messagebox.showinfo("", "Phrase is deleted!")

def loadAllUsers(ID):
    global cursor
    UserList = []
    sql = '''SELECT * FROM BlinkyDB.dbo.[User] WHERE mid=?'''
    cursor.execute(sql,ID)
    for row in cursor:
        if row.mid == ID:
            UserList.append(DataBaseEncryption.getTranslatedMessage('d',row.uid,3))

    return UserList

def MentorRemoveImagetoUser(MentorID,MentorList):

    sql = '''DELETE FROM BlinkyDB.dbo.Images WHERE uid=? AND mid=? AND name=?'''
    params = (MentorList["UserComboBox"].get(), MentorID, MentorList["ImageComboBox"].get())
    cursor.execute(sql,params)
    conn.commit()
    MentorList["UserComboBox"].delete(0, 'end')
    MentorList["ImageComboBox"].delete(0,'end')
    MentorList["ImageComboBox"]['values'] = allImages(MentorID,MentorList)
    messagebox.showinfo("","the image has been removed.")

def MentorRemovePhrasetoUser(MentorID,MentorList):

    sql = '''DELETE FROM BlinkyDB.dbo.Titles WHERE uid=? AND mid=? AND phrase=?'''
    params = (MentorList["UserComboBox"].get(), MentorID, MentorList["titleCombobox"].get())
    cursor.execute(sql,params)
    conn.commit()
    MentorList["UserComboBox"].delete(0, 'end')
    MentorList["titleCombobox"].delete(0, 'end')
    MentorList["titleCombobox"]['values'] = allPhrases(MentorID,MentorList)
    messagebox.showinfo("", "the phrase has been removed.")

def MentorAddPhrasetoUser(MentorID,MentorList):
    sql = '''UPDATE BlinkyDB.dbo.Titles set role=? WHERE uid=? AND role=? AND mid=?'''
    params = (0,MentorList["UserComboBox"].get(),MentorList["rolecombobox"].get(),MentorID)
    cursor.execute(sql, params)
    conn.commit()
    messagebox.showinfo("", "the phrase had been added.")

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
    messagebox.showinfo("", "the image has been added.")

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
    messagebox.showinfo("", "the user has been removed.")

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
        messagebox.showinfo("", "the user has been added.")
    else:
        messagebox.showinfo("", "invalid data input.")

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
        imageList.append(row.imagesID)
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
        imageList.append(DataBaseEncryption.getTranslatedMessage('d', row.name, 3))
    return imageList


def getAllTitles():
    global cursor
    titleList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.[Titles]'''
    cursor.execute(sql)
    for row in cursor:
        titleList.append(DataBaseEncryption.getTranslatedMessage('d',row.phrase,3))
    return titleList

def user_info(Mid):
    if (Mid == None):
        return False
    if (type(Mid) != str):
        return False
    global conn
    global cursor
    global prog_location
    conn = pyodbc.connect(mySQLserver)
    cursor = conn.cursor()
    sql = '''SELECT DISTINCT COUNT(*) FROM BlinkyDB.dbo.Mentor,BlinkyDB.dbo.[User]
                               where BlinkyDB.dbo.Mentor.mid=BlinkyDB.dbo.[User].mid;'''
    cursor.execute(sql)
    row = cursor.fetchone()
    fpath = os.path.join(prog_location+'/Reports', 'userinfo.txt')
    file = open(fpath, 'w')
    file.write('Hello Mentor ' + Mid)
    file.write('\n')
    file.write('        You have ' + str(row[0]) + ' users under your name\n')

    sql = '''SELECT DISTINCT [User].mid,[User].uid,[User].firstName,[User].lastName,[User].age, [User].gender,[User].birthday,[User].phone,[User].address,[User].contact1,[User].contact2,[User].diet
           FROM BlinkyDB.dbo.Mentor,BlinkyDB.dbo.[User]
           where BlinkyDB.dbo.[User].mid=?;'''


    cursor.execute(sql, Mid)
    if(cursor==None):
        return False

    file.write('\n')
    t = 0
    for row in cursor:
        assert isinstance(Mid, str)
        if (row == None):
            return False
        file.write(' user number #' + str(t))
        file.write('\n')
        t = t + 1
        file.write('        uid: ' + row.uid)
        file.write('\n')
        file.write('        first name: ' + row.firstName)
        file.write('\n')
        file.write('        last name: ' + row.lastName)
        file.write('\n')
        file.write('        age: ' + str(row.age))
        file.write('\n')
        file.write('        gender: ' + row.gender)
        file.write('\n')
        file.write('        birthday: ' + row.birthday)
        file.write('\n')
        file.write('        phone: ' + str(row.phone))
        file.write('\n')
        file.write('        address: ' + row.address)
        file.write('\n')
        file.write('        contact1: ' + str(row.contact1))
        file.write('\n')
        file.write('        contact2: ' + str(row.contact2))
        file.write('\n')
    file.close()
    conn.close()

    root = tk.Tk()
    st = Pmw.ScrolledText(root, borderframe=1, labelpos=tk.N,
                          label_text='Blackmail', usehullsize=1,
                          hull_width=400, hull_height=300,
                          text_padx=10, text_pady=10,
                          text_wrap='none')
    st.importfile(fpath)
    st.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

    root.mainloop()
    return True

def medical_info(mid):
    global conn
    global prog_location
    if (mid == None):
        return False
    if (type(mid) != str):
        return False
    conn = pyodbc.connect(mySQLserver)
    global cursor
    cursor = conn.cursor()
    sql = '''SELECT Mentor.mid,[User].uid,medical
            FROM BlinkyDB.dbo.Mentor,BlinkyDB.dbo.[User]
            where BlinkyDB.dbo.Mentor.mid=BlinkyDB.dbo.[User].mid AND Mentor.mid=?;'''

    cursor.execute(sql, mid)
    row = cursor.fetchone()
    if(row==None):
        return False
    fpath = os.path.join(prog_location+'\Reports', 'medical_info_Report.txt')

    file = open(fpath, 'w')
    file.write('medical info Report:')
    file.write('\n')
    file.write('Hello Mentor ' + mid)
    file.write('\n')
    file.write('        user name:' + str(row.uid))
    file.write('\n')
    file.write('            medical info:')
    file.write('\n')
    file.write('                    ' + str(row.medical))
    file.write('\n')
    file.close()

    conn.close()

    root = tk.Tk()
    st = Pmw.ScrolledText(root, borderframe=1, labelpos=tk.N,
                          label_text='Blackmail', usehullsize=1,
                          hull_width=400, hull_height=300,
                          text_padx=10, text_pady=10,
                          text_wrap='none')
    st.importfile(fpath)
    st.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

    root.mainloop()
    return True

def updateMedical(userid,changeList):
    updateString = changeList['MedicalOrDiet'].get()
    sql = '''UPDATE BlinkyDB.dbo.[user] set medical=? WHERE uid=?'''
    params = (updateString,userid)
    cursor.execute(sql, params)
    conn.commit()

def updateDiet(userid,changeList):
    updateString = changeList['MedicalOrDiet'].get()
    sql = '''UPDATE BlinkyDB.dbo.[user] set diet=? WHERE uid=?'''
    params = (updateString,userid)
    cursor.execute(sql, params)
    conn.commit()

def getMail(ID):
    global cursor
    titleList = []
    sql = '''SELECT DISTINCT * FROM BlinkyDB.dbo.[Admins] WHERE id=?'''
    params = ID
    cursor.execute(sql, params)
    for row in cursor:
        titleList.append(row.email)
    return titleList
