#!/usr/bin/env python2

blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
white='\033[37;1m'
yellow='\033[33;1m'
red='\033[1;91m'

import os
import time
import sys

os.system("clear")
time.sleep(0.1)
print ("______________________________________________________________________")
print(cyan),("To Install My tools please check your internet")
print
print(red),("[1. ] Ya ")
print(green),("[2. ] Tidak")
print
print(purple),("[!] Vol (-) + z to exit.. ")
print(white),("______________________________________________________________________")
print
pilih = input("\033[36;1mRoot@StarFuckTak ==>> ")
print

if pilih == 1:
         time.sleep(0.1)
         os.system("sh check")
         print ("\033[36;1mYess%s... ")
         time.sleep(0.1)
         os.system("python2 Sddos.py")
         exit()
if pilih == 2:
         time.sleep(0.1)
         os.system("clear")
         print "%sExiting%s...."%(green,white)
         time.sleep(0.1)
         print "%sTo back %s>> %s python2 start.py"%(purple,green,white)
         sys.exit()
else:
         print "%s Wrong %sInput"%(blue,yellow) 
         sys.exit()
