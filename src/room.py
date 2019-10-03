# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:

    def __init__(self, name, description, inventory = None):
        self.name = name
        self.description = description
        self.inventory = inventory
        if inventory is None:
            self.inventory = []

    def __str__(self):
        output = ''
        if len(self.inventory) == 0:
            output = f'There are no items in the room.'
        if len(self.inventory) == 1:
            output += f'There is the following item:'
            output += f'\n * {self.inventory[0]}'
        if len(self.inventory) > 1:
            output += f'There are the following items:'
            for i in self.inventory:
                output += f'\n * {i}'
        return output


# outside = Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east.""", [Item("Percy", "also known as the pitchfork from hell"), Item("Squasher", " a tea spoon")])

# print(outside)