
import tkinter as tk
import unittest


class Hackathon(unittest.TestCase):

    
    def test_numOfAdmins(self):
        print('testing num of admins function')
        self.assertEqual(self.dataBase.returnNumOfAdmins(), 1)
if __name__ == '__main__':
    unittest.main()
