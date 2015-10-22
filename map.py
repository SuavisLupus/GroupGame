from items import *

room_cryo = {
    "name": "Cryo",

    "description":
    """Taking a look around the room you realise that it is mostly how you remember it.\nCryo bays for 60 crew line the walls, all eerily empty. The fluorescent blue\nlights are mostly steady, and the terminal is humming softly in the\ncorner...not literally, its a metaphor.""",

    "exits": {"east": "Hallway1"},

    "items": [item_clothes]
}

room_life = {
    "name": "Life Support",

    "description":
    """The life support room has seen better days. Sparks fly from the system,\nrevealing the walls in sad flashes of light and leaving dark and shady corners\nthroughout. You squint your eyes to see, a faint message written on the wall\nFORGIVE ME..." There is a distinct smell of bacon in the air.\nyou note the anti-fire system is dammaged, it will need a new pipe and some\nwire to repair the circuit board and a wrench wouldnt hurt either... """,

    "exits": {"east": "Hallway22", "west": "Hallway1"},

    "items": [item_oxygen_filter]
}

room_engine = {
    "name": "Engine Room",

    "description":
    """The engines lay ominously silent for the first time you could remember,\nthe only noise being the dismal creaking of the ship....Should ships sound\nlike that? You hear the loud sounds of snapping metal in the distance,\nfollowed by what could only be described as the twanging of a giant \nrubber band....nope....probably not.""",

    "exits": {"north": "Hallway1"},

    "items": [item_fuel]
}

room_maintenance = {
    "name": "Maintenance",

    "description":
    """Tools and shelves line the walls of the maintenance room, you think to\nlook for something useful in here but wouldnt really know where to start...""",

    "exits": {"east": "Hallway20", "west": "Hallway3"},

    "items": [item_screwdriver, item_wrench]
}

room_escape = {
    "name": "Escape Pod",

    "description":
    """Tens of corpses scattered across the floor in various states and....pieces.\nclearly not everyone made it. the last escape pod is severly dammaged it will \nneed some cable, a new fuel tank and an oxygen filter before its going anywhere.""",

    "exits": {"south": "Hallway9"},

    "items": []
}

room_bridge = {
    "name": "Bridge",

    "description":
    """The massive windows of the bridge are the first things that greet you, but \nthey are not as they once were. Large cracks run through them, and you start \nto feel lightheaded as you notice the hissing of oxygen leaving the room.\nBlood has pooled around the Captain’s chair in the centre of the room and \nyou feel relieved when there isnt a body sa- oh wait nope, thats definitely \na severed hand right there.""",

    "exits": {"south": "Hallway13"},

    "items": [item_lamp]
}

room_cafeteria = {
    "name": "Cafeteria",

    "description":
    """The cafeteria is a mess of scattered plates and food, it looks like it was \nthe lunch hour when all of this began.Judging from the state of some of the food \nyou gather that the attack had been more recent than you first thought, a few days\nat most.""",

    "exits": {"east": "Kitchen", "south": "Hallway15"},

    "items": [item_stool]
}

room_control = {
    "name": "Control",

    "description":
    """The control rooms massive machines are spaced evenly across the floor, it seems\nthat everyone managed to get out of here at least as there is next to no \ndamage. A streak of blood runs through the doorway as if left by a dragged and \nbleeding body...dead or alive you cannot tell.""",

    "exits": {"north": "stairdown", "south": "Hallway3"},

    "items": [item_IR_emmiter, item_code]
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """Multiple stoves and ovens line one side of the room, with various kitchen tools and\nutensils scattered throughout.""",

    "exits": {"south": "Hallway16", "west": "Cafeteria"},

    "items": [item_knife, item_oven]
}

room_relay = {
    "name": "Relay Room",

    "description":
    """Youd never been in the relay room before and are surprised at its small size. Static\nplays through the intercom infront of a slouched body, it looks like they tried calling\nfor help.....it didnt work.""",

    "exits": {"east": "Hallway23", "south": "Cupboard7"},

    "items": [item_wire, item_mouse]
}

room_research = {
    "name": "Research Lab",

    "description":
    """Strange plants and creatures are scattered in glass containers throughout the room,\nyou are acutely aware that some of the containers lie broken and empty...\nLooking around more you start to fully realise the extent of the mess; pages of notes,\nchemicals, and lab equipment mix with the blood and the bodies of the main research team.\nOnly one terminal is still in working order, the others having been seemingly smashed apart in\nthe struggle.""",

    "exits": {"east": "Hallway27", "west": "Hallway26"},

    "items": [item_amplifier, item_research_screen]
}

