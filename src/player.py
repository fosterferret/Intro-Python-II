# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def print_current_room(self):
        print(f'\nCurrent room: {self.current_room}')

    def move(self, direction):
        new_room = getattr(self.current_room, f'{direction}_to')
        if not new_room:
            print('\nDark things lie there so you cannot go there!')
        else:
            self.current_room = new_room
            print(f'You are now in the {self.current_room}')

    def get_item(self, item_to_get):
        if any(item.name == item_to_get for item in self.current_room.items):
            item_object = next(
                (item for item in self.current_room.items if item.name == item_to_get), None)
            self.items.append(item_object)
            self.current_room.items.remove(item_object)
        else:
            print(f"{item_to_get} isn't in this room...")
