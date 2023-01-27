import game_config
import random
from ClassItem import Item
from ClassPlayer import Player

class ArenaController:
    
    def __init__(self, size=10):
        self.size = size
        self.items_deck = []
        self.monsters_deck = []
        self.enemy_side = []
        self.allies_side = []

    def createItemsDeck(self):
        ItemTypes = game_config.ItemTypes
        for i in range(0,self.size):
            self.items_deck.append(Item(ItemTypes[i%len(ItemTypes)][0],
                ItemTypes[i%len(ItemTypes)][1]))
    
    def createMonstersDeck(self):
        MonsterTypes = game_config.MonsterTypes
        for i in range(0,self.size):
            self.monsters_deck.append(Player(name = MonsterTypes[i%len(MonsterTypes)][0],
                power = MonsterTypes[i%len(MonsterTypes)][1],
                description = MonsterTypes[i%len(MonsterTypes)][2]))

    def createPlayers(self, name = "DefaultPlayer", power = 1, type = "PLAYER"):
        self.player = Player(name, power, type)

    def giveItemToPlayer(self):
        if len(self.items_deck) > 0:
            self.player.addItem(self.items_deck.pop(0))
        else:
            print("There is no item left in the deck.")

    def placeMonsterToArena(self):
        if len(self.monsters_deck) > 0:
            self.enemy_side.append(self.monsters_deck.pop(0))
        else:
            print("There is no monsters left in the deck.")

    def placePlayerToArena(self):
        self.allies_side.append(self.player)

    def describeArena(self):
        print("On the enemy side weeee haveeeee")
        for enemy in self.enemy_side:
            enemy.describePlayer()
        
        print("Aaaand on the allieeess siideee, weeee haaaveee")
        for player in self.allies_side:
            player.describePlayer()