room_server = {
    "name": "Server Room",

    "description":
    """A few of the ships servers flicker with light while others lie dead, the ship must\nhave shut down the non-important ones to conserve power. At the same time you notice a\nfew have been destroyed entirely, with bodies lying partially inside them as if thrown\nat great force.""",

    "exits": {"west": "Hallway30", "south": "Cupboard8"},

    "items": [item_cable]
}

#Hallways
room_hallway1 = {
    "name": "Hallway",

    "description":
    """The hallway shows signs of a recent struggle, with bullet holes and blood \nmarking the now-dirty walls. To the west is life support, the south holds the\nengine room, to the west is the cryo chamber, and to the north lies the rest\n of the ship.""",

    "exits": {"north": "Hallway3", "east": "Life", "south": "Engine", "west": "Cryo"},

    "items": [] 
}

room_hallway3 = {
    "name": "Hallway",

    "description":
    """The hallway lights flicker irregularly, lighting up things best left \nunseen. The control room is to the north, east is the maintenance room, \nto the west you see a long hallway leading deep into the ship, and to the\nsouth is the cryo room amoungst\nother things.""",

    "exits": {"north": "Control", "east": "Maintenance", "south": "Hallway1", "west": "Hallway4"},

    "items": []
}

room_hallway4 = {
    "name": "Hallway",

    "description":
    """Grim shadows play across the wall, with the hallway extending from west\n to east. You see the doors of a cupboard to the north""",

    "exits": {"north": "Cupboard1", "east": "Hallway3", "west": "Hallway5"},

    "items": []
}

room_hallway5 = {
    "name": "Hallway",

    "description":
    """You see a curve in the hallway to the west, to the south is a cupboard\n in the east you can distantly see the doors of the maintenance room. """,

    "exits": {"east": "Hallway4", "south": "Cupboard2", "west": "Hallway6"},

    "items": []
}

room_hallway6 = {
    "name": "Hallway",

    "description":
    """You have reached the south-western corner of the ships hallways.\nThere appears to be the remains of a brief barricade nscattered around\nthe floor mixed with the bodies of various crew-members, clearly it\n wasnt enough.""",

    "exits": {"north": "Hallway8", "east": "Hallway5"},

    "items": []
}

room_hallway8 = {
    "name": "Hallway",

    "description":
    """Eerie noises echo throughout the ship.......You see the doors of\nthe escape pod at the northern end of the corridor! To the west are\nthe doors of yet another cupboard, the hallway curves away in the south.""",

    "exits": {"north": "Hallway9", "south": "Hallway6", "west": "Cupboard6"},

    "items": []
}

room_hallway9 = {
    "name": "Hallway",

    "description":
    """The escape-pod room lies directly infront of you, and the hallway\nextends far both to the east and south. You remember the kitchen and\nstairs to the upper deck were definately to the east somewhere....""",

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
    """The crossroads of the space stations hallway network; the once fine\ncentral location now gives off the aura of a massacre, with not a single\nalien body to be seen amoungst the many dead....half of the station must\nhave died here! To the south you see the stairwell ascending upwards, and\nto the east you see the doors of the stations bridge.The hallway extends\n in each direction.""",

    "exits": {"north": "Hallway13", "east": "Hallway14", "south": "stairdown", "west": "Hallway10"},

    "items": []
}

room_hallway13 = {
    "name": "Hallway",

    "description":
    """The door to the bridge is right infront of you.""",

    "exits": {"north": "Bridge", "south": "Hallway12"},

    "items": []
}

room_hallway14 = {
    "name": "Hallway",

    "description":
    """You nose twitches as you smell something other than the aroma of\ndeath on the ship...you must be nearing the cafeteria. A cupboard \nlies to the south.""",

    "exits": {"east": "Hallway15", "south": "Cupboard3", "west": "Hallway12"},

    "items": [item_pipe]
}

room_hallway15 = {
    "name": "Hallway",

    "description":
    """The big double doors of the cafeteria loom infront of you, partially\n wedged open by...is that a leg?""",

    "exits": {"north": "Cafeteria", "east": "Hallway16", "west": "Hallway14"},

    "items": [item_bucket]
}

room_hallway16 = {
    "name": "Hallway",

    "description":
    """You stand infront of the kitchen, to the south lies a hallway that you think may lead to the maintenance room.""",

    "exits": {"north": "Kitchen", "south": "Hallway18", "west": "Hallway15"},

    "items": []
}

room_hallway18 = {
    "name": "Hallway",

    "description":
    """Blood seeps through a hole in the ceiling, pooling on the floor below.\nTo the east you notice a cupboard door.""",

    "exits": {"north": "Hallway16", "east": "Cupboard4", "south": "Hallway20"},

    "items": [item_mop]
}

