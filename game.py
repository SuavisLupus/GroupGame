#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
from aliens import *
from random import *
from timer import *
from spam import *
import time


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    outString = ""
    count = 1
    for stuff in items:
        if(count == 1):
            outString += stuff["name"]
        elif(count > 1):
            outString += (", " + stuff["name"])
        count += 1
    
    return(outString)        
    pass


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    prntRmItems = ""
    prntRmItems = list_of_items(room["items"])
    if(len(prntRmItems) >= 1):
        print("There is " + prntRmItems + " here.\n")
    pass


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    prntInvt = ""
    prntInvt = list_of_items(items)
    if(len(prntInvt) >= 1):
        print("You have " + prntInvt + ".\n")

    pass


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    wire = False
    emmiter = False
    amplifier = False

    cable = False
    beacon = False
    oxygen = False
    fuel = False        

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for rmItems in room_items:
        if rmItems["weight"] != "5.1":
            print("TAKE " + rmItems["id"].upper() + " to take " + rmItems["name"] + "." )    
    for loot in inv_items:
        print("DROP " + loot["id"].upper() + " to drop " + loot["name"] + ".")
    print("INSPECT to inspect any item in the room or in inventory")
    for items in inv_items:
        if items["id"] == "wire":
            wire = True
        if items["id"] == "emmiter":
            emmiter = True
        if items ["id"] == "amplifier":
            amplifier = True
    if wire == True and emmiter == True and amplifier == True:
        print("CRAFT to craft a distress beacon")

    fuel = False
    oxygen = False
    cable = False
    distress = False
    for items in rooms["Escape"]["items"]:
        if items["id"] == "fuel":
            fuel = True
        if items["id"] == "filter":
            oxygen = True
        if items["id"] == "cable":
            cable = True
        if items["id"] == "beacon":
            distress = True

    if rooms["Life"]["description"] == "The life support room has seen better days. Sparks fly from the system, revealing the walls in sad \nflashes of light and leaving dark and shady corners throughout. You squint your eyes to see, a faint message written on the\nwall FORGIVE ME... The anti-fire system is running efficiently, \nnow it will douse any fire with a ship wide monsoon" and current_room == rooms["Kitchen"]:
        print("BURN CLOTHES to start a fire!")

    if cable == True and oxygen == True and fuel == True:
        print("go to the escape pod and enter the airlock code to escape...")


    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    global endturn
    exits=current_room["exits"]

    if(is_valid_exit(exits,direction)):
        current_room = move(exits,direction)
    else:
        print("You cannot go there.")

    endturn = endturn + 2

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    global inventory
    global endturn
    itmExists = False

    for junk in current_room["items"]:
        if(junk["id"] == item_id):
            itmExists = True
            if(isAvailCarry(item_id) == True):
                inventory.append(junk)
                current_room["items"].remove(junk)
                print(junk["name"] + " has been added to inventory.")
            else:
                print("\nBag is too heavy to carry " + junk["name"] +
                " \ntry dropping something from inventory")
            
        else:
            itmExists = False  

    
    if(itmExists == False):
        print("You cannot take that.")    

    endturn = endturn + 1
    
def exectue_inspect(item_id):
    """this function takes an item_id and  prints the item descriptioin so the player can get a better understanding 
    of the world they are in
    """
    for item in current_room["items"]:
        if item["id"] == item_id:
            print(item["description"])
    for item in inventory:
        if item["id"] == item_id:
            print(item["description"])
    return

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    global inventory
    global endturn
    invtExists = False

    for loot in inventory:
        if(loot["id"] == item_id):
            invtExists = True
            current_room["items"].append(loot)
            inventory.remove(loot)   

        

    if(invtExists == False):
        print("You cannot drop that.")        
    endturn = endturn + 1

def execute_check(direction):
    """
    this alows the player to check nearby rooms for alien activity before walking
    right into them
    """
    global current_room
    exits=current_room["exits"]

    if(is_valid_exit(exits,direction)):
        if alien1_current_room == move(exits,direction) and alien1_alive == True:
            print("alien is present")
        elif alien2_current_room == move(exits,direction) and alien2_alive == True:
            print("alien is present")
        elif alien3_current_room == move(exits,direction) and alien3_alive == True:
            print("alien is present")
        else:
            print("no alien")
    else:
        print("You cannot go there.")
    
