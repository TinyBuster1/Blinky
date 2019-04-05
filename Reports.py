import Tkinter as tk
import sys
import os
import BlinkyDataBaseManagment

global prog_call
global prog_location

prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]

def FeedbackReport():
    global prog_location
    root = tk.Tk()
    root.title("Feedback Report")
    root.geometry("500x500")
    reports = prog_location + "\Reports" + "\\" + "FeedbackReport.txt"
    with open(reports, "r") as f:
        tk.Label(root, text=f.read()).pack()
    root.mainloop()
    f.close()
	
def exceptionReport():
    global prog_location
    root = tk.Tk()
    root.title("Exception report")
    root.geometry("500x500")
    reports = prog_location + "\Reports" + "\\" + "exceptionReport.txt"
    with open(reports, "r") as f:
        tk.Label(root, text=f.read()).pack()
    root.mainloop()
    f.close()