room_hallway20 = {
    "name": "Hallway",

    "description":
    """This part of the ship lies suspiciously quiet and empty, you hope \nit stays that way. The hallway continues north and southwards, with the\n maintenance room from before to the west.""",

    "exits": {"north": "Hallway18", "south": "Hallway22", "west": "Maintenance"},

    "items": []
}

room_hallway22 = {
    "name": "Hallway",

    "description":
    """The hallway suddenly ends, with tiny holes scattered throughout \nthe wall. You wonder what could have possibly made them......To the \nwest is the life support systems, the east holds a cupboard.""",

    "exits": {"north": "Hallway20", "east": "Cupboard5", "west": "Life"},

    "items": []
}

room_hallway23 = {
    "name": "Hallway",

    "description":
    """You hear a noise and turn around suddenly....the hallway lies \nempty. To your west is the relay room, the hallway extends to the east.""",

    "exits": {"east": "Hallway24", "west": "Relay"},

    "items": []
}

room_hallway24 = {
    "name": "Hallway",

    "description":
    """The upstairs of the ship is in exactly the same state as below. \nIt looks like a lot of the crew became trapped up here after the \ninitial struggle. To the east lies the stairwell.""",

    "exits": {"north": "Hallway26", "east": "stairup", "west": "Hallway23"},

    "items": []
}

room_hallway26 = {
    "name": "Hallway",

    "description":
    """The research rooms doors lie broken and warped in the centre\n of the hallway, what happened here? .""",

    "exits": {"east": "Research", "south": "Hallway24"},

    "items": []
}

room_hallway27 = {
    "name": "Hallway",

    "description":
    """The shattered glass windows of the research room gives hints\n at the mess within.""",

    "exits": {"south": "Hallway29", "west": "Research"},

    "items": [item_coin]
}

room_hallway29 = {
    "name": "Hallway",

    "description":
    """The shattered lights above do nothing to illuminate the\nhallway, you are unsure if you prefer the darkness to the \nominous flickering of the rest of the ship.""",

    "exits": {"north": "Hallway27", "east": "Hallway30", "west": "stairup"},

    "items": []
}

room_hallway30 = {
    "name": "Hallway",

    "description":
    """The server room lies at the end of the hallway, bloodied\nhandprints mark the walls surounding the door....""",

    "exits": {"east": "Server", "west": "Hallway29"},

    "items": []
}

#cupboards

room_cupboard1 = {
    "name": "Cupboard",

    "description":
    """Various cleaning supplies litter the dark cupboard, \nyou think that this could be a good place to hide.""",

    "exits": {"south": "Hallway4"},

    "items": []
}

room_cupboard2 = {
    "name": "Cupboard",

    "description":
    """Various cleaning supplies litter the dark cupboard, \nyou think that this could be a good place to hide.""",

    "exits": {"north": "Hallway5"},

    "items": []
}

room_cupboard3 = {
    "name": "Cupboard",

    "description":
    """Various cleaning supplies litter the dark cupboard, \nyou think that this could be a good place to hide.""",

    "exits": {"north": "Hallway14"},

    "items": []
}

room_cupboard4 = {
    "name": "Cupboard",

    "description":
    """Various cleaning supplies litter the dark cupboard, \nyou think that this could be a good place to hide.""",

    "exits": {"west": "Hallway18"},

    "items": []
}

room_cupboard5 = {
    "name": "Cupboard",

    "description":
    """Various cleaning supplies litter the dark cupboard, \nyou think that this could be a good place to hide.""",

    "exits": {"west": "Hallway22"},

    "items": []
}

room_cupboard6 = {
    "name": "Cupboard",

    "description":
    """Various cleaning supplies litter the dark cupboard, \nyou think that this could be a good place to hide.""",

    "exits": {"east": "Hallway8"},

    "items": []
}

room_cupboard7 = {
    "name": "Cupboard",

    "description":
    """Various cleaning supplies litter the dark cupboard, \nyou think that this could be a good place to hide.""",

    "exits": {"north": "Relay"},

    "items": []
}

room_cupboard8 = {
    "name": "Cupboard",

    "description":
    """Various cleaning supplies litter the dark cupboard, \nyou think that this could be a good place to hide.""",

    "exits": {"north": "Server"},

    "items": []
}

room_stairsDown = {
    "name": "lower Stairwell",

    "description":
    """Stairs are so much better when you are going down \nthem, you whistle a jaunty tune until you see the blood\nseeping from a nearby air duct,oh yeah...killer aliens.""",

    "exits": {"up": "stairup", "north": "Hallway12", "south": "Control"},

    "items": []
}

room_stairsUp = {
    "name": "upper Stairwell",

    "description":
    """You arrive upstairs panting and out of breath, maybe you\nshould have bought that £225 gym membership when you had the\nchance...or not. You remember this floor houses the research,\nrelay, and server rooms.""",

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
