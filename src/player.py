# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player:
    def __init__(self, name, current_room, inventory = [Item("Squasher", " a tea spoon")]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'{self.name} is in {self.current_room}.'

    

