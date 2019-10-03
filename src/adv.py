from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Percy", "also known as the pitchfork from Hell")]),

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


# helpers functions

def movePlayer(dir, current_room):
    attrib = f'{dir}_to'

    # see if room has destination attrib
    if hasattr(current_room, attrib):
        return getattr(current_room, attrib)

    # otherwise they can't move in that direction
    print("You can't go that way")

    return current_room

def startAction(action, item):
    if action == "get" or "take":
        for i in player.current_room.inventory:
            if i.name.lower() == item:
                # Add to the player inventory 
                player.inventory.append(i)
                # TODO Remove from the room inventory
                print(f'You\'ve added {i.name} to your inventory')
            else:
                print("This item isn't in the room, you can't pick it up")
    # TODO Add possibility to drop item
    # if action == "drop"
        # check if item is in the


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Rob Zombie", room['outside'])

# Welcome message
welcome = ""
welcome = f'Welcome to this new quest, {player.name}!\n'
# Prints the current room name
welcome += f'* Use "n", "s", "e" or "w" to move. \n* Press q to quit.\n'
print (welcome)

# Write a loop
done = False

while not done:
    # Print the current room name and its description
    output =  f'You are now in the {player.current_room.name}:\n'
    output += f'{player.current_room.description}.\n'
    output += f'{player.current_room}'

    print(output)
    # Waits for user input and decides what to do.
    s = input("Command > ").strip().lower()
    sList = s.split()

    if len(sList) == 2:
        action = sList[0]
        item = sList[1]
        startAction(action, item)

        # TODO Make sure output is clean with 2 words

    # If the user enters "q", quit the game.
    if s == "q":
        print("Goodbye\n")
        done = True

    elif s in ["n", "s", "e", "w"]:
        player.current_room = movePlayer(s, player.current_room)

    elif s == "i":
        if len(player.inventory) == 0:
            print("You're not carrying anything")
        else:
            print("You're carrying:")
            for i in player.inventory:
                print(f'\t - {i}')

    else:
        print(f"The command isn't valid. Try again.")
