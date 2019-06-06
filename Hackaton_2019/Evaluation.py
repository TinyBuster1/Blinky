import datetime
import smtplib
import time
import sys
import os


### help GUI function ###

myCommit = "test"
now = datetime.datetime.now()
time1 =  now.day.__str__() + "/" + now.month.__str__() + "/" + now.year.__str__() + " at: " + now.time().__str__()

def GUI():
    print(" calling GUI window , testing benchmark.")
'''	
	
### 4 Evaluation and vision ###
precent = 1.1
def Evaluation(precent):
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    reports = prog_location + "\\" + "test.txt"
    with open(reports, "r") as f:
        eval = f.read()
        print(eval)
    start_time = time.time()
    GUI()
    endTime = now.time()
    total = time.time() - start_time
    print(total*precent)
    print(eval)
    if total*precent > float(eval):
        print("The program is running to slow compared to the last build.")
    f.close()
    with open(reports, "w") as f:
        f.write(str(total))
        f.close()
'''
GUI()
