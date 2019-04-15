# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
import random

def sendEmail(email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("blinkysendmsg@gmail.com", "sukablyat123")
    number = random.randint(1000,9999)
    num = str(number)
    message = 'Subject: {}\n\n{}'.format('Login Authentication','your pin code is: '+num)
    s.sendmail("blinkysendmsg@gmail.com", email, message)
    s.quit()
    return number