from items import *

room_cryo = {
    "name": "Cryo",

    "description":
    """Taking a look around the room you realise that it is mostly how you remember it. Cryo bays for 60\
    \n crew line the walls, all eerily empty. The fluorescent blue lights are mostly steady, and the terminal\
    \n is humming softly\n in the corner….not literally, its a metaphor.""",

    "exits": {"east": "Hallway1"},

    "items": []
}

room_life = {
    "name": "Life Support",

    "description":
    """The life support room has seen better days. Sparks fly from the system, revealing the walls in sad \
    \nflashes of light and leaving dark and shady corners throughout. You squint your eyes to see, a faint \
    \nmessage written on the wall “ + " FORGIVE ME… ” + " There is a distinct smell of bacon in the air. """,

    "exits": {"east": "Hallway22", "west": "Hallway1"},

    "items": []
}

room_engine = {
    "name": "Engine Room",

    "description":
    """The engines lay ominously silent for the first time Kirill could remember, the only noise being the\
    \n dismal creaking of the ship….. Should ships sound like that? You hear the loud sounds of snapping metal \
    \nin the distance, followed\n by what could only be described as the twanging of a giant rubber band....nope\
    \n....probably not.""",

    "exits": {"north": "Hallway1"},

    "items": [item_fuel]
}

room_maintenance = {
    "name": "Maintenance",

    "description":
    """description""",

    "exits": {"east": "Hallway20", "west": "Hallway3"},

    "items": [item_screwdriver]
}

room_escape = {
    "name": "Escape Pod",

    "description":
    """Tens of corpses scattered across the floor in various states and…...pieces. It reminds you of rugby.\
    \n  The crew must have ran here once they knew Wales had lost as all but one of the escape pods were gone, \
    \n clearly not everyone made it. """,

    "exits": {"south": "Hallway9"},

    "items": []
}

room_bridge = {
    "name": "Bridge",

    "description":
    """The massive windows of the bridge are the first things that greet you, but they are not as they once were.\
    \nLarge cracks run through them, and you start to feel lightheaded as you notice the hissing of oxygen leaving\
    \nthe room. Blood has pooled around the Captain’s chair in the centre of the room and you feel relieved when\
    \nthere isnt a body sa- oh wait nope, thats definitely a severed hand right there.""",

    "exits": {"south": "Hallway13"},

    "items": []
}

room_cafeteria = {
    "name": "Cafeteria",

    "description":
    """description""",

    "exits": {"east": "Kitchen", "south": "Hallway15"},

    "items": []
}

room_control = {
    "name": "Control",

    "description":
    """description""",

    "exits": {"north": "stairdown", "south": "Hallway3"},

    "items": []
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """Multiple stoves and ovens line one side of the room, with various kitchen tools and utensils scattered\
    \n throughout. As you look around you start to remember you used to have a thing for the old cafeteria lady, \
    \nDorothy. She was sexy as can be, legs as long as a runway, curves that would make an hour glass jealous. \
    \nYou have many fond memories of this place and\n feel a deep warmth grow from within. You regret the mistakes\
    \nthat have led to this day, the life you could have had…..Was it hot in here? """,

    "exits": {"south": "Hallway16", "west": "Cafeteria"},

    "items": [item_knife]
}

room_relay = {
    "name": "Relay Room",

    "description":
    """description""",

    "exits": {"east": "Hallway23", "south": "Cupboard7"},

    "items": []
}

room_research = {
    "name": "Research Lab",

    "description":
    """Strange plants and creatures are scattered in glass containers throughout the room, you are acutely aware\
    \nthat some of the containers lie broken and empty........ Looking around more you start to fully realise the \
    \nextent of the mess; pages of notes, chemicals, and lab equipment mix with the blood and the bodies of the main\
    \nresearch team. Only one terminal is still in working order, the others having been seemingly smashed apart in \
    \nthe struggle.""",

    "exits": {"east": "Hallway27", "west": "Hallway26"},

    "items": []
}

room_server = {
    "name": "Server Room",

    "description":
    """description""",

    "exits": {"west": "Hallway30", "south": "Cupboard8"},

    "items": []
}

