from datetime import *
import time
import ctypes
import Data.data as data
import os
import sys
from playsound import playsound

ctypes.windll.kernel32.SetConsoleTitleW("Gift")




clear = lambda: os.system('cls')

def start():  

    # change these variables

    BDmonth = 6
    BDday = 27
    name = "REDACTED"
    authorName = "Nick"
    wishes = """
    I wish you...
    """

    # other code

    path = os.getcwd()
    now = datetime.now()
    today = date.today()
    NWyear = now.year
    kadBD = date(now.year, BDmonth, BDday) # date of birthday 
    nowDate = date(now.year, now.month, now.day)
    if len(str(BDday)) == 1:
        BDday = f"0{BDday}"
    if len(str(BDmonth)) == 1:
        BDmonth = f"0{BDmonth}"
    if str(today) == f"{NWyear}-{BDmonth}-{BDday}": # date of birthday 
        path = os.getcwd()
        print("")
        time.sleep(5)
        clear()
        BDyear = input("[Year when you got born]{>} ")
        KadYears = now.year - int(BDyear)
        print("")
        time.sleep(5)
        clear()
        print(f"{data.cake}\n\n")
        try:
            playsound(f'{path}/Data/Audio/bd.mp3')
        except Exception:
            print("Open this in path where is no latin words or something")
            time.sleep(10)
            sys.exit()
        print(f"   You are {KadYears} years old now :D")
        time.sleep(3)
        clear()

        print(f"Happy Birthday Dear {name}! [From {authorName}] (Ctrl+C to close)")
        try:
            playsound(f'{path}\\Data\\Audio\\yeah.mp3')
        except Exception:
            print("Open this in path where is no latin words or something")
            time.sleep(10)
            sys.exit()
        print(wishes)

        while True:
            a = 1 + 1
    else:
        delta = kadBD - nowDate
        print(f"Please, don't open this program. Open it after {delta.days} >_<")
    
try:
    today = date.today()
    print(today)
    start()
except KeyboardInterrupt:
    print()
    print("Exiting...")
