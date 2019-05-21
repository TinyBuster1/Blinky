import matplotlib
matplotlib.use('Agg')
import unittest
import BlinkyDataBaseManagment
import AdminPanel
import tkinter as tk
import pyodbc
import GUI
import MentorPanel
import support
import sendMsgs
import LoginAuth
import Forgot_password

class BlinkyTest(unittest.TestCase):
    BlinkyDataBaseManagment.createCursor()
    dataBase = BlinkyDataBaseManagment
    mainContainer = GUI
    mainContainerTest = GUI.MainPageContainer
    emptyList = []

    def test_DbConnection_value(self):
        print('tesing DbConnection value ')
        self.assertIsNotNone(self.dataBase.conn, 'its None')

 

    def test_Loginflag(self):
        print('tesing login flag value')
        self.assertEqual(BlinkyDataBaseManagment.loginFlag, 0, 'not equal')

    def test_Mentor_browse(self):
        print('tesing Mentor browse func')
        self.assertTrue(MentorPanel.browse, 'not equal')

    def test_allMentors(self):
        print('tesing allMentors func')
        self.assertEqual(type(BlinkyDataBaseManagment.allMentors()), list, 'not equal')

    def test_loadAllUsers(self):
        print('tesing loadAllUsers func')
        self.assertNotEqual(BlinkyDataBaseManagment.loadAllUsers("test"), list, 'not equal')

    def test_tempdirAdmin(self):
        print('tesing tempdir value for browse function')
        self.assertNotEqual(AdminPanel.tempdir, " ", 'not equal')

    def test_userChecker(self):
        print('tesing userChecker func')
        self.assertEqual(self.dataBase.userChecker('1', '2'), 0, 'not equal')

    def test_uploadImage1(self):
        print('tesing uploadImage func')
        self.assertFalse(self.dataBase.uploadImage('1', '2', '3', '4', '5', '6'))

    def test_uidCheck(self):
        print('tesing uidCheck func')
        self.assertEqual(self.dataBase.uidCheck('122'), 1)

    def test_midCheck(self):
        print('tesing midCheck func')
        self.assertTrue(self.dataBase.midCheck('1'))

    def test_patientsCheck(self):
        print('tesing patientsCheck func')
        self.assertEqual(self.dataBase.patientsCheck('1', '2'), 0, 'not equal')

    def test_registerMentormid(self):
        print('tesing registerMentor func')
        try:
            self.assertFalse(self.dataBase.registerMentor('3443', '123', '125', 'AMIT', 'A', '0525'), 1)
        except:
            print("cant register mentor")

    def test_imageCheck(self):
        print('tesing imageCheck func')
        self.assertFalse(self.dataBase.imageCheck('175254'), 1)

    def test_uploadImage(self):
        print('tesing uploadImage func from diffrent user')
        self.assertFalse(self.dataBase.uploadImage('121333', 'amit', 'sdkskclslc//', 'role', '125321', '120'), 1)

    def test_signPatient(self):
        print('tesing signPatient func')
        self.assertFalse(self.dataBase.signPatient('175254', '1213'), 1)

    def test_uploadTitle(self):
        print('tesing uploadTitle func')
        self.assertFalse(self.dataBase.uploadTitle('animal', '1213', '2e2232ds', 'sdsda', 'dsds'), 1)

    def test_log(self):
        print('tesing logSQLconnection() func')

        conn = pyodbc.connect(BlinkyDataBaseManagment.mySQLserver)
        cursor = conn.cursor()
        self.assertTrue(cursor)

    def test_numOfAdmins(self):
        print('testing num of admins function')
        self.assertEqual(self.dataBase.returnNumOfAdmins(), 1)

    def test_possitiveNumOfAdmins(self):
        print('testing num of admins is positive integer')
        self.assertGreater(self.dataBase.returnNumOfAdmins(), 0)

    def test_numOfUsers(self):
        print('testing num of users function')
        self.assertEqual(self.dataBase.returnNumOfUsers(), 2)

    def test_numOfMentors(self):
        print('testing num of mentors function')
        self.assertEqual(self.dataBase.returnNumOfUsers(), 2)

    def test_numOfPhrases(self):
        print('testing num of phrases function')
        self.assertNotEqual(self.dataBase.returnNumOfPhrases(), 3)

    def test_numOfPictures(self):
        print('testing num of pictures function')
        self.assertNotEqual(self.dataBase.returnNumOfPictures(), 3)

    def test_typeOfImageList(self):
        print('testing num of pictures function')
        self.assertIsInstance(self.dataBase.getAllImages(), list)

    def test_typeOfTitleList(self):
        print('testing num of pictures function')
        self.assertIsInstance(self.dataBase.getAllTitles(), list)

    def test_notNullOfImageList(self):
        print('testing not null num of pictures function')
        self.assertIsNotNone(self.dataBase.getAllImages())

    def test_notNullfTitleList(self):
        print('testing not null num of pictures function')
        self.assertIsNotNone(self.dataBase.getAllTitles())

    def test_user_info1(self):
        print('test_user_info ')
        self.assertEqual(self.dataBase.user_info(None), False)

    def test_user_info2(self):
        print('test_user_info ')
        self.assertEqual(self.dataBase.user_info('M1'), True)

    def test_user_info3(self):
        print('test_user_info ')
        self.assertEqual(self.dataBase.user_info(125), False)

    def test_user_info4(self):
        print('test_user_info ')
        self.assertEqual(self.dataBase.user_info('sdsd'), True)

    def test_user_info5(self):
        print('test_user_info ')
        self.assertEqual(self.dataBase.user_info(3.14), False)

    def test_user_medical_info1(self):
        print('test_user_info ')
        self.assertEqual(self.dataBase.medical_info(None), False)

    def test_user_medical_info2(self):
        print('test medical_info ')
        self.assertEqual(self.dataBase.medical_info('m'), True)

    def test_medical_info3(self):
        print('test medical_info')
        self.assertEqual(self.dataBase.medical_info(125), False)

    def test_user_medical_info4(self):
        print('test medical_info')
        self.assertEqual(self.dataBase.medical_info('sdsd'), False)

    def test_user_medical_info5(self):
        print('test medical_info ')
        self.assertEqual(self.dataBase.medical_info(3.14), False)

    def test_user_medical_info6(self):
        print('test medical_info ')
        self.assertEqual(self.dataBase.medical_info(-3.14), False)

    def test_user_medical_info7(self):
        print('test medical_info ')
        self.assertEqual(self.dataBase.medical_info(-1), False)



    ##Forgot password_u
    def test_Forgot_password_U_entry(self):
        print( 'testnig entry to Recover password')
        self.assertIsNotNone(self.dataBase.conn, 'its None')

    def test_Forgot_password_U_user(self):
        print('tesing user enter Forgot password func')
        self.assertTrue(Forgot_password.Forgot_password_U, 'not equal')

    def test_test_Forgot_password_U_database(self):
        print("testing sql concoction to change password")
        #print(type(pyodbc.connect(BlinkyDataBaseManagment.mySQLserver)))
        self.assertIsInstance(self.dataBase.conn,pyodbc.Connection)


    ##Forgot password_a
    def test_Forgot_password_A_entry(self):
        print( 'testnig entry to Recover password')
        self.assertRaises(Exception,Forgot_password.Forgot_password_A(self.testEntry2,self.testEntry1))

    def test_Forgot_password_A_user(self):
        print('tesing user enter Forgot password func')
        self.assertRaises(Exception,Forgot_password.Forgot_password_A(self.testEntry2,self.testEntry1))

    def test_Forgot_password_A_database(self):
        print("testing sql concoction to change password")
        self.assertIsInstance(self.dataBase.conn,pyodbc.Connection)

    ##test mentor

    def test_Forgot_password_M_entry(self):
        print('testnig entry to mentor to Recover password for user')
        self.assertRaises(Exception, Forgot_password.Forgot_password_M(';amit'))

    def test_Forgot_password_M_user(self):
        print('tesing mentor enter Forgot password func')
        self.assertRaises(Exception, Forgot_password.Forgot_password_M("sdsd"))

    def test_Forgot_password_M_database(self):
        print("testing sql concoction to change password")
        self.assertIsInstance(self.dataBase.conn, pyodbc.Connection)





    #support M
    def test_support_M1(self):
        print('testnig entry to mentor support_M')
        self.assertRaises(Exception, support.support_M())

    def test_support_M2(self):
        print('testnig entry to mentor support_M')
        self.assertEqual(support.support_M(),None)

    def test_support_M3(self):
        print('testnig entry to mentor support_M')
        self.assertFalse(support.support_M(),1)

    def test_test_support_M(self):
        print('testnig entry to mentor support_M')
        self.assertFalse(support.support_M(), 2)

    # support U
    def test_support_U1(self):
        print('testnig entry to user support_U')
        self.assertRaises(Exception, support.support_U())

    def test_support_U2(self):
        print('testnig entry to user support_U')
        self.assertEqual(support.support_U(), None)

    def test_support_U3(self):
        print('testnig entry to user support_U')
        self.assertFalse(support.support_U(), 1)

    def test_support_U4(self):
        print('testnig entry to user support_U')
        self.assertFalse(support.support_U(), 2)
        
    def test_login_auth1(self):
        print('testing email contains @ in feedback function')
        self.assertEqual(LoginAuth.sendFeedbackToContact("a","u","str"), False)

    def test_login_aut2(self):
        print('testing email contains @ in emergency function')
        self.assertEqual(LoginAuth.sendEMERGENCY("a","u"), False)

    def test_login_aut3(self):
        print('testing email contains @ in email function')
        self.assertEqual(LoginAuth.sendEmail("a"), False)

    def test_login_aut4(self):
        print('testing that email returns int value')
        self.assertEqual(type(LoginAuth.sendEmail("alexabo4@ac.sce.ac.il")), int)

    def test_sendMsg1(self):
        print('sending msg to user from mentor')
        self.assertEqual(sendMsgs.sendMsgtoUserFromMentor("m", self.emptyList), False)

    def test_sendMsg2(self):
        print('sending emergency to  mentor')
        self.assertEqual(sendMsgs.sendEMERGENCYtoMentorFromUser(""), False)

    def test_sendMsg3(self):
        print('sending msg to contacts')
        self.assertEqual(sendMsgs.sendFeedbackToContacts("m", self.emptyList), False)

    def test_sendMsg4(self):
        print('sending msg to mentor from user')
        self.assertEqual(sendMsgs.sendMsgtoMentorFromUser("m", self.emptyList), False)

    def test_sendMsg5(self):
        print('sending msg to user from mentor')
        self.assertEqual(sendMsgs.sendMsgtoMentorFromAdmin("m", self.emptyList), False)





if __name__ == '__main__':
    unittest.main()
    BlinkyDataBaseManagment.closeSQLconnection()