#Hallways
room_hallway1 = {
    "name": "Hallway",

    "description":
    """The hallway shows signs of a recent struggle, with bullet holes and blood marking the now-dirty walls.\
    \n  To the west is life support, the south holds the engine room, to the west is the cryo chamber, and to\
    \nthe north lies the rest of the ship.""",

    "exits": {"north": "Hallway3", "east": "Life", "south": "Engine", "west": "Cryo"},

    "items": [] 
}

room_hallway3 = {
    "name": "Hallway",

    "description":
    """The hallway lights flicker irregularly, lighting up things best left unseen. The control room is to the \
    \nnorth, east is the maintenance room, to the west you see a long hallway leading deep into the ship, and to\
    \nthe south is the cryo room amoungst other things.""",

    "exits": {"north": "Control", "east": "Maintenance", "south": "Hallway1", "west": "Hallway4"},

    "items": []
}

room_hallway4 = {
    "name": "Hallway",

    "description":
    """Grim shadows play across the wall, with the hallway extending from west to east. You see the doors of a\
    \ncupboard to the north""",

    "exits": {"north": "Cupboard1", "east": "Hallway3", "west": "Hallway5"},

    "items": []
}

room_hallway5 = {
    "name": "Hallway",

    "description":
    """You see a curve in the hallway to the west, to the south is a cupboard in the east yo ucan distantly see the\
    \ndoors of the maintenance room. """,

    "exits": {"east": "Hallway4", "south": "Cupboard2", "west": "Hallway6"},

    "items": []
}

room_hallway6 = {
    "name": "Hallway",

    "description":
    """You have reached the south-western corner of the ships hallways. There appears to be the remains of a brief barricade \
    \nscattered around the floor mixed with the bodies of various crew-members, clearly it wasnt enough.""",

    "exits": {"north": "Hallway8", "east": "Hallway5"},

    "items": []
}

room_hallway8 = {
    "name": "Hallway",

    "description":
    """Eerie noises echo throughout the ship.......You see the doors of the escape pod at the northern end of the corridor!\
    \nTo the west are the doors of yet another cupboard, the hallway curves away in the south.""",

    "exits": {"north": "Hallway9", "south": "Hallway6", "west": "Cupboard6"},

    "items": []
}

room_hallway9 = {
    "name": "Hallway",

    "description":
    """The escape-pod room lies directly infront of you, and the hallway extends far both to the east and south. \
    \n You remember the kitchen and stairs to the upper deck were definately to the east somewhere....""",

    "exits": {"north": "Escape", "east": "Hallway10", "south": "Hallway8"},

    "items": []
}

room_hallway10 = {
    "name": "Hallway",

    "description":
    """The hallway continues on into the distance to the east, a corner lies to the west...""",

    "exits": {"east": "Hallway12", "west": "Hallway9"},

    "items": []
}

room_hallway12 = {
    "name": "Hallway",

    "description":
    """The crossroads of the space stations hallway network; the once fine central location now gives off the aura\
    \nof a massacre, with not a single alien body to be seen amoungst the many dead....half of the station\
    \nmust have died here! To the south you see the stairwell ascending upwards, and to the east you see the doors \
    \nof the stations bridge. The hallway extends in each direction.""",

    "exits": {"north": "Hallway13", "east": "Hallway14", "south": "stairdown", "west": "Hallway10"},

    "items": []
}

room_hallway13 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Bridge", "south": "Hallway12"},

    "items": []
}

room_hallway14 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"east": "Hallway15", "south": "Cupboard3", "west": "Hallway12"},

    "items": []
}

room_hallway15 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Cafeteria", "east": "Hallway16", "west": "Hallway14"},

    "items": []
}

room_hallway16 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Kitchen", "south": "Hallway18", "west": "Hallway15"},

    "items": []
}

room_hallway18 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Hallway16", "east": "Cupboard4", "south": "Hallway20"},

    "items": []
}

room_hallway20 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Hallway18", "south": "Hallway22", "west": "Maintenance"},

    "items": []
}

