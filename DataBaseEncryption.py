import pyodbc
import os
from shutil import copyfile
import sys
import GUIandDBCommunication
import tkinter as tk
from tkinter import messagebox
import datetime
import Pmw
from cryptography.fernet import Fernet

global mySQLserver
global conn
global cursor
global prog_call
global prog_location

prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
mySQLserver = 'Driver={SQL Server};''Server=DESKTOP-JQOUC01\SQLEXPRESS;''Database=BlinkyDB;''Trusted_Connection=yes;''Integrated Security=true''Column Encryption Setting=Enabled'

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated
