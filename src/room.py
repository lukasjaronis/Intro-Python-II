# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description

        # Room Functionality
        discovered = False
        UP = "up", 'north', 'n'
        DOWN = "down", "south", 's'
        LEFT = "left", "west", 'w'
        RIGHT = "right", "east", 'e'

        # Checking if we've been in a room already

        # Creating a dictionary
        discovered_rooms = {
            'outside': False,
            'foyer': False,
            'overlook': False,
            'narrow': False,
            'treasure': False,
        }



        # room['outside'].n_to = room['foyer']
        # room['foyer'].s_to = room['outside']
        # room['foyer'].n_to = room['overlook']
        # room['foyer'].e_to = room['narrow']
        # room['overlook'].s_to = room['foyer']
        # room['narrow'].w_to = room['foyer']
        # room['narrow'].n_to = room['treasure']
        # room['treasure'].s_to = room['narrow']


