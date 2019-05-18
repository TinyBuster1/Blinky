# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
import random
import socket

def sendRecoveryPassword(id, email, password):
    if '@' not in email:
        return False
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("blinkysendmsg@gmail.com", "sukablyat123")
    number = random.randint(1000,9999)
    num = str(number)
    message = 'Subject: {}\n\n{}'.format('Password Recovery', id + ' Your Password is: '+password)
    s.sendmail("blinkysendmsg@gmail.com", email, message)
    s.quit()
    return True

def sendEmail(email):
    if '@' not in email:
        return False
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("blinkysendmsg@gmail.com", "sukablyat123")
    number = random.randint(1000,9999)
    num = str(number)
    message = 'Subject: {}\n\n{}'.format('Login Authentication','your pin code is: '+num)
    s.sendmail("blinkysendmsg@gmail.com", email, message)
    s.quit()
    return number


def sendEMERGENCY(email, userid):
    if '@' not in email:
        return False
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("blinkysendmsg@gmail.com", "sukablyat123")

    message = 'Subject: {}\n\n{}'.format('EMERGENCY','THE USER: '+ userid + " PRESSED THE EMERGENCY BUTTON!!!")
    s.sendmail("blinkysendmsg@gmail.com", email, message)
    s.quit()
    return True

def sendFeedbackToContact(email,userid,feedback):
    if '@' not in email:
        return False
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("blinkysendmsg@gmail.com", "sukablyat123")
    message = 'Subject: {}\n\n{}'.format('Feedback', 'feedback for user: ' + userid + " " + feedback)
    s.sendmail("blinkysendmsg@gmail.com", email, message)
    s.quit()
    return True
