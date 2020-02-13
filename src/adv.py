from room import Room
from player import Player
from item import LightSource
from item import Treasure
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Create list of items to add to rooms
item = {
    'sword': Item("sword", "The weapon of choice of all great adventurers."),
    'gold': Treasure('gold', "The treasure that the adventurer seeks!"),
    'lantern': LightSource('lantern', "Let there be light, and there was"),
}

room['outside'].add_item(item['lantern'])
room['outside'].add_item(item['sword'])
room['treasure'].add_item(item['gold'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


def prYellow(skk): print("\033[94m {}\033[00m" .format(skk))


player_name = input("\nWelcome to the land of mysteries. What is your name?: ")
player = Player(player_name, room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def main():
    print_welcome_message()
    player.print_current_room()
    prompt_player()


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def print_welcome_message():
    prGreen(
        f'\n** Hello, {player_name} - welcome to the greatest Adventure Game ever made! **')


def prompt_player():
    prompt_text = '\nWhat would you like to do next?\nYou can press "h" to open the help menu and see the options available to you. '
    key = input(prompt_text).split(' ')
    handle_input(key)


def print_supported_input():
    print('\nn: go North')
    print('w: go West')
    print('s: go South')
    print('e: go East')
    print('q: quit adventure')
    print('drop [item]: drop an item and remove it from your inventory')
    print('get/pickup [item]: add an item to your inventory \n')
    prompt_player()


def handle_invalid_input():
    print("\nYou can't do that here, young adventurer!\n")
    prompt_player()


def handle_input(key):
    if len(key) == 1:
        key = key[0].lower()

        cardinal_directions = {'n': 'North',
                               'e': 'East',
                               's': 'South',
                               'w': 'West'}

        if key == 'q':
            quit_adventure()
        elif key == 'h':
            print_supported_input()
        elif key == 'i':
            player.print_inventory()
            prompt_player()
        elif key in cardinal_directions.keys():
            prYellow(f'Current Location: {cardinal_directions[key]}.')
            player.move(key)
            player.print_current_room()
            prompt_player()

    elif len(key) == 2:
        action = key[0].lower()
        item_desc = key[1].lower()
        global last_item
        if item_desc == 'it':
            item_desc = last_item
        last_item = item_desc

        if action == 'get' or action == 'pick':
            player.get_item(item_desc)
            prompt_player()
        elif action == 'drop':
            player.drop_item(item_desc)
            prompt_player()
        else:
            handle_invalid_input()

    else:
        handle_invalid_input()


def quit_adventure():
    print('\nYou have chosen to abandon your quest.\n')


main()
