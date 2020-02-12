# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def print_current_room(self):
        print(f'\nCurrent room: {self.current_room}')

    def move(self, direction):
        new_room = getattr(self.current_room, f'{direction}_to')
        if not new_room:
            print('\nDark things lie there so you cannot go there!')
        else:
            self.current_room = new_room
