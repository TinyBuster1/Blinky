
import unittest
import datetime

class Hackathon(unittest.TestCase):
    now = datetime.datetime.now()
    time =  now.day.__str__() + "/" + now.month.__str__() + "/" + now.year.__str__() + " at: " + now.time().__str__()

    def print_time(self):
        print("Latest commit is done at: " + self.time)

if __name__ == '__main__':
    unittest.main()
