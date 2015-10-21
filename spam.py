import time


def test(spamage):
    timeout = time.time() + 1*5   # 5 secs from now
    userInput = 0
    loopCounter = 1
    spamList = []
    survived = True

    while time.time() < timeout:
        userInput = input(str(loopCounter) + ") hit enter:")
        spamList.append(userInput)

        if time.time() > timeout:
            if(len(spamList) >= spamage):
                survived = True
            else:
                survived = False
            break
        loopCounter += 1

    return survived
