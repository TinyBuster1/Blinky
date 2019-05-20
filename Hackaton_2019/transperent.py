import datetime
import smtplib
import time
import sys
import os

#### 2  Everyone can see what's happening ####
myCommit = "test"
now = datetime.datetime.now()
time1 =  now.day.__str__() + "/" + now.month.__str__() + "/" + now.year.__str__() + " at: " + now.time().__str__()

emailList = ["alexabo4@ac.sce.ac.il"]
def send_Mails(emailList,time1):
    for mail in emailList:
        if '@' not in mail:
            return False
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("blinkysendmsg@gmail.com", "sukablyat123")

        message = 'Subject: {}\n\n{}'.format('new code commit! at', time1)
        s.sendmail("blinkysendmsg@gmail.com", mail, message)
        s.quit()

send_Mails(emailList,time1)
