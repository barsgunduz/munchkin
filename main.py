import game_config
import random
from ClassPlayer import Player
from ClassItem import Item
from classes import ArenaController

#################################################
# CREATE ITEMS, MONSTERS AND PLAYERS
#################################################

# Create the Arena
arena = ArenaController(10)

# Create items
arena.createItemsDeck()

# Create monsters
arena.createMonstersDeck()

# Create player
arena.createPlayers("Bars", 1)

#################################################
# SET THE SCENE
#################################################

# Give 2 items to player
arena.giveItemToPlayer()
arena.giveItemToPlayer()

# Place a monster to Arena
arena.placeMonsterToArena()

# Place player to Arena
arena.placePlayerToArena()

# Describe the Arena
arena.describeArena()

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
    
