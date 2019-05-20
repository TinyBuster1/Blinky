import datetime
import smtplib
import time
import sys
import os

#### 1 Everyone Commits To the Mainline Every Day ####

myCommit = "test"
now = datetime.datetime.now()
time1 =  now.day.__str__() + "/" + now.month.__str__() + "/" + now.year.__str__() + " at: " + now.time().__str__()

def print_time(time,myCommit):
    print("Latest commit is done at: " + time + ", commit: " + myCommit)

print_time(time1, myCommit)
