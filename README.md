# Birthday App

This is a program that congratulates your friend or you on your birthday.
-----
## How to change names, dates and wishes

Open ``main.py`` and change only these variables:
```py

    # change these variables

    BDmonth = 6  #birthday month
    BDday = 27  #birthday day
    name = "REDACTED"  #Name of the birthday boy/girl
    authorName = "Nick"  # Author  name
    wishes = """  
    I wish you...
    """  #wishes

```

And after this, build it.

Requirements:

 - ctypes
 - datetime
 - playsound
 - time
 - pyinstaller

## Build it 

1. Open cmd in folder with script

2. Run this command to build app
```
pyinstaller main.py -n Gift -i Gift.ico --onefile
```

3. Find work application in dist folder

4. Put Data folder in dist folder

5. Profit!

# Credits

Birthday music - Birthday Boy by Squimpus McGrimpus  [Link](https://www.youtube.com/watch?v=0NLaekB_afE)
