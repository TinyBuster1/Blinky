import MentorPanel
import tkinter as tk
import unittest


class Hackathon(unittest.TestCase):

    
    def test_Mentor_browse(self):
        print('tesing Mentor browse func')
        self.assertTrue(MentorPanel.browse, 'not equal')

if __name__ == '__main__':
    unittest.main()
