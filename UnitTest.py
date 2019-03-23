# Blinky
Eye tracking &amp; virtual keyboard application to improve communication for disabled people.

import unittest
import pyodbc

import BlinkyDataBaseManagment


class MyTestCase(unittest.TestCase):
    dataBase = BlinkyDataBaseManagment

    def test_userChecker(self):
            print('tesing userChecker func')
            self.assertEqual(self.dataBase.userChecker(1, 2), 0, 'not equal')
    def test_uploadImage(self):
            print('tesing uploadImage func')
            self.assertFalse(self.dataBase.uploadImage(1, 2, 3, 4, 5, 6))
    def test_uidCheck(self):
            print('tesing uidCheck func')
            self.assertEqual(self.dataBase.uidCheck('122'),1)
    def test_midCheck(self):
            print('tesing midCheck func')
            self.assertTrue(self.dataBase.midCheck(1))
    def test_patientsCheck(self):
            print('tesing patientsCheck func')
            self.assertEqual(self.dataBase.patientsCheck(1, 2), 0, 'not equal')
    def test_registerMentormid(self):
       print('tesing registerMentor func')
       self.assertFalse(self.dataBase.registerMentor('3443','123', '125', 'AMIT', 'A', '0525'),1)
    def test_imageCheck(self):
        print('tesing imageCheck func')
        self.assertFalse(self.dataBase.imageCheck('175254'),1 )
    def test_uploadImage(self):
         print('tesing uploadImage func')
         self.assertFalse(self.dataBase.uploadImage('121333','amit','sdkskclslc//','role','125321','120'),1)
    def test_signPatient(self):
        print('tesing signPatient func')
        self.assertFalse(self.dataBase.signPatient('175254','1213'),1 )
    def test_uploadTitle(self):
         print('tesing uploadTitle func')
         self.assertFalse(self.dataBase.uploadTitle('animal','1213','2e2232ds','sdsda','dsds'),1)

    def test_log(self):
         print('tesing logSQLconnection() func')

         conn = pyodbc.connect("Driver={SQL Server};"  
                               "Server=LAPTOP-L7B6A755;" 
                               "Database=BlinkyDB;"  
                               "Trusted_Connection=yes;")
         cursor = conn.cursor()
         self.assertTrue(cursor)
        
    def test_Loginflag(self):
        print('tesing login flag value')
        self.assertEqual(BlinkyDataBaseManagment.loginFlag,0,'not equal')
        
    
    def test_Mentor_browse(self):
        print('tesing Mentor browse func')
        self.assertTrue(MentorPanel.browse(""),'not equal')
        
    def test_allMentors(self):
        print('tesing allMentors func')
        self.assertEqual(type(BlinkyDataBaseManagment.allMentors()),list,'not equal')
        
    def test_loadAllUsers(self):
        print('tesing loadAllUsers func')
        self.assertNotEqual(BlinkyDataBaseManagment.loadAllUsers("test"),list,'not equal')
                 
    def test_tempdirAdmin(self):
        print('tesing tempdir value for browse function')
        self.assertNotEqual(AdminPanel.tempdir," ",'not equal')


if __name__ == '__main__':
    unittest.main()
