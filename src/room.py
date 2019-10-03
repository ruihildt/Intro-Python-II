# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(self, name, description, inventory = []):
        self.name = name
        self.description = description
        self.inventory = inventory

    def __str__(self):
        output = f'{self.name}'
        if len(self.inventory) == 0:
            output = f'There are no items in the room.'
        for i in self.inventory:
            output += f'  * {str(i)}'
