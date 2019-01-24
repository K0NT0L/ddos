 #!/system/xbin/bash

#Coded by StarFuckTak:b

blue='\033[34;1m'
green='\033[32;1m'  
purple='\033[35;1m'
cyan='\033[36;1m'
white='\033[37;1m'                                           
yellow='\033[33;1m'
red='\033[1;91m'

 clear 
 clear 
 
 toilet -f pagga Welcome 
 echo "$cyan To Running My tools"
echo "$green please check your internet{Y/N}"
echo "" 
read -p "-# " kntl; 


if [ $kntl = Y ] || [ $kntl = y ]
then
clear 
sh check 
echo ""
echo "" 
 sleep 2
 apt install python python2 vim figlet curl
pkg install php
pip2 install lolcat
pip2 install mechanize
clear
clear
python2 Sddos.py
fi 

if [ $kntl = N ] || [ $kntl = n ]
then
clear
toilet -f standard "Thanks" | lolcat 
echo "$purple Trying To exit... "
echo ""
fi 
