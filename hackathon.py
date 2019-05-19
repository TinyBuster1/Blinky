import datetime
import smtplib

#### 1 Everyone Commits To the Mainline Every Day ####

myCommit = "test"
now = datetime.datetime.now()
time =  now.day.__str__() + "/" + now.month.__str__() + "/" + now.year.__str__() + " at: " + now.time().__str__()

def print_time(time,myCommit):
    print("Latest commit is done at: " + time + ", commit: " + myCommit)

print_time(time, myCommit)


#### 2  Everyone can see what's happening ####

emailList = ["alexabo4@ac.sce.ac.il"]
def send_Mails(emailList,time):
    for mail in emailList:
        if '@' not in mail:
            return False
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("blinkysendmsg@gmail.com", "sukablyat123")

        message = 'Subject: {}\n\n{}'.format('new code commit! at',time)
        s.sendmail("blinkysendmsg@gmail.com", mail, message)
        s.quit()
send_Mails(emailList,time)
