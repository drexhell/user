#This program for add new user in any linux os.
#AUTHER = AYUSH DALE

import os
import crypt

def newuser():

    uname=input("Select Username: \n")
    upass=input("Select Password : \n")
    #The encryption module seems to solve the obvious security leak,
    ucrypt=crypt.crypt(upass,"123")
    os.system("useradd -m -p "+upass+" "+uname)

newuser()
