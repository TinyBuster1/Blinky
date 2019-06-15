import pyodbc
import os
import random
import sys
from tkinter import messagebox
global mySQLserver
global conn
global cursor
global prog_call
global prog_location

prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
mySQLserver = 'Driver={ODBC Driver 13 for SQL Server};''SERVER=LAPTOP-L7B6A755;''Database=BlinkyDB;''Trusted_Connection=yes;'



loginFlag = 0



def createCursor():
    global cursor
    global conn
    print([x for x in pyodbc.drivers() if x.endswith(' for SQL Server')])
    conn=pyodbc.connect(mySQLserver)
    cursor = conn.cursor()


def all():
    global cursor
    adminList = []
    mentorList = []
    userList = []


    cursor.execute('SELECT DISTINCT * FROM BlinkyDB.dbo.[User] ')

    for data in cursor:
        userList.append(data.uid)



    cursor.execute('SELECT DISTINCT * FROM BlinkyDB.dbo.Mentor ')
    for data in cursor:
        mentorList.append(data.mid)


    cursor.execute('SELECT DISTINCT * FROM BlinkyDB.dbo.Admins ')
    for data in cursor:
        adminList.append(data.id)

   # print(adminList)
    #print(userList)
    #print(mentorList)
    return(adminList,mentorList,userList)
def getPassword():
    global cursor
    adminList = []
    mentorList = []
    userList = []

    cursor.execute('SELECT DISTINCT * FROM BlinkyDB.dbo.[User] ')

    for data in cursor:
        userList.append((data.uid,data.password))

    cursor.execute('SELECT DISTINCT * FROM BlinkyDB.dbo.Mentor ')
    for data in cursor:
        mentorList.append((data.mid,data.password))

    cursor.execute('SELECT DISTINCT * FROM BlinkyDB.dbo.Admins ')
    for data in cursor:
        adminList.append((data.id,data.password))

    # print(adminList)
    # print(userList)
    # print(mentorList)
    return (adminList, mentorList, userList)
def gen_key(id):
    #'''update keys to A,M,U IN EVREY CONACTION'''
     temp=all()
     getPassword()

     adminList=()
     userList=()
     mentorList=()

     adminList=temp[0]
     mentorList=temp[1]
     userList=temp[2]


     lock=0
     for x in adminList:
        if id==x :
            print("this is admin")
            lock=1
     for x in mentorList:
         if id == x:
             print("this is mentor")
             lock = 2
     for x in userList:
         if id == x:
             print("this is user")
             lock = 3

     S = open('Castamere.txt')
     i = 0
     temp2 = []
     for word in S:
         if (word == " "):
             i = i + 1
         else:
             temp2.append(word.split(" "))
         i = i + 1
     x = temp2[0]
     temp2.remove(x)



     if lock == 1:
         rand=random.randint(1,10)
         key = temp2[rand % 12][2]
         sql='''UPDATE  BlinkyDB.dbo.Admins
             SET BlinkyDB.dbo.Admins.spk=?'''

     elif lock == 2:
         rand = random.randint(1, 10)
         key = temp2[rand % 12][1]
         sql = '''UPDATE  BlinkyDB.dbo.Mentor
                  SET BlinkyDB.dbo.Mentor.spk=?'''
     elif lock == 3:
         rand = random.randint(1, 10)
         key = temp2[rand % 12][1]
         sql = '''UPDATE  BlinkyDB.dbo.[User]
                      SET BlinkyDB.dbo.[User].spk=?'''

     params = key
     cursor.execute(sql, params)
     conn.commit()
     print("in gen-key=",key)
     return (id,lock)

def createTable():
    abc= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    temp = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    for x in range(27):
        y=x
        abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        while(y>0):
            myindex=0
            obj=abc[myindex]
            abc.remove(obj)
            abc.append(obj)
            myindex=myindex+1
            y=y-1


        temp1=list(abc)
        temp[x]=temp1
    return temp
