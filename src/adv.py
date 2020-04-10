import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100


class Player:
    def __init__(self):
        self.name = ''
        self.career = ''
        self.location = 'outside'
        self.treasure = False


user = Player()


def game_loop():
    while user.treasure is False:
        prompt()


############# Title Screen ################
def title_screen_selections():
    # option = prompt for user when called
    option = input(">: ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a command that is valid.")
        option = input(">: ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('clear')
    print('###########################################')
    print("Welcome to Lukas's adventure text based game!")
    print('###########################################')
    print('                ~ Play ~                   ')
    print('                ~ Help ~                   ')
    print('                ~ Quit ~                   ')
    print('###########################################')
    print('###########################################')
    title_screen_selections()


def help_menu():
    print('###########################################')
    print("Welcome to Lukas's adventure text based game!")
    print('###########################################')
    print("~ Type ['n', 'e', 's', 'w'] to move throughout the game ")
    print("                'n' = North                ")
    print("                'e' = East                 ")
    print("                's' = South                ")
    print("                'w' = West                 ")
    print("           'pu' = Pick Up an Item          ")
    print("           'drop' = Drop an Item          ")
    print('###########################################')
    print("                'q' = Quit                 ")
    print('###########################################')
    print("                Have fun!                  ")
    print('###########################################')
    title_screen_selections()

    ###########################################

    ############# Room ########################


room_name = str
room_description = str
discovered = False
death = False
UP = "up", 'north', 'n'
DOWN = "down", "south", 's'
LEFT = "left", "west", 'w'
RIGHT = "right", "east", 'e'
ERROR = False

# Creating a dictionary
discovered_rooms = {
    'outside': False,
    'foyer': False,
    'overlook': False,
    'narrow': False,
    'treasure': False,
    'error': False
}


# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

# 'outside' = UP to 'foyer'
# 'foyer' = DOWN to 'outside'
# 'foyer' = UP to 'overlook'
# 'foyer' = RIGHT to 'narrow'
# 'overlook' = DOWN to 'foyer'
# 'narrow' = LEFT to 'foyer'
# 'narrow' = UP to 'treasure'
# 'treasure' DOWN to 'narrow'
# 'treasure' LEFT to 'death'


def print_location():
    print('\n' + ('#' * (4 + len(user.location))))
    print('#' + user.location.upper() + ' #')
    print('#' + room_map[user.location][room_description] + ' #')
    print('\n' + ('#' * (4 + len(user.location))))


def prompt():
    print("\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("WHAT do you want to do?")
    print("#######################")
    print("['quit', 'move', 'walk']")
    action = input(">: ")
    acceptable_actions = ['quit', 'move', 'walk', 'pick up', 'drop']
    while action.lower() not in acceptable_actions:
        print("Unknown command, try again. \n")
        action = input(">: ")
    if action.lower() == 'quit':
        print("Good bye!")
        sys.exit()
    elif action.lower() in ['move', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['pick up', 'drop']:
        player_interact(action.lower())


def player_move(playerAction):
    ask = "Which direction would you like to go?\n"
    print("#######################")
    print(["up", 'north', 'n'])
    print(["down", "south", 's'])
    print(["left", "west", 'w'])
    print(["right", "east", 'e'])
    dest = input(ask)
    if dest in ["up", 'north', 'n']:
        destination = room_map[user.location][UP]
        movement_handler(destination)
    elif dest in ["down", "south", 's']:
        destination = room_map[user.location][DOWN]
        movement_handler(destination)
    elif dest in ["left", "west", 'w']:
        destination = room_map[user.location][LEFT]
        movement_handler(destination)
    elif dest in ["right", "east", 'e']:
        destination = room_map[user.location][RIGHT]
        movement_handler(destination)
    elif dest is ERROR:
        destination = room_map[user.location][ERROR]
        movement_handler(destination)


def movement_handler(destination):
    if destination != ERROR:
        print('\n' + "You have moved to the " + destination + ".")
        user.location = destination
        print_location()
    elif ERROR is True:
        print(ERROR)
        print(user.location)
        # while ERROR is True:
        #     witch = f"Hello, {user.name}, seems like you've entered the witchers room \n"
        #     witch2 = f"I will teleport you back to spawn! \n"
        #     witch3 = "Muahahahahahaha"
        #     for character in witch:
        #         sys.stdout.write(character)
        #         sys.stdout.flush()
        #         time.sleep(0.05)
        #     for character in witch2:
        #         sys.stdout.write(character)
        #         sys.stdout.flush()
        #         time.sleep(0.05)
        #     for character in witch3:
        #         sys.stdout.write(character)
        #         sys.stdout.flush()
        #         time.sleep(0.1)
        # user.location = 'outside'



def player_interact(action):
    if room_map[user.location][discovered] == True:
        print("You've already been here! Stop running around in circles!")
    else:
        print("Ah... the fresh air of a new path!")


room_map = {
    'outside': {
        room_name: "Outside Cave Entrance",
        room_description: "North of you, the cave mount beckons",
        discovered: False,
        death: False,
        UP: 'foyer',
        DOWN: 'error',
        LEFT: 'error',
        RIGHT: 'error',
    },
    'foyer': {
        room_name: "Foyer",
        room_description: "North of you, the cave mount beckons",
        discovered: False,
        death: False,
        UP: 'overlook',
        DOWN: 'outside',
        LEFT: 'error',
        RIGHT: 'narrow',
    },
    'overlook': {
        room_name: "Grand Overlook",
        room_description: """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
        discovered: False,
        death: False,
        UP: ERROR,
        DOWN: 'foyer',
        LEFT: 'error',
        RIGHT: 'error',
    },
    'narrow': {
        room_name: "Narrow Passage",
        room_description: """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
        discovered: False,
        death: False,
        UP: 'treasure',
        DOWN: 'error',
        LEFT: 'foyer',
        RIGHT: 'error',
    },
    'treasure': {
        room_name: "Treasure Chamber",
        room_description: """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
        discovered: False,
        death: False,
        UP: 'error',
        DOWN: 'narrow',
        LEFT: 'death',
        RIGHT: 'error',
    },
    'death': {
        room_name: "Spooky House",
        room_description: """You've entered the spooky house and died :( Sorry!""",
        discovered: False,
        death: True,
    },
    'error': {
        room_name: "The Witchers Home",
        room_description: """You better hide from the witch!""",
        discovered: False,
        ERROR: True,
    }
}


###########################################

def setup_game():
    os.system('clear')

    question_one = " Hello, what is your name?\n"
    for character in question_one:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    player_name = action = input(">: ")
    user.name = player_name

    question_two = f"{user.name}, what role do you want to play?\n"
    question_two_extra = f"BUT {user.name}, you can only play as...\n"
    question_two_extra_again = "'lambda warrior', 'python killa', 'ux sniper' \n"
    for character in question_two:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in question_two_extra:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in question_two_extra_again:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    player_career = input(">: ")
    valid_careers = ['lambda warrior', 'ux sniper', 'python killa']
    if player_career.lower() in valid_careers:
        Player.career = player_career
        print(f'You are now a {player_career}' + '!\n')
    else:
        while player_career.lower() not in valid_careers:
            player_career = input(">: ")
            if player_career.lower() in valid_careers:
                Player.career = player_career
                print("You are now" + player_career + "! \n")

    question_three = "Welcome " + user.name + " the " + user.career + " \n"""
    for character in question_three:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)

    speech = "Good luck finding the treasure!\n"
    for character in speech:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

        os.system('clear')
        print("##################################")
        print("           Start it Up!           ")
        print("##################################")
        game_loop()


# Calling the game
title_screen()
