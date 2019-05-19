
import tkinter as tk
import unittest


class Hackathon(unittest.TestCase):

    roottest = tk.Tk()
    testLabel = tk.Label()
    testLabel1 = tk.Label()
    
    def test_label(self):
        print('testing label')
        self.assertNotEqual(self.testLabel1, self.testLabel, 'not equal')
