from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('PlayerOne', room['outside'])
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


def print_welcome_message():
    print('\n** Welcome to the greatest Adventure Game ever made! **')


def prompt_player():
    prompt_text = 'What would you like to do?\nYou can press "h" to open the help menu and see the options available to you. '
    key = input(prompt_text).split(' ')
    handle_input(key)


def print_supported_input():
    print('n: go North')
    print('w: go West')
    print('s: go South')
    print('e: go East')
    print('q: quit adventure')
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
        elif key in cardinal_directions.keys():
            print(f'You moved {cardinal_directions[key]}.')
            player.move(key)
            player.print_current_room()
            prompt_player()
        else:
            print("\nYou can't do that here, young adventurer!\n")
            prompt_player()


def quit_adventure():
    print('\nYou have chosen to abandon your quest.\n')


main()
