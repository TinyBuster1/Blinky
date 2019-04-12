import GUI
import NewUserRegister
import RegisterNewMentor
import LogicGui
import BlinkyDataBaseManagment
import sys
import os.path
import tkMessageBox
#comment loginAuth if needed  DONT DELETE IT!
import LoginAuth

import Tkinter as tk
import tkSimpleDialog
import datetime

global login_dict
global count
global prog_call
global prog_location

prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
count = 0
login_dict = {}

class GUIandDB:
    @staticmethod
    def checkUserInput(self,UserList,top):


        value = BlinkyDataBaseManagment.registerUser(UserList["UserID"].get(),UserList["UserPassword1"].get(),
                                             UserList["PatientName"].get(),UserList["UserLastName"].get(),
                                             UserList["MentorID"].get(),UserList["UserAge"].get(),
                                             UserList["UserGender"].get(),UserList["PatientDOB"].get(),
                                             UserList["UserPhone"].get(),UserList["UserAddress"].get(),
                                             UserList["UserContact1"].get(),UserList["UserContact2"].get(),
                                             UserList["UserMedical"].get(),UserList["UserDiet"].get())

        if value == 0:
            LogicGui.LogicGui.returnToMainFromUser(self, top)
        
    @staticmethod
    def checkMentorInput(self,MentorList,top,flag):
        value = BlinkyDataBaseManagment.registerMentor(MentorList["MentorID"].get(), MentorList["MentorPassword1"].get(),
                                               MentorList["MentorPassword2"].get(),MentorList["MentorName"].get(),
                                               MentorList["MentorLastName"].get(),MentorList["MentorPhone"].get())

        if value == 0:
            LogicGui.LogicGui.returnToMainFromMentor(self, top,flag)
        
    @staticmethod
    def Logged(self, LoginList, top):
        global count
        BlinkyDataBaseManagment.createCursor()
        userType = BlinkyDataBaseManagment.userChecker(LoginList["UserNameText"].get(), LoginList["PasswordText"].get())
        
        if userType == 1:
            # here do the transfer to admin page
            #GUIandDB.adminMailVerifier(self,LoginList,top)
            LogicGui.LogicGui.OpenAdminPanelWin(self, top)
            print("Admin login success!")
        elif userType == 2:
            # here do the transfer to mentor page
            #GUIandDB.mentorMailVerifier(self, LoginList, top, email)
            LogicGui.LogicGui.OpenMentorPanelWin(self,LoginList["UserNameText"].get(), top)
            print("Mentor login success!")
        elif userType == 3:
            
            PicAndPharases = {}
            PicAndPharases["pic1button"] = BlinkyDataBaseManagment.takePic(LoginList["UserNameText"].get(), "1")
            PicAndPharases["pic2button"] = BlinkyDataBaseManagment.takePic(LoginList["UserNameText"].get(), "2")
            PicAndPharases["pic3button"] = BlinkyDataBaseManagment.takePic(LoginList["UserNameText"].get(), "3")
            PicAndPharases["pic4button"] = BlinkyDataBaseManagment.takePic(LoginList["UserNameText"].get(), "4")

            PicAndPharases["Phrase1Button"] = BlinkyDataBaseManagment.takePhrase(LoginList["UserNameText"].get(), "1")
            PicAndPharases["Phrase2Button"] = BlinkyDataBaseManagment.takePhrase(LoginList["UserNameText"].get(), "2")
            PicAndPharases["Phrase3Button"] = BlinkyDataBaseManagment.takePhrase(LoginList["UserNameText"].get(), "3")
            PicAndPharases["Phrase4Button"] = BlinkyDataBaseManagment.takePhrase(LoginList["UserNameText"].get(), "4")
            #GUIandDB.userMailVerifier(self, LoginList,top,PicAndPharases,"alexabo4@ac.sce.ac.il")
            LogicGui.LogicGui.OpenUserPanelWin(self, LoginList["UserNameText"].get(), PicAndPharases, top)

        else:
            tkMessageBox.showinfo("error", "wrong id or password please try again!")
            if LoginList["UserNameText"].get() not in login_dict:
                count = 0
                login_dict[LoginList["UserNameText"].get()] = count
            elif login_dict[LoginList["UserNameText"].get()] == 1:
                File_path = prog_location + "\Reports" + "\\" + "wrongPasswordReport.txt"
                f = open(File_path, "a")
                now = datetime.datetime.now()
                line = " uid: " + str(LoginList["UserNameText"].get()) + " " + now.day.__str__() + "/" + now.month.__str__()
                line += "/" + now.year.__str__() + " at: " + now.time().__str__()
                f.write(line+"%d\r\n" % (1))
                f.close()
            else:
                login_dict[LoginList["UserNameText"].get()] += 1

    @staticmethod
    def mentorMailVerifier(self, LoginList,top,email):
        a = LoginAuth.sendEmail(email)  # enter real email from user
        answer = tkSimpleDialog.askinteger("Login Authentication", "Please enter your PIN:") or -1
        entrycount = 0
        while a != answer and answer != -1:
            print(a)  # real PIN code
            entrycount += 1
            entry = str(entrycount)
            tkMessageBox.showinfo("error", "Wrong pin code! attempt number :" + entry)
            answer = tkSimpleDialog.askinteger("Login Authentication", "Please enter your PIN:") or -1
        if answer == -1:
            print("")
        else:
            LogicGui.LogicGui.OpenMentorPanelWin(self,LoginList["UserNameText"].get(), top)

    @staticmethod
    def adminMailVerifier(self, LoginList,top,email):
        a = LoginAuth.sendEmail(email)  # enter real email from user
        answer = tkSimpleDialog.askinteger("Login Authentication", "Please enter your PIN:") or -1
        entrycount = 0
        while a != answer and answer != -1:
            print(a)  # real PIN code
            entrycount += 1
            entry = str(entrycount)
            tkMessageBox.showinfo("error", "Wrong pin code! attempt number :" + entry)
            answer = tkSimpleDialog.askinteger("Login Authentication", "Please enter your PIN:") or -1
        if answer == -1:
            print("")
        else:
            LogicGui.LogicGui.OpenAdminPanelWin(self, top)

    @staticmethod
    def userMailVerifier(self, LoginList,top,PicAndPharases,email):
        a = LoginAuth.sendEmail(email)  # enter real email from user
        answer = tkSimpleDialog.askinteger("Login Authentication", "Please enter your PIN:") or -1
        entrycount = 0
        while a != answer and answer != -1:
            print(a)  # real PIN code
            entrycount += 1
            entry = str(entrycount)
            tkMessageBox.showinfo("error", "Wrong pin code! attempt number :" + entry)
            answer = tkSimpleDialog.askinteger("Login Authentication", "Please enter your PIN:") or -1
        if answer == -1:
            print("")
        else:
            LogicGui.LogicGui.OpenUserPanelWin(self, LoginList["UserNameText"].get(), PicAndPharases, top)

    @staticmethod
    def RefreshUserPic(ChangeList, top):
        role = ChangeList["picIDcomboBox"].get()

        button = ChangeList["pic"+role+"button"]

        prog_call = sys.argv[0]
        prog_location = os.path.split(prog_call)[0]
        photo_location = os.path.join(prog_location, ChangeList["path"])
        image = tk.PhotoImage(file=photo_location)

        button.configure(image=image)
        button.configure(pady="0")
        button.update()

        ChangeList["LoginFrame"].update()

        top.mainloop()
    
    @staticmethod
    def RefreshUserPhrase(ChangeList,top):
        role = ChangeList["PhraseIDCombobox"].get()
        phrase =ChangeList["NewPhrasesBox"].get()
        button = ChangeList["Phrase"+role+"Button"]
        button.configure(text=phrase)
        button.update()
        ChangeList["LoginFrame"].update()
        top.mainloop()

