import game_config
import random
from ClassPlayer import Player
from ClassItem import Item

#################################################
# CREATE ITEMS, MONSTERS AND PLAYERS
#################################################

# Create items
ItemTypes = game_config.ItemTypes
items=[]
for i in range(0,len(ItemTypes)):
    items.append(Item(ItemTypes[i][0], ItemTypes[i][1]))

# Create monsters
MonsterTypes = game_config.MonsterTypes
monsters=[]
for i in range(0,len(MonsterTypes)):
    monsters.append(Player(name = MonsterTypes[i][0], power = MonsterTypes[i][1], description = MonsterTypes[i][2]))

# Create player
player = Player("Bars", 1, "PLAYER")

#################################################
# SET THE SCENE
#################################################

# Give 2 items to player
player.addItem(items.pop(0))
player.addItem(items.pop(0))

# Place a monster to Arena
arena =[[], []]

arena[0].append(monsters.pop(0))

# Place player to Arena
arena[1].append(player)

# Print the stats of monster
print("")
print(player.name + " has entered into a room. There is a monster in the room. " + arena[0][0].name + "!(" + str(arena[0][0].power) + ")")
print(arena[0][0].description)

# Print the stats of the player
print("")
print(player.name + " has " + str(player.getTotalPower()) + " power and level " + str(player.level) + ", has the following items;")
for item in player.list_of_items:
    print(item.name + " (Pwr:" + str(item.power) + ")")
print("")

#################################################
# THE FIGHT
#################################################

choice = input("You have 2 options: 1)RUN or 2)FIGHT\nYour choice: ")

if choice == "1":
    # Roll a dice and decide if the player dies or runs...
    print("We will roll a dice for you. If the number is equal to 5 or higher, you will survive. Else... You will lose all your levels.")
    input("Press ENTER to continue...")
    dice = random.randint(1,6)
    if dice >= 5:
        print("The number is " + str(dice) + ". You are free to go...")
    else:
        print("The number is " + str(dice) + ". You lost your levels.")
        player.level = 1
elif choice == "2":
    # Calculate the Power of Monster side
    total_monster_power = 0
    for monster in arena[0]:
        total_monster_power += monster.power
    print("Total power of the Monsters: " + str(total_monster_power))

    # Calculate the power of Player side
    total_player_power = 0
    for player in arena[1]:
        total_player_power += player.getTotalPower()
    print("Total power of the players: " + str(total_player_power))

    # Decide on the winner side
    if total_player_power > total_monster_power:
        # Player wins
        print(player.name + " killed " + arena[0][0].name)
        # Player gets a card
        player.addItem(items.pop(0))
    
