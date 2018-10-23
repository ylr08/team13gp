from items import *
from people import *
from puzzles import *

room_courtyard = {
    "name": "Courtyard",

    "description":
    """This is the courtyard. TODO ---""",
    # exits/people/items in room will be added using functions in game.py
    # (printed in full sentences)

    "exits": {"north": "Great Hall", "south": "Battlements"},

    "items": [item_oldboot],

    "people": {"lady":people_lady, "catherine":people_lady},

    "puzzles" : [],

    "objects": [object_fountain, object_lady]

}

room_greathall = {
    "name": "Great Hall",

    "description":
    """This is the great hall. TODO ---""",

    "exits": {"west": "Throne Room", "south": "Courtyard", "east": "Battlements", "north": "Anteroom"},

    "items": [],

    "people": {"wizard":people_wizard, "gaius":people_wizard},

    "puzzles" : [],
	
    "objects": [object_wizard]

}

room_throne = {
    "name": "Throne Room",

    "description":
    """This is the throne room. TODO ---""",

    "exits": {"east": "Great Hall"},

    "items": [],

    "people": {"king":people_king,
               "viceroy":people_viceroy},

    "puzzles" : [],
	
    "objects": [object_king, object_viceroy]

}

room_battlements = {
    "name": "Battlements",

    "description":
    """These are the battlements. TODO ---""",

    "exits": {"west": "Great Hall", "north": "Courtyard"},

    "items": [],

    "people": {"soldier":people_soldier1, "warrior":people_soldier2},

    "puzzles" : [dice_game],

    "objects": [object_soldier1, object_soldier2]

}

room_ante = {
    "name": "Anteroom",

    "description":
    """This is the anteroom. TODO ---""",

    "exits": {"south": "Great Hall"},

    "items": [],

    "people": {},

    "puzzles" : [],

    "objects": []

}

room_jail = {
    "name": "Jail",

    "description":
    """This is the jail. TODO ---""",

    "exits": {},

    "items": [],

    "people": {},

    "puzzles" : [],
	
    "objects": []

}


rooms = {
    "Courtyard": room_courtyard,
    "Great Hall": room_greathall,
    "Throne Room": room_throne,
    "Battlements": room_battlements,
    "Anteroom": room_ante,
    "Jail": room_jail
}
