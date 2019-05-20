import datetime
import smtplib
import time
import sys
import os

def GUI():
    print(" calling GUI window , testing benchmark.")
	
### 3 Benchmark ####
numOfRuns = 4000
def benchmark(numOfRuns):
    start_time = time.time()
    for i in range(numOfRuns):
        GUI()
    endTime = now.time()
    total = time.time() - start_time
    print("total time of benchmark: " + str(total))