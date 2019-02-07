#!/bin/env python2

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

print(cyan),("To Install My tools please check your internet")
print
print(red),("[Y atau T]")
print
asw = input("%sRoot%s@local%shost ==>> ")%(green,yellow,white)
print

if asw == Y:
         time.sleep(0.1)
         os.system("sh check")
         print ("%sYess%s... ")%(cyan,white)
         time.sleep(0.1)
         os.system("python2 Sddos.py")
         exit()
if asw == T:
         time.sleep(0.1)
         os.system("clear")
         print ("%sExiting....")
         time.sleep(0.1)
         print ("%sTo back %s>> %s python2 start.py")%(purple,green,white)
         sys.exit()
else:
         print ("%s Wrong %sInput")%(blue,yellow) 
         sys.exit()
         
