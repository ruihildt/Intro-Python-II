from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", ["n"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["n", "s", "e"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["s"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["n", "w"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["w"]),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Rob Zombie", room['outside'])
directions = player.current_room.directions

output = ""
output = f'Welcome to this new quest, {player.name}!\n\n'
# Prints the current room name
output += f'You are now in the {player.current_room.name}.\n'
# Prints the current description
output += f'{player.current_room.description}.\n\n'
output += f'You have the following options:\n'
for d in directions:
    output += f' - press "{d}"\n'
output += f' - press "q" to exit\n'
print (output)

# Waits for user input and decides what to do.
selection = input("Where do you want to go? ")

# If the user enters "q", quit the game.
if str(selection) == "q":
    exit()
# Print an error message if the movement isn't allowed.
if str(selection) != ("n" or "s" or "w" or "e"):
    print("Invalid command, chose one of the available options")
# If the user enters a cardinal direction, attempt to move to the room there.
if str(selection) in directions:
    True

