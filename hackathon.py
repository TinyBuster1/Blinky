import datetime

myCommit = "test"
now = datetime.datetime.now()
time =  now.day.__str__() + "/" + now.month.__str__() + "/" + now.year.__str__() + " at: " + now.time().__str__()

def print_time(time,myCommit):
    print("Latest commit is done at: " + time + ", commit: " + myCommit)

print_time(time,myCommit)
