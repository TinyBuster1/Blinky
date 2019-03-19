import GUI
import NewUserRegister
import RegisterNewMentor
import Tkinter as tk
import LogicGui
import BlinkyDataBaseManagment
import sys
import os.path


class GUIandDB:
    @staticmethod
    def checkUserInput(self,UserList,top):
        BlinkyDataBaseManagment.registerUser(UserList["UserID"].get(),UserList["UserPassword1"].get(),
                                             UserList["PatientName"].get(),UserList["UserLastName"].get(),
                                             UserList["MentorID"].get(),UserList["UserAge"].get(),
                                             UserList["UserGender"].get(),UserList["PatientDOB"].get(),
                                             UserList["UserPhone"].get(),UserList["UserAddress"].get(),
                                             UserList["UserContact1"].get(),UserList["UserContact2"].get(),
                                             UserList["UserMedical"].get(),UserList["UserDiet"].get())
        LogicGui.LogicGui.returnToMainFromUser(self, top)
        
    @staticmethod
    def checkMentorInput(self,MentorList,top):
        BlinkyDataBaseManagment.registerMentor(MentorList["MentorID"].get(), MentorList["MentorPassword1"].get(),
                                               MentorList["MentorPassword2"].get(),MentorList["MentorName"].get(),
                                               MentorList["MentorLastName"].get(),MentorList["MentorPhone"].get())
        LogicGui.LogicGui.returnToMainFromMentor(self, top)
        
    @staticmethod
    def Logged(self, LoginList, top):
        
        userType = BlinkyDataBaseManagment.userChecker(LoginList["UserNameText"].get(),LoginList["PasswordText"].get())
        
        if userType == 1:
            # here do the transfer to admin page

            LogicGui.LogicGui.OpenAdminPanelWin(self, top)
            print("Admin login success!")
        elif userType == 2:
            # here do the transfer to mentor page
            LogicGui.LogicGui.OpenMentorPanelWin(self, top)
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

            LogicGui.LogicGui.OpenUserPanelWin(self,LoginList["UserNameText"].get(), PicAndPharases, top)
            print("User login success!")
        else:
            print("wrong id or password please try again!")


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


    
