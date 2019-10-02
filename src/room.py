# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    directions = []

    def __init__(self, name, description, directions):
        self.name = name
        self.description = description
        self.directions = directions

    def __str__(self):
        return f'{self.name}'
