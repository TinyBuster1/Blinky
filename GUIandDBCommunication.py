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
        BlinkyDataBaseManagment.registerUser(UserList["UserID"].get(),UserList["UserPassword1"].get(),UserList["UserPassword2"].get(),
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
        

    
    