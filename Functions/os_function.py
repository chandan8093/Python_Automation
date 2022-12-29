'''
import os
import time
import platform

if platform.system()=="windows":
    print("Wait for cleaaring the screen . . . ")
    time.sleep(3)
    os.system("cls")

    print("Wait for listing directory and files . . . ")
    time.sleep(3)
    os.system("dir")
else:
    print("Linux type os")
    print("Wait for cleaaring the screen . . . ")
    time.sleep(3)
    os.system("clear")

    print("Wait for listing directory and files . . . ")
    time.sleep(3)
    os.system("ls -lrt")

'''
#The above logic can be reduced by FUNCTIONS

import os
import time
import platform

def call(x,y):
    print("Wait for cleaaring the screen . . . ")
    time.sleep(3)
    os.system(x)

    print("Wait for listing directory and files . . . ")
    time.sleep(3)
    os.system(y)
if platform.system()=="Windows":
    call("cls","dir")
else:
    call("clear","ls -lrt")