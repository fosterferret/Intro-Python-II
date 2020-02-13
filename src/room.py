# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, is_lit):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.is_lit = is_lit

    def __str__(self):
        return f'{self.name}\n{self.description}\n'

    def print_items(self):
        for item in self.items:
            print(f'This is a {item.name}: {item.description}.')

    def add_item(self, item):
        self.items.append(item)