def isAvailCarry(item_id):
    """this function checks weather the players total inventory weight exceeds a set limit
    if it does then the function returns false which in turn causes the player to be unable 
    to pick up more items.
    """
    global inventory
    totalWeight = 0.0
    itmWeight = 0.0

    for loot in inventory:
        totalWeight += float(loot["weight"])

    for stuff in current_room["items"]:
        if(stuff["id"] == item_id):
            itmWeight = stuff["weight"]    

    if(totalWeight + float(itmWeight)) < 5:
        return True
    else:
        return False      

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    global alien1_alive
    global alien1_current_room
    global alien2_alive
    global alien2_current_room
    global alien3_alive
    global alien3_current_room
    global player_alive

    if 0 == len(command):
        return

    if command[0] == "go" or command[0] == "walk" or command[0] == "run" or command[0] == "stroll" or command[0] == "hike" or command[0] == "parade" or command[0] == "pace" or command[0] == "march":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take" or command[0] == "pick up":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop" or command[0] == "ditch" or command[0] == "let go" or command[0] == "discard" or command[0] == "leave":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
    elif command[0] == "check" or command[0] == "look" or command[0] == "peek" or command[0] == "glimpse" or command[0] == "view" or command[0] == "listen":
        if len(command) > 1:
            execute_check(command[1])
        else:
            print("check where?")

    elif command[0] == "hide":
        print("laying low...")
        if alien1_alive == True:
            alien1_current_room = alien_move(alien1_current_room)
        if alien2_alive == True:
            alien2_current_room = alien_move(alien2_current_room)
        if alien3_alive == True:
            alien3_current_room = alien_move(alien3_current_room)
        endturn = 0

    elif command[0] == "craft":
        wire = False
        emmiter = False
        amplifer = False
        for items in inventory:
            if items["id"] == "wire":
                wire = True
            if items["id"] == "emmiter":
                emmiter = True
            if items ["id"] == "amplifier":
                amplifier = True
        if wire == True and emmiter == True and amplifier == True:
            inventory.append(item_distress_beacon)
            inventory.remove(item_wire)
            inventory.remove(item_IR_emmiter)
            inventory.remove(item_amplifier)

    elif command[0] == "inspect":
        if len(command) > 1:
            exectue_inspect(command[1])
        else:
            print("inspect what?")
    else:
        print("This makes no sense.")


