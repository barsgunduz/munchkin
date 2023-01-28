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

arena.askFirstChoice()
    
