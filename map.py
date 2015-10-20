from items import *

room_cryo = {
    "name": "Cryo",

    "description":
    """This is where you slept while everyone on board was devoured.""",

    "exits": {"east": "Hallway1"},

    "items": []
}

room_life = {
    "name": "Life Support",

    "description":
    """description""",

    "exits": {"east": "Hallway22", "west": "Hallway1"},

    "items": []
}

room_engine = {
    "name": "Engine Room",

    "description":
    """description""",

    "exits": {"north": "Hallway1"},

    "items": []
}

room_maintenance = {
    "name": "Maintenance",

    "description":
    """description""",

    "exits": {"east": "Hallway20", "west": "Hallway3"},

    "items": []
}

room_escape = {
    "name": "Escape Pod",

    "description":
    """description""",

    "exits": {"south": "Hallway9"},

    "items": []
}

room_bridge = {
    "name": "Bridge",

    "description":
    """description""",

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
    """description""",

    "exits": {"south": "Hallway16", "west": "Cafeteria"},

    "items": []
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
    """description""",

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
    """A long bland hallway...""",

    "exits": {"north": "Hallway3", "east": "Life", "south": "Enigne", "west": "Cryo"},

    "items": [] 
}

room_hallway3 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Control", "east": "Maintenance", "south": "Hallway1", "west": "Hallway4"},

    "items": []
}

room_hallway4 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Cupboard1", "east": "Hallway3", "west": "Hallway5"},

    "items": []
}

room_hallway5 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"east": "Hallway4", "south": "Cupboard2", "west": "Hallway6"},

    "items": []
}

room_hallway6 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Hallway8", "east": "Hallway5"},

    "items": []
}

room_hallway8 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Hallway9", "south": "Hallway6", "west": "Cupboard6"},

    "items": []
}

room_hallway9 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"north": "Escape", "east": "Hallway10", "south": "Hallway8"},

    "items": []
}

room_hallway10 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

    "exits": {"east": "Hallway12", "west": "Hallway9"},

    "items": []
}

room_hallway12 = {
    "name": "Hallway",

    "description":
    """A long bland hallway...""",

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
    "Enigne": room_engine,
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