def ENC(id,num):
    table = createTable()


    #take-take firstname shis is the text
    if(num==1):
        sql = '''select BlinkyDB.dbo.Admins.name
                           from BlinkyDB.dbo.Admins
                           where Admins.id=?; '''
        params = id
        cursor.execute(sql, params)
        for row in cursor:
            tempName = row.firstName
    elif num==2:
        sql = '''select BlinkyDB.dbo.Mentor.firstName
                     from BlinkyDB.dbo.Mentor
                     where Mentor.mid=?; '''

        params = id
        cursor.execute(sql, params)
        for row in cursor:
            tempName = row.firstName
    elif num==3:
        sql = '''select BlinkyDB.dbo.[User].firstName
               from BlinkyDB.dbo.[User]
               where [User].uid=?; '''
        params = id
        cursor.execute(sql, params)
        for row in cursor:
            tempName = row.firstName

    print(tempName)




    #taake key
    if(num==1):
        sql = '''select BlinkyDB.dbo.Admins.spk
                           from BlinkyDB.dbo.Admins
                           where Admins.id=?; '''
        params = id
        cursor.execute(sql, params)
        for row in cursor:
            temp = row.spk
    elif num==2:
        sql = '''select BlinkyDB.dbo.Mentor.spk
                     from BlinkyDB.dbo.Mentor
                     where Mentor.mid=?; '''

        params = id
        cursor.execute(sql, params)
        for row in cursor:
            temp = row.spk
    elif num==3:
        sql = '''select BlinkyDB.dbo.[User].spk
               from BlinkyDB.dbo.[User]
               where [User].uid=?; '''

        params = id
        cursor.execute(sql, params)
        for row in cursor:
            temp = row.spk


    key1=temp
    text=tempName
    #first name



    mydic = {'A': 26, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
             'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
             'Z': 25}

    textsize = len(text)
    index1 = 0

    keysize = len(key1)
    keyIndex = 0
    Ctext = ""
    while (textsize > 0):
        if keyIndex == keysize:
            keyIndex = 0

        Skey = key1[keyIndex]
        #if(Skey=='A'):
         #   Skey='B'
        char = text[index1]
        if (char == ' '):
            Ctext = Ctext + " "
        if (char=='1' or char=='2'or char=='3' or char=='4' or char=='5' or char=='6' or char=='7' or char=='8' or char=='9'):
            Ctext=Ctext+char


        else:
            index2 = mydic.get(char.upper())  # culum
            index3 = mydic.get(Skey.upper())  # row
            Echar = table[index3][index2]
            # print("KEY-",Skey,"1-",char,"2-",Echar)
            Ctext = Ctext + Echar
            keyIndex = keyIndex + 1

        textsize = textsize - 1
        index1 = index1 + 1

    print("ENC:--text(uid)=", text, "key=", key1, "ctext=",Ctext)




    lock=num
    if lock == 1:
        sql = '''UPDATE  BlinkyDB.dbo.Admins
            SET BlinkyDB.dbo.Admins.firstName=?
            WHERE BlinkyDB.dbo.Admins.id=?;'''


    elif lock == 2:

        sql = '''UPDATE  BlinkyDB.dbo.Mentor
                 SET BlinkyDB.dbo.Mentor.firstName=?
                 WHERE BlinkyDB.dbo.Mentor.mid=?;'''

    elif lock == 3:
        sql = '''UPDATE  BlinkyDB.dbo.[User]
                     SET BlinkyDB.dbo.[User].firstName=?
                     WHERE BlinkyDB.dbo.[User].uid=?;'''


    params = (Ctext,id)
    cursor.execute(sql, params)
    conn.commit()



    return (Ctext,num)
def DEC(Ctext,num,id):
    # DEC
    table = createTable()
    #get key
    if (num == 1):
        sql = '''select BlinkyDB.dbo.Admins.spk
                              from BlinkyDB.dbo.Admins
                              where Admins.id=?; '''
        params = id
        cursor.execute(sql, params)
        for row in cursor:
            temp = row.spk
        print(temp)

        pass
    elif num == 2:
        sql = '''select BlinkyDB.dbo.Mentor.spk
                        from BlinkyDB.dbo.Mentor
                        where Mentor.mid=?; '''

        params = id
        cursor.execute(sql, params)
        for row in cursor:
            temp = row.spk
    elif num == 3:
        sql = '''select BlinkyDB.dbo.[User].spk
                  from BlinkyDB.dbo.[User]
                  where [User].uid=?; '''

        params = id
        cursor.execute(sql, params)
        for row in cursor:
            temp = row.spk


    mydic = {'A': 26, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
             'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
             'Z': 25}

    textsize = len(Ctext)

    # DEC
    key1 = temp
    index1 = 0
    tempString=Ctext[index1]
    size = len(tempString)
    textsize = len(tempString)
    Pliantext = ""
    keysize = len(key1)
    keyIndex = 0


    while (size > 0):
        if keyIndex == keysize:
            keyIndex = 0

        Skey = key1[keyIndex]

        char = tempString[index1]
        if (char == ' '):
            Pliantext = Pliantext + " "
        else:
            bol = 0
            x = 0
            while bol == 0:
                #print(x)
                if (char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9'):
                    Pliantext = Pliantext + char
                    bol=1
                    continue
                rowindex = mydic.get(Skey.upper())
                if (table[rowindex][x] == char):
                    Dtext = table[0][x]
                    Pliantext = Pliantext + Dtext
                    bol = 1
                else:
                    x = x + 1

            keyIndex = keyIndex + 1
        index1 = index1 + 1
        size = size - 1

    print("DEC:--key=",key1,"Ctext=",Ctext[0],"Ptext=",Pliantext)

    lock = num
    if lock == 1:
        sql = '''UPDATE  BlinkyDB.dbo.Admins
              SET BlinkyDB.dbo.Admins.firstName=?
              WHERE BlinkyDB.dbo.Admins.id=?;'''


    elif lock == 2:

        sql = '''UPDATE  BlinkyDB.dbo.Mentor
                   SET BlinkyDB.dbo.Mentor.firstName=?
                   WHERE BlinkyDB.dbo.Mentor.mid=?;'''

    elif lock == 3:
        sql = '''UPDATE  BlinkyDB.dbo.[User]
                       SET BlinkyDB.dbo.[User].firstName=?
                       WHERE BlinkyDB.dbo.[User].uid=?;'''

    params = (Pliantext, id)
    cursor.execute(sql, params)
    conn.commit()





    return Pliantext



def loginUser(userid, password):
    cursor.execute('SELECT * FROM BlinkyDB.dbo.[User] WHERE uid=? AND password=?', (userid, password))
    for data in cursor:
        if data.uid == userid and data.password == password:
            print("login success!")
            tempid=userid
        else:
            print("wrong id or password please try again!")
            messagebox.showinfo("error", "wrong id or password please try again!")



        x=gen_key(tempid)
        print(x[0],x[1])
        t2=ENC(x[0],x[1])
        #print("t2-",t2)
        t3=DEC(t2,x[1],tempid)














createCursor()
loginUser('U420','1234')


#NumMix(120)
#gen_key("M1")
#e1=ENC("I LOVE ICE")
#e2=DEC(e1)


#print(e1)
#print(e2)

