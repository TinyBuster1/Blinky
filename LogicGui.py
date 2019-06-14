import BlinkyDataBaseManagment
import GUI
import NewUserRegister
import RegisterNewMentor
import Infohelp
import tkinter as tk
import FeedbackFrame
import UserPanel
import MentorPanel
import AdminPanel
import Forgot_password
import GUIandDBCommunication
import MouseCursorControl

global picIndex
global phraseIndex
picIndex = 0
phraseIndex = 0

class LogicGui:
    @staticmethod
    def returnToMainFromUser(self, top):
        self.PatientRegisterFrame.destroy()
        tk.Frame(GUI.vpReturnToMain(top))

    @staticmethod
    def returnToMainFromMentor(self,top,flag=None):
        if flag is None:
            self.RegisterNewMentorFrame.destroy()
            tk.Frame(GUI.vpReturnToMain(top))
        if flag == 1:
            self.RegisterNewMentorFrame.destroy()
            tk.Frame(AdminPanel.AdminPanel().create_AdminPanelWin(top))


    @staticmethod
    def RegNewMenWin(self,top,flag=None):
        if flag is None:
            self.MainPageFrame.destroy()
            tk.Frame(RegisterNewMentor.RegisterNewMentorLevel().create_RegMentor(top))
        if flag == 1:
            self.AdminOptions.destroy()
            tk.Frame(RegisterNewMentor.RegisterNewMentorLevel().create_RegMentor(top, 1))

    @staticmethod
    def RegNewUserWin(self, top):
        self.MainPageFrame.destroy()
        tk.Frame(NewUserRegister.UserRegister().Create_RegNewUSer(top))

    @staticmethod
    def ShowInfo(self, top):
        self.MainPageFrame.destroy()
        tk.Frame(Infohelp.InfoFrame().create_InfoWin(top))

    @staticmethod
    def InfoBackToMain(self,top):
        self.Frame1.destroy()
        tk.Frame(GUI.vpReturnToMain(top))

    @staticmethod
    def FeedBackWin(self,top):
        self.Frame1.destroy()
        tk.Frame(FeedbackFrame.FeedBackFrame().create_FeedBackWin(top))

    @staticmethod
    def BackToInfoHelp(self,top):
        self.Feedback.destroy()
        tk.Frame(Infohelp.InfoFrame().create_InfoWin(top))

    @staticmethod
    def OpenUserPanelWin(self,UserID,PicAndPharases, top):
        self.MainPageFrame.destroy()
        tk.Frame(UserPanel.UserPanel().create_UserPanelWin(UserID,PicAndPharases,top))

    @staticmethod
    def OpenMentorPanelWin(self,MentorID, top):
        self.MainPageFrame.destroy()
        tk.Frame(MentorPanel.MentorPanel().create_MentorPanelWin(MentorID, top))

    @staticmethod
    def OpenAdminPanelWin(self,adminID,top):
        self.MainPageFrame.destroy()
        tk.Frame(AdminPanel.AdminPanel().create_AdminPanelWin(adminID,top))

    @staticmethod
    def LogoutfromUser(self, top):
        BlinkyDataBaseManagment.closeSQLconnection()
        self.LoginFrame.destroy()
        MouseCursorControl.Destroy_eye_tracker()
        tk.Frame(GUI.vpReturnToMain(top))

    @staticmethod
    def LogoutfromMentor(self, top):
        BlinkyDataBaseManagment.closeSQLconnection()
        self.MentorCntPnl.destroy()
        tk.Frame(GUI.vpReturnToMain(top))

    @staticmethod
    def LogoutfromAdmin(self, top):
        BlinkyDataBaseManagment.closeSQLconnection()
        self.AdminOptions.destroy()
        tk.Frame(GUI.vpReturnToMain(top))

    @staticmethod
    def updateChosenPic(index, top, ChangeList):
            global picIndex
            if( picIndex != 0):
                oldPicture = ChangeList["pic" + str(picIndex) + "button"]
                oldPicture.configure(activebackground="#ececec")
                oldPicture.configure(activeforeground="#000000")
                oldPicture.configure(background="#d9d9d9")
                oldPicture.configure(disabledforeground="#a3a3a3")
                oldPicture.configure(foreground="#000000")
                oldPicture.configure(highlightbackground="#d9d9d9")
                oldPicture.configure(highlightcolor="black")

            picIndex = index
            chosenButton = ChangeList["pic"+str(index)+"button"]
            chosenButton.configure(relief=tk.GROOVE, borderwidth=5, background="#2244FF", activebackground="#FF0000", highlightcolor="#00FF00")
            chosenButton.configure(borderwidth=10)
            chosenButton.configure(pady="0")
            chosenButton.update()
            ChangeList["LoginFrame"].update()
            top.mainloop()


    @staticmethod
    def updateChosenPhrase(index1, top, ChangeList):
        global phraseIndex
        if (phraseIndex != 0):
            oldPhrase = ChangeList["Phrase" + str(phraseIndex) + "Button"]
            oldPhrase.configure(activebackground="#ececec")
            oldPhrase.configure(activeforeground="#000000")
            oldPhrase.configure(background="#d9d9d9")
            oldPhrase.configure(disabledforeground="#a3a3a3")
            oldPhrase.configure(foreground="#000000")
            oldPhrase.configure(highlightbackground="#d9d9d9")
            oldPhrase.configure(highlightcolor="black")
            oldPhrase.configure(borderwidth=2)
            oldPhrase.configure(pady="0")

        phraseIndex = index1
        chosenButton = ChangeList["Phrase" + str(index1) + "Button"]
        chosenButton.configure(relief=tk.GROOVE, borderwidth=5, background="#2244FF",
                               activebackground="#FF0000",
                               highlightcolor="#00FF00")
        chosenButton.configure(borderwidth=10)
        chosenButton.configure(pady="0")
        chosenButton.update()
        ChangeList["LoginFrame"].update()
        top.mainloop()
        
        
        
        
        
        
        
