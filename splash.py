""" splash screen """

import os
import time
from game import *

string1 = "\n\n\t\t\t     The year is 2231"
string1 += "\n\n\tSpace travel has advanced sufficiently for corporations"
string1 += "\n\tand governments to begin setting up colonies on planets"
string1 += "\n\t\t     further than our own solar system."

string1 += "\n\n\tYou are Kirill, a rogue programmer who has been contracted"
string1 += "\n\tby a corporation to ensure the failure of the government"
string1 += "\n\t\t     research vessel \"LWSS Pleiades\"."

#new screen

string2 = "\n\n\tYour contractors never informed you what the Pleiades'"
string2 += "\n\tmission was but they explicitly stated that it had to"
string2 += "\n\t\tfail its mission by any means necessary."

string2 += "\n\n\tYou assume the identity of one of the members of the ship"
string2 += "\n\tand board it with the other members heading straight into"
string2 += "\n\t\tthe cryo chamber to be placed into statis."

string2 += "\n\n\tYou place your clothes into one of the lockers along with"
string2 += "\n\t\tyour ID card and prepare to be placed into"
string2 += "\n\t\t\t\tstatis."

#new screen

string3 = "\n\n\tJust before you are placed into statis, the captain forces"
string3 += "\n\tall of you to watch an educational video that teaches you"
string3 += "\n\t\twhat to do in the event of an emergency."

string3 += "\n\n\tThe video is dull and boring to watch, but one piece"
string3 += "\n\t\tof information is engarved into your mind"

string3 += "\n\n\t    \"Never go into space without a distress beacon.\""

#new screen

string4 = "\n\n\n\n\t\tYou step into your cryochamber, expecting to be woken"
string4 += "\n\t\t     up once your ship has reached its destination."

#new screen

string5 = "\n\n\t\tYou wake up from cryo, dazed, cold and alone."
string5 += "\n\tAs the door opens you fall to the floor onto the metal grating."

string5 += "\n\n\tYou call out for help as you lay on the floor thawing from"
string5 += "\n\t\tcryo, hear nothing but the hum of the engines."

string5 += "\n\n\tAfter a while you realise that noone is coming to help you."
string5 += "\n\tYou slowly lift yourself up, staggering around as you haven't"
string5 += "\n\t\tmoved for at least a couple of months."

#new screen

string6 = "\n\n\tThere is a terminal in cryo that is flashing red and white,"
string6 += "\n\tit's obvious that it's trying to get someones attention."

string6 += "\n\n\tThe termial informs you that the oxygen levels are running"
string6 += "\n\tlow and you have about 15 minutes remaining before it runs"
string6 += "\n\t\t\t\t    out!"

string6 += "\n\n\tYou quickly set your watch to count down from this time to keep"
string6 += "\n\t\t     track of how long you have to escape."

string7 = "\n\n\tThis game features two new features which you may not have used"
string7 += "\n\t\t\t\t   before."
string7 += "\n\n\t\t\"check\": checks an adjacent room for a threat"
string7 += "\n\n\t\t\"hide\": hide from threats in cupboards"

endTime1 = time.time() + 1*12
endTime2 = time.time() + 1*26
endTime3 = time.time() + 1*37
endTime4 = time.time() + 1*46
endTime5 = time.time() + 1*58
endTime6 = time.time() + 1*67
endTime7 = time.time() + 1*77

printed1 = False
printed2 = False
printed3 = False
printed4 = False
printed5 = False
printed6 = False
printed7 = False

while True:
	#os.system('cls')
	if(time.time() < endTime1):
		if(printed1 is False):
			os.system('cls')
			print(string1)
			printed1 = True
	elif(time.time() < endTime2):
		if(printed2 is False):
			os.system('cls')
			print(string2)
			printed2 = True
	elif(time.time() < endTime3):
		if(printed3 is False):
			os.system('cls')
			print(string3)
			printed3 = True
	elif(time.time() < endTime4):
		if(printed4 is False):
			os.system('cls')
			print(string4)
			printed4 = True
	elif(time.time() < endTime5):
		if(printed5 is False):
			os.system('cls')
			print(string5)
			printed5 = True
	elif(time.time() < endTime6):
		if(printed6 is False):
			os.system('cls')
			print(string6)
			printed6 = True
	elif(time.time() < endTime7):
		if(printed7 is False):
			os.system('cls')
			print(string7)
			printed7 = True
	elif(time.time() > endTime7):
		break
# Start Oxygen Tank countdown
TimerWidget()

# Start Main
main()
