import datetime


now = datetime.datetime.now()
time =  now.day.__str__() + "/" + now.month.__str__() + "/" + now.year.__str__() + " at: " + now.time().__str__()

def print_time(time):
    print("Latest commit is done at: " + time)

print_time(time)
