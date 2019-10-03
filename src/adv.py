from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Percy", "also known as the pitchfork from Hell"), Item("Ballsy", "a giant meatball")]),

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

def isInInventory(item_name, inventory):
    names = []
    for i in inventory:
        names.append(i.name.lower())
    if item_name in names:
        return True
    return False

def startAction(action, item_name):
    print('you typed: "', action, item_name,'"')
    if action != ("get" or "take" or "remove" or "drop"):
        print("This isn't a valid command. Please try again.")
        return 

    elif action == ("get" or "take"):
        if isInInventory(item_name, player.current_room.inventory) == True:
            for i in player.current_room.inventory:
                if i.name.lower() == item_name:
                    # Add to the player inventory 
                    player.inventory.append(i)
                    # Remove from the room inventory
                    player.current_room.inventory.remove(i)
                    print(f'\nYou\'ve added {i.name} to your inventory.')
                    return
        print("This item isn't in the room, you can't pick it up.")

    elif action == ("remove" or "drop"):
        if isInInventory(item_name, player.inventory) == True:
            for i in player.inventory:
                if i.name.lower() == item_name:
                    # Add to the room inventory 
                    player.current_room.inventory.append(i)
                    # Remove from the player inventory
                    player.inventory.remove(i)
                    print(f'\nYou\'ve dropped {i.name} to your inventory.')
                    return
        print("This item isn't in your inventory, you can't drop it.")

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Rob Zombie", room['outside'])

# Welcome message
welcome = ""
welcome = f'Welcome to this new quest, {player.name}!\n'
# Prints the current room name
welcome += f'\n* Use "n", "s", "e" or "w" to move. \n* Press q to quit.'
print (welcome)

# Write a loop
done = False

while not done:
    # Print the current room name and its description
    output =  f'\nYou are now in the {player.current_room.name}:\n'
    output += f'{player.current_room.description}.\n'
    output += f'{player.current_room}'

    print(output)
    # Waits for user input and decides what to do.
    s = input("Command > ").strip().lower()
    sList = s.split()

    if len(sList) == 2:
        action = sList[0]
        item_name = sList[1]
        startAction(action, item_name)

    # If the user enters "q", quit the game.
    if s == "q":
        print("Goodbye\n")
        done = True

    # Move to new room
    elif s in ["n", "s", "e", "w"]:
        player.current_room = movePlayer(s, player.current_room)

    # Get player inventory
    elif s == "i":
        if len(player.inventory) == 0:
            print("You're not carrying anything")
        else:
            print("You're carrying:")
            for i in player.inventory:
                print(f'\t - {i}')

    if len(sList) > 2:
        print(f"The command isn't valid. Try again.")