def encounter(alien_injuries):
    """this function is called when a player and an alien are in the same room
    it gives the player the option to run away(hit enter repeatedly to eascape the alien)
    or the option to fight the alien by typing quickly the commands in CAPS.
    """
    global current_room
    global player_alive

    exits = current_room["exits"]

    while True:

        print("you can RUN or ATTACK")
        command = input("your deccision?: ")
        command = normalise_input(command)

        if 0 == len(command):
            encounter(alien_injuries)

        if command[0] == "run":
            print("press enter to run!!")

            if test(randrange(1, 30)) is True:

                if(is_valid_exit(exits, "north")):
                    current_room = rooms[exits["north"]]
                    return alien_injuries
                elif(is_valid_exit(exits, "east")):
                    current_room = rooms[exits["east"]]
                    return alien_injuries
                elif(is_valid_exit(exits, "south")):
                    current_room = rooms[exits["south"]]
                    return alien_injuries
                elif(is_valid_exit(exits, "west")):
                    current_room = rooms[exits["west"]]
                    return alien_injuries

        if command[0] == "attack":
            print("attack")
            Won = True
            timeout = time.time() + 1*6
            difficulty = randrange(3, 7, 1)
            weapon = 0
            mistakes = 0
            for items in inventory:
                if items["id"] == "screwdriver" and weapon != 2:
                    difficulty = randrange(2, 6, 1)
                    weapon = 1
                if items["id"] == "knife":
                    difficulty = randrange(1, 5, 1)
                    weapon = 2
                    print("knife")

            if weapon == 0:
                if difficulty >= 1:
                    attack = input("PUNCH the alien!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "punch" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 2:
                    attack = input("KICK the alien!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "kick" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 3:
                    attack = input("STAND up!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "stand" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 4:
                    attack = input("SHOVE the alien away!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "shove" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 5:
                    attack = input("CHARGE the alien: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "charge" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 6:
                    attack = input("KICK the alien!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "kick" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1

            if weapon == 1:
                if difficulty >= 1:
                    attack = input("PUNCH the alien!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "punch" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 2:
                    attack = input("KICK the alien!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "kick" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 3:
                    attack = input("STAB the alien!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "stand" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 4:
                    attack = input("SHOVE the alien away!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "shove" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 5:
                    attack = input("CHARGE the alien: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "charge" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1

            if weapon == 2:
                if difficulty >= 1:
                    attack = input("CUT the alien!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "cut" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 2:
                    attack = input("KICK the alien!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "kick" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 3:
                    attack = input("STAB the alien!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "stand" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                if difficulty >= 4:
                    attack = input("SLASH the alien!: ")
                    if 0 == len(normalise_input(attack)):
                        mistakes = mistakes + 1
                    elif "slash" != normalise_input(attack)[0]:
                        mistakes = mistakes + 1
                intelect = 0
            if time.time() < timeout and mistakes <= 2:
                won = True
                print("you beat the alien back and managed to run to the next room...")
                
            else:
                Won = False

            if Won is True:
                alien_injuries = alien_injuries + 1
                if(is_valid_exit(exits, "north")):
                    current_room = rooms[exits["north"]]
                    return alien_injuries
                elif(is_valid_exit(exits, "east")):
                    current_room = rooms[exits["east"]]
                    return alien_injuries
                elif(is_valid_exit(exits, "south")):
                    current_room = rooms[exits["south"]]
                    return alien_injuries
                elif(is_valid_exit(exits, "west")):
                    current_room = rooms[exits["west"]]
                    return alien_injuries
            elif randrange(1, 101) >= 70:

                print("you distract it long enough to escape")

                if(is_valid_exit(exits, "north")):
                    current_room = rooms[exits["north"]]
                    return alien_injuries
                elif(is_valid_exit(exits, "east")):
                    current_room = rooms[exits["east"]]
                    return alien_injuries
                elif(is_valid_exit(exits, "south")):
                    current_room = rooms[exits["south"]]
                    return alien_injuries
                elif(is_valid_exit(exits, "west")):
                    current_room = rooms[exits["west"]]
                    return alien_injuries
            else:
                print("you fail to kill the alien and it devours you...")
                player_alive = False
                death(player_alive)


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """
    global alien1_alive
    global alien2_alive
    global alien3_alive
    global alien1_injuries
    global alien2_injuries
    global alien3_injuries
    global endturn

    # Check for alien presense
    if alien1_current_room == current_room:
        if alien1_alive is True:
            print("an alien spots you, what do you do?...")
            alien1_injuries = encounter(alien1_injuries)
            endturn = endturn + 2
            if alien1_injuries >= 4:
                alien1_alive = False
            return ""
        elif alien1_alive == False:
            print("Alien 1 is dead...")

    if alien2_current_room == current_room:
        if alien2_alive == True:
            print("an alien spots you, what do you do?...")
            alien2_injuries = encounter(alien2_injuries)
            endturn = endturn + 2
            if alien2_injuries >= 4:
                alien2_alive = False
            return ""
        elif alien2_alive == False:
            print("Alien 2 is dead...")

    if alien3_current_room == current_room:
        if alien3_alive == True:
            print("an alien spots you, what do you do?...")
            alien3_injuries = encounter(alien3_injuries)
            endturn = endturn + 2
            if alien3_injuries >= 4:
                alien3_alive = False
            return ""
        elif alien3_alive == False:
            print("Alien 3 is dead...")
        
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]

def alien_move(alien_current_room):
    """this function makes the aliens move randomly in any possible direction and if
    the player is holding a screwdriver they will jump on the player when they move
    into and adjecant room
    """
    number = randrange(1, 5, 1)
    intelect = 0
    global current_room
    exits = alien_current_room["exits"]

    

    if intelect == 0:
        if number == 1:
            direction = "north"
        elif number == 2:
            direction = "east"
        elif number == 3:
            direction = "south"
        elif number == 4:
            direction = "west"
        

        if current_room == rooms["stairdown"] and number == 4:
            direction = "up"
        if current_room == rooms["stairdown"] and number == 1:
            direction = "down"

        if(is_valid_exit(exits,direction)) and move(exits,direction)["name"] != "Cupboard":
            return rooms[exits[direction]]
        else:
            return alien_current_room  



    if intelect == 1:
        if(is_valid_exit(exits,"north")) and move(exits,"north")["name"] != "Cupboard":
            if current_room == move(exits,"north"):
                return rooms[exits["north"]]
        elif(is_valid_exit(exits,"east")) and move(exits,"east")["name"] != "Cupboard":
            if current_room == move(exits,"east"):
                return rooms[exits["east"]]
        elif(is_valid_exit(exits,"south")) and move(exits,"south")["name"] != "Cupboard":
            if current_room == move(exits,"south"):
                return rooms[exits["south"]]
        elif(is_valid_exit(exits,"west")) and move(exits,"west")["name"] != "Cupboard":
            if current_room == move(exits,"west"):
                return rooms[exits["west"]]
        
        number = randrange(1, 5, 1)
        if number == 1:
            direction = "north"
        elif number == 2:
            direction = "east"
        elif number == 3:
            direction = "south"
        elif number == 4:
            direction = "west"
        exits = alien_current_room["exits"]

        if current_room == rooms["stairdown"] and number == 4:
            direction = "up"
        if current_room == rooms["stairdown"] and number == 1:
            direction = "down"

        for items in inventory:
            if items["id"] == "screwdriver":
                if intelect != 1:
                    intelect = 1
        if(is_valid_exit(exits,direction)) and move(exits,direction)["name"] != "Cupboard":
            return rooms[exits[direction]]
        else:
            return alien_current_room

def death(player_alive):
    """this function ends the game upon failure
    """
    if player_alive == False:
        print('You have died.\n\nGame Over.')
        time.sleep(2)
        quit()
    else:
        pass

def check_win(current_room):
    """this function checks the two vitocry rooms and weather they have met
    the right conditioins to put them in a state where a command can be issued
    to win the game(or throw yourself out to starve in space)
    """
    global player_alive
    global Water_fixed
    fuel = False
    oxygen = False
    cable = False
    distress = False
    screwdriver = False

    pipe = False
    wrench = False
    wire = False
    clothes = False

    global alien1_alive
    global alien2_alive
    global alien3_alive

    for items in inventory:
        if items["id"] == "wrench":
            wrench = True
        if items["id"] == "screwdriver":
            screwdriver = True
        if items["id"] == "clothes":
            clothes = True

    for items in rooms["Escape"]["items"]:
        if items["id"] == "fuel":
            fuel = True
        if items["id"] == "filter":
            oxygen = True
        if items["id"] == "cable":
            cable = True
        if items["id"] == "beacon":
            distress = True

    for items in rooms["Life"]["items"]:
        if items["id"] == "pipe":
            pipe = True
        if items["id"] == "wire":
            wire = True

    if pipe == True and wire == True and wrench == True and current_room == rooms["Life"]:
        Water_fixed = True
        rooms["Life"]["items"].remove(item_pipe)
        rooms["Life"]["items"].remove(item_wire)
        print("you use the wrench and the pipe to fix the broken anti-fire system and \nuse the wire to repair the circuit boards")
        rooms["Life"]["description"] = "The life support room has seen better days. Sparks fly from the system, revealing the walls in sad \nflashes of light and leaving dark and shady corners throughout. You squint your eyes to see, \na faint message written on the wall FORGIVE ME... The anti-fire system is running efficiently, \nnow it will douse any fire with a ship wide monsoon"
        print("now just to start the fire...")


    if rooms["Life"]["description"] == "The life support room has seen better days. Sparks fly from the system, revealing the walls in sad \nflashes of light and leaving dark and shady corners throughout. You squint your eyes to see, a faint message written on the\nwall FORGIVE ME... The anti-fire system is running efficiently, \nnow it will douse any fire with a ship wide monsoon" and current_room == rooms["Kitchen"]:
        command = menu(current_room["exits"], current_room["items"], inventory)

        if 0 == len(command):
            return

        if command[0] == "burn":
            if len(command) > 1:
                if command [1] == "clothes":
                    print("you place your clothes on the hob and watch them ignite...")
                    print("the smoke causes the alarm to go off and the sprinklers rain down hard.")
                    print("you hear distant distorted screams...")
                    alien1_alive = False
                    alien2_alive = False
                    alien3_alive = False
        else:
            execute_command(command)

    if fuel == True and oxygen == True and cable == True and screwdriver == True and current_room == rooms["Escape"]:
        command = menu(current_room["exits"], current_room["items"], inventory)

        if 0 == len(command):
            return

        if command[0] == "879834":
            print("you jetison out into the cold of space...")
            if distress == True:
                print("your fixed distress beacon fires up and sends out a strong signal \n and soon enough galactic rescue pick you up... \n CONGRATULATIONS YOU WIN!!!")
                return True
            else: 
                print("without any form of comunication you slowly starve to death...")
                player_alive = False
                return False
        else:
            execute_command(command)

    if alien1_alive == False:
        if alien2_alive == False:
            if alien3_alive == False:
                print("you finally managed to kill all of the aliens on board, you now await rescue...")
                print("\n CONGRATULATIONS YOU WIN!!!")
                return True
    return False

# This is the entry point of our program
def main():
    Water_fixed = False
    global endturn
    global alien1_current_room
    global alien2_current_room
    global alien3_current_room
    win = False

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        

        print_room(current_room)
        print_inventory_items(inventory)
        win = check_win(current_room)

        if win == True:
            break
        if player_alive == False:
            break
        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)
        
        if alien1_current_room != current_room and alien2_current_room != current_room and alien3_current_room != current_room:
            if endturn >= 2:
                if alien1_alive == True:
                    alien1_current_room = alien_move(alien1_current_room)
                if alien2_alive == True:
                    alien2_current_room = alien_move(alien2_current_room)
                if alien3_alive == True:
                    alien3_current_room = alien_move(alien3_current_room)
                endturn = 0
        else:
            endturn = 0
        

        

        

        

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    p = TimerWidget()
    while main():
        p
