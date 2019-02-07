 #!/usr/bin/python
 
import os
import sys,time

os.system("clear")
os.system("figlet Welcome | lolcat")
print ("\033[1;32mLogin Dulu ea")
print ("\033[1;31;1mPm StarFuckTak'-' Dikalau anda bosan wkwk")
ID='FUCKKING'      
password='240918'

def restart():
        os.system("python2 eaa.py")

def main():
	user = raw_input("username : ")
	if user == ID:
		pwna = raw_input("password : ")

		if pwna == password:
			print "\n\033[1;34mSukses!!", 
			exit()

		else:
			print "\n\033[1;36mMaafkeun Aing Anda Harus Mengulang !!!\033[00m"
			print "Back Login\n"
			restart()
			
	else:
		print "\n\033[1;36mSalah ID cuk =(\033[00m"
		print "Back Login\n"
time.sleep(2)
print 
print ("\033[94m")
try:
	main()
except KeyboardInterrupt:
	restart()
