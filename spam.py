import time

timeout = time.time() + 1*5   # 5 secs from now
userInput = 0
test =1
loopCounter = 1

spamList = []
survived = True
#def test:
print("you have been GRABBED by an ALIEN!!!!!!!\n press enter repeatedly as quickly as you can, to struggle free")
while time.time() < timeout:
    
    userInput = input(str(loopCounter) + ") spam:")
    spamList.append(userInput)

    if time.time() > timeout:

        #print(spamList)
        #print(len(spamList))
        if(len(spamList) >= 30):
        	survived = True
        	#print("You have managed to struggle free")
         	
        else:
           	#print("YOU have been EATEN by alien")
           	survived = False

        break
    loopCounter += 1 

if(survived):
	print("\n----SUCCESS----\nYou have managed to struggle free")
else:
	print("\nYOU FAILED to break free, YOU have been EATEN by the alien")	    
    #test = test + 1
    
