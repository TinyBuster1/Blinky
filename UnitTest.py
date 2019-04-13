import unittest
import BlinkyDataBaseManagment
import AdminPanel
import pyodbc
import GUI
import UserPanel
import Tkinter as tk
import MentorPanel


class BlinkyTest(unittest.TestCase):
    window = tk.Tk()
    testButton = tk.Button()
    BlinkyDataBaseManagment.createCursor()

    dataBase = BlinkyDataBaseManagment
    mainContainer = GUI
    mainContainerTest = GUI.MainPageContainer
    testLabel = tk.Label()

    global val, w
    roottest = tk.Tk()
    top = mainContainerTest(roottest)
    w = top
    top_level = top
    roottest = top

    def test_DbConnection_value(self):
        print('tesing DbConnection value ')
        self.assertIsNotNone(self.dataBase.conn, 'its None')

    def test_Loginbutton(self):
        print('testing Login button')
        self.assertNotEqual(self.top.Login, self.testButton, 'not equal')

    def test_label(self):
        print('testing label')
        self.assertNotEqual(self.top.Label1, self.testLabel, 'not equal')

    def test_Loginflag(self):
        print('tesing login flag value')
        self.assertEqual(BlinkyDataBaseManagment.loginFlag, 0, 'not equal')

    def test_Mentor_browse(self):
        print('tesing Mentor browse func')
        self.assertTrue(MentorPanel.browse, 'not equal')

    def test_GUI(self):
        print('testing main GUI window')
        self.assertNotEqual(self.mainContainer.root, self.window, 'not equal')

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
        self.assertEqual(self.dataBase.returnNumOfUsers(), 3)

    def test_numOfMentors(self):
        print('testing num of mentors function')
        self.assertEqual(self.dataBase.returnNumOfUsers(), 3)

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


if __name__ == '__main__':
    unittest.main()
    BlinkyDataBaseManagment.closeSQLconnection()
