import pyodbc
import tkinter
from tkinter import messagebox

import BlinkyDataBaseManagment
from doctest import master
from functools import partial

import LogicGui

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk



def support_M():
    root = tk.Tk()
    root.title("mentor support")
    root.geometry("1032x741+544+110")




    Frame1 = tk.Frame(root)
    Frame1.place(relx=0.097, rely=0.027, relheight=0.81, relwidth=0.775)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief='groove')
    Frame1.configure(background="#d9d9d9")
    Frame1.configure(width=350)



    infoLabel = tk.Label(Frame1)
    infoLabel.place(relx=0.213, rely=0.033, height=91, width=425)
    infoLabel.configure(background="#d9d9d9")
    infoLabel.configure(disabledforeground="#a3a3a3")

    infoLabel.configure(foreground="#000000")
    infoLabel.configure(text='''Information and help''')
    infoLabel.configure(width=425)


    Contactinfo = tk.Label(Frame1)
    Contactinfo.place(relx=0.025, rely=0.533, height=51, width=289)
    Contactinfo.configure(background="#d9d9d9")
    Contactinfo.configure(disabledforeground="#a3a3a3")

    Contactinfo.configure(foreground="#000000")
    Contactinfo.configure(text='''Contact:''')
    Contactinfo.configure(width=289)

    TechLabel = tk.Label(Frame1)
    TechLabel.place(relx=0.088, rely=0.667, height=51, width=289)
    TechLabel.configure(background="#d9d9d9")
    TechLabel.configure(disabledforeground="#a3a3a3")

    TechLabel.configure(foreground="#000000")
    TechLabel.configure(text='''Technical support:''')
    TechLabel.configure(width=289)

    rick = tk.Label(Frame1)
    rick.place(relx=0.45, rely=0.567, height=26, width=282)
    rick.configure(background="#d9d9d9")
    rick.configure(disabledforeground="#a3a3a3")
    rick.configure(foreground="#000000")
    rick.configure(text='''professor Sanchez Rick : 050-000-0000''')
    rick.configure(width=282)

    mortysanchez = tk.Label(Frame1)
    mortysanchez.place(relx=0.463, rely=0.683, height=26, width=269)
    mortysanchez.configure(background="#d9d9d9")
    mortysanchez.configure(disabledforeground="#a3a3a3")
    mortysanchez.configure(foreground="#000000")
    mortysanchez.configure(text='''Doctor Sanchez Morty : 050-000-0001''')
    mortysanchez.configure(width=269)

    infolabel = tk.Label(Frame1)
    infolabel.place(relx=0.2, rely=0.183, height=46, width=462)
    infolabel.configure(background="#d9d9d9")
    infolabel.configure(disabledforeground="#a3a3a3")
    infolabel.configure(foreground="#000000")
    infolabel.configure(text='''We started in 2016 and we're still going strong.''')
    infolabel.configure(width=462)

    blinky = tk.Label(Frame1)
    blinky.place(relx=0.238, rely=0.267, height=46, width=394)
    blinky.configure(background="#d9d9d9")
    blinky.configure(disabledforeground="#a3a3a3")
    blinky.configure(foreground="#000000")
    blinky.configure(text='''Easy to use, accurate.Learn why the Bllinky is the eye-tracking device of choice''')


    action_with_args = partial(LogicGui.LogicGui.FeedBackWin,)


    powerlabel = tk.Label(Frame1)
    powerlabel.place(relx=0.125, rely=0.367, height=26, width=567)
    powerlabel.configure(background="#d9d9d9")
    powerlabel.configure(disabledforeground="#a3a3a3")
    powerlabel.configure(foreground="#000000")
    powerlabel.configure( text='''combines powerful processing with the worlds most advanced eye tracking platform''')

def support_U():
    root = tk.Tk()
    root.title("user support")
    root.geometry("1032x741+544+110")


    Frame1 = tk.Frame(root)
    Frame1.place(relx=0.097, rely=0.027, relheight=0.81, relwidth=0.775)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief='groove')
    Frame1.configure(background="#d9d9d9")
    Frame1.configure(width=350)



    infoLabel = tk.Label(Frame1)
    infoLabel.place(relx=0.213, rely=0.033, height=91, width=425)
    infoLabel.configure(background="#d9d9d9")
    infoLabel.configure(disabledforeground="#a3a3a3")
    #infoLabel.configure(font=font9)
    infoLabel.configure(foreground="#000000")
    infoLabel.configure(text='''Information and help''')
    infoLabel.configure(width=425)


    Contactinfo = tk.Label(Frame1)
    Contactinfo.place(relx=0.025, rely=0.533, height=51, width=289)
    Contactinfo.configure(background="#d9d9d9")
    Contactinfo.configure(disabledforeground="#a3a3a3")

    Contactinfo.configure(foreground="#000000")
    Contactinfo.configure(text='''Contact:''')
    Contactinfo.configure(width=289)

    TechLabel = tk.Label(Frame1)
    TechLabel.place(relx=0.088, rely=0.667, height=51, width=289)
    TechLabel.configure(background="#d9d9d9")
    TechLabel.configure(disabledforeground="#a3a3a3")

    TechLabel.configure(foreground="#000000")
    TechLabel.configure(text='''Technical support:''')
    TechLabel.configure(width=289)

    rick = tk.Label(Frame1)
    rick.place(relx=0.45, rely=0.567, height=26, width=282)
    rick.configure(background="#d9d9d9")
    rick.configure(disabledforeground="#a3a3a3")
    rick.configure(foreground="#000000")
    rick.configure(text='''professor Sanchez Rick : 050-000-0000''')
    rick.configure(width=282)

    mortysanchez = tk.Label(Frame1)
    mortysanchez.place(relx=0.463, rely=0.683, height=26, width=269)
    mortysanchez.configure(background="#d9d9d9")
    mortysanchez.configure(disabledforeground="#a3a3a3")
    mortysanchez.configure(foreground="#000000")
    mortysanchez.configure(text='''Doctor Sanchez Morty : 050-000-0001''')
    mortysanchez.configure(width=269)

    infolabel = tk.Label(Frame1)
    infolabel.place(relx=0.2, rely=0.183, height=46, width=462)
    infolabel.configure(background="#d9d9d9")
    infolabel.configure(disabledforeground="#a3a3a3")
    infolabel.configure(foreground="#000000")
    infolabel.configure(text='''We started in 2016 and we're still going strong.''')
    infolabel.configure(width=462)

    blinky = tk.Label(Frame1)
    blinky.place(relx=0.238, rely=0.267, height=46, width=394)
    blinky.configure(background="#d9d9d9")
    blinky.configure(disabledforeground="#a3a3a3")
    blinky.configure(foreground="#000000")

    action_with_args = partial(LogicGui.LogicGui.FeedBackWin,)


    powerlabel = tk.Label(Frame1)
    powerlabel.place(relx=0.125, rely=0.367, height=26, width=567)
    powerlabel.configure(background="#d9d9d9")
    powerlabel.configure(disabledforeground="#a3a3a3")
    powerlabel.configure(foreground="#000000")
    powerlabel.configure( text='''combines powerful processing with the worlds most advanced eye tracking platform''')