room_hallway22 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Hallway20", "east": "Cupboard5", "west": "Life"},

    "items": []
}

room_hallway23 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"east": "Hallway24", "west": "Relay"},

    "items": []
}

room_hallway24 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Hallway26", "east": "stairup", "west": "Hallway23"},

    "items": []
}

room_hallway26 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"east": "Research", "south": "Hallway24"},

    "items": []
}

room_hallway27 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"south": "Hallway29", "west": "Research"},

    "items": []
}

room_hallway29 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Hallway27", "east": "Hallway30", "west": "stairup"},

    "items": []
}

room_hallway30 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"east": "Server", "west": "Hallway29"},

    "items": []
}

#cupboards

room_cupboard1 = {
    "name": "Cupboard",

    "description":
    """A hiding place""",

    "exits": {"south": "Hallway4"},

    "items": []
}

room_cupboard2 = {
    "name": "Cupboard",

    "description":
    """A hiding place""",

    "exits": {"north": "Hallway5"},

    "items": []
}

room_cupboard3 = {
    "name": "Cupboard",

    "description":
    """A hiding place""",

    "exits": {"north": "Hallway14"},

    "items": []
}

room_cupboard4 = {
    "name": "Cupboard",

    "description":
    """A hiding place""",

    "exits": {"west": "Hallway18"},

    "items": []
}

room_cupboard5 = {
    "name": "Cupboard",

    "description":
    """A hiding place""",

    "exits": {"west": "Hallway22"},

    "items": []
}

room_cupboard6 = {
    "name": "Cupboard",

    "description":
    """A hiding place""",

    "exits": {"east": "Hallway8"},

    "items": []
}

room_cupboard7 = {
    "name": "Cupboard",

    "description":
    """A hiding place""",

    "exits": {"north": "Relay"},

    "items": []
}

room_cupboard8 = {
    "name": "Cupboard",

    "description":
    """A hiding place""",

    "exits": {"north": "Server"},

    "items": []
}

room_stairsDown = {
    "name": "lower Stairwell",

    "description":
    """you can go up the stairs""",

    "exits": {"up": "stairup", "north": "Hallway12", "south": "Control"},

    "items": []
}

room_stairsUp = {
    "name": "upper Stairwell",

    "description":
    """you can go down the stairs""",

    "exits": {"down": "stairdown", "east": "Hallway29", "west": "Hallway24"},

    "items": []
}

rooms = {
    "Cryo": room_cryo,
    "Life": room_life,
    "Engine": room_engine,
    "Maintenance": room_maintenance,
    "Control": room_control,
    "Escape": room_escape,
    "Bridge": room_bridge,
    "Cafeteria": room_cafeteria,
    "Kitchen": room_kitchen,
    "Relay": room_relay,
    "Research": room_research,
    "Server": room_server,

    "Hallway1": room_hallway1,
    "Hallway3": room_hallway3,
    "Hallway4": room_hallway4,
    "Hallway5": room_hallway5,
    "Hallway6": room_hallway6,
    "Hallway8": room_hallway8,
    "Hallway9": room_hallway9,
    "Hallway10": room_hallway10,
    "Hallway12": room_hallway12,
    "Hallway13": room_hallway13,
    "Hallway14": room_hallway14,
    "Hallway15": room_hallway15,
    "Hallway16": room_hallway16,
    "Hallway18": room_hallway18,
    "Hallway20": room_hallway20,
    "Hallway22": room_hallway22,
    "Hallway23": room_hallway23,
    "Hallway24": room_hallway24,
    "Hallway26": room_hallway26,
    "Hallway27": room_hallway27,
    "Hallway29": room_hallway29,
    "Hallway30": room_hallway30,

    "Cupboard1": room_cupboard1,
    "Cupboard2": room_cupboard2,
    "Cupboard3": room_cupboard3,
    "Cupboard4": room_cupboard4,
    "Cupboard5": room_cupboard5,
    "Cupboard6": room_cupboard6,
    "Cupboard7": room_cupboard7,
    "Cupboard8": room_cupboard8,

    "stairup": room_stairsUp,
    "stairdown": room_stairsDown,
}
