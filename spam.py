import time


def test(spamage):
    timeout = time.time() + 1*5   # 5 secs from now
    userInput = 0
    test =1
    loopCounter = 1

    spamList = []
    survived = True

    while time.time() < timeout:
        
        userInput = input(str(loopCounter) + ") spam:")
        spamList.append(userInput)

        if time.time() > timeout:
            if(len(spamList) >= spamage):
                survived = True
                print("you managed to survive!")
            else:
               	survived = False

            break
        loopCounter += 1 

    return survived    
    
