from items import *
from map import rooms

#turn system
endturn = 0

# Start aliens at cryo
alien1_current_room = rooms["Hallway9"]
alien2_current_room = rooms["Kitchen"]
alien3_current_room = rooms["stairdown"]

alien1_alive = True
alien2_alive = True
alien3_alive = True

alien1_injuries = 0
alien2_injuries = 0
alien3_injuries = 0
#will insert in lists/dictionaries
