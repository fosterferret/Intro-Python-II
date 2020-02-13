# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def print_current_room(self):
        print(f'\nCurrent room: {self.current_room}')
    
    def has_a_lightsource(self):
        return any(isinstance(item, LightSource) for item in self.items)

    def move(self, direction):
        new_room = getattr(self.current_room, f'{direction}_to')
        if not new_room:
            print('\nYou may not tread that path, young adventurer, as it is a dead end!')
        else:
            self.current_room = new_room
            print(f'You are now in the {self.current_room}')
    
    def drop_item(self, item_to_drop):
        if any(item.name == item_to_drop for item in self.items):
            item_object = next(
                (item for item in self.items if item.name == item_to_drop), None)
            self.items.remove(item_object)
            self.current_room.items.append(item_object)
            item_object.on_drop()
        else:
            print(f"You can't lose what you don't own({item_to_drop})!")

    def get_item(self, item_to_get):
        if any(item.name == item_to_get for item in self.current_room.items):
            item_object = next(
                (item for item in self.current_room.items if item.name == item_to_get), None)
            self.items.append(item_object)
            self.current_room.items.remove(item_object)
        else:
            print(f"{item_to_get} isn't in this room...")

    def print_inventory(self):
        if not len(self.items):
            print('\nYou have no item in your inventory.')
        else:
            print('\nThe items in your inventory are:')
            for item in self.items:
                print(f'- {item}')
