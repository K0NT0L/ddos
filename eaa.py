 #!/usr/bin/python
 
import os
import sys,time

os.system("clear")
os.system("figlet Welcome | lolcat")
print ("\033[1;32mLogin Dulu ea")
print ("\033[1;31;1mPm StarFuckTak'-' Dikalau anda bosan wkwk")
username='FUCKKING'      
password='240918'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mSukses!!", 
			exit()

		else:
			print "\n\033[1;36mMaafkeun Aing Anda Harus Mengulang !!!\033[00m"
			print "Back Login\n"
			restart()
			
	else:
		print "\n\033[1;36mSorry Invalid Username !!!\033[00m"
		print "Back Login\n"
time.sleep(2)
os.system("python2 eaa.py")

try:
	main()
except KeyboardInterrupt:
system('clear')
	restart()
