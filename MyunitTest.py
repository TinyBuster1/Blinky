import unittest
import BlinkyDataBaseManagment
import AdminPanel
import pyodbc
import GUI
import UserPanel
import MentorPanel


import Forgot_password
import support

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk



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



    testEntry1 = tk.Entry()
    testEntry1.insert(0,'a default value')
    testEntry2=testEntry1


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
        #print(type(pyodbc.connect(BlinkyDataBaseManagment.mySQLserver)))
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
    def test_support_M(self):
        print('testnig entry to mentor support_M')
        self.assertRaises(Exception, support.support_M())

    def test_support_M(self):
        print('testnig entry to mentor support_M')
        self.assertEqual(support.support_M(),None)

    def test_support_M(self):
        print('testnig entry to mentor support_M')
        self.assertFalse(support.support_M(),1)

    def test_test_support_M(self):
        print('testnig entry to mentor support_M')
        self.assertFalse(support.support_M(), 2)

    # support U
    def test_support_U(self):
        print('testnig entry to user support_U')
        self.assertRaises(Exception, support.support_U())

    def test_support_U(self):
        print('testnig entry to user support_U')
        self.assertEqual(support.support_U(), None)

    def test_support_U(self):
        print('testnig entry to user support_U')
        self.assertFalse(support.support_U(), 1)

    def test_support_U(self):
        print('testnig entry to user support_U')
        self.assertFalse(support.support_U(), 2)

