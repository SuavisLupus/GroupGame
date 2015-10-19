""" splash screen """

import os
import time
from game import*

string1 = "\n\n\n\nlong,long time ago in a magical place called RUSSIA...."
string2 = "\n\n\n\n   A SUPER EXTRA-BRILLIANT RUSSIAN Scientist" 
string2 +="\n  WITH EXTRA-ORDINARY PROGRAMMING PROWESS EXISTED,"
string2 +="\n	HIS NAME WAS... \n\n\n\n                KIRILL\n\n\
			 \n\n\nABLE TO fix ERRORS with a SINGLE line of code\n\n\nABLE to create 3 dimensional models which no one understands\n\n\nAble to breakdown the entire world into Binary\n\n\nABLE TO SPOT BUGS WITHOUT opening his eyes"
string3 = "\n\n\n\n    IN SOVIET RUSSIA...\n\n\n\n\n\n     THE PROGRAMS RUN YOU\n\n\n\n         and now comrad... you will re-live his story\n"

endTime1 = time.time() + 1*4
endTime2 = time.time() + 1*13
endTime3 = time.time() + 1*20

printed1 = False
printed2 = False
printed3 = False

os.system('cls')

while True:
	#os.system('cls')
	if(time.time() < endTime1):
		if(printed1 == False):
			os.system('cls')
			print(string1)
			printed1 = True
	elif(time.time() < endTime2):
		if(printed2 == False):
			os.system('cls')
			print(string2)
			printed2 = True
	elif(time.time() < endTime3):
		if(printed3 == False):
			os.system('cls')
			print(string3)
			printed3 = True
	elif(time.time() > endTime3):
		break
main()
