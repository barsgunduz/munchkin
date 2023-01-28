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

    def shuffleDeck(self, array):
        new = []
        while len(array)>0:
            new.append(array.pop(random.randint(0,len(array)-1)))
        return new

    def createItemsDeck(self):
        ItemTypes = game_config.ItemTypes
        for i in range(0,self.size):
            self.items_deck.append(Item(ItemTypes[i%len(ItemTypes)][0],
                ItemTypes[i%len(ItemTypes)][1]))
        self.items_deck = self.shuffleDeck(self.items_deck)
        
    def createMonstersDeck(self):
        MonsterTypes = game_config.MonsterTypes
        for i in range(0,self.size):
            self.monsters_deck.append(Player(name = MonsterTypes[i%len(MonsterTypes)][0],
                power = MonsterTypes[i%len(MonsterTypes)][1],
                description = MonsterTypes[i%len(MonsterTypes)][2]))
        self.monsters_deck = self.shuffleDeck(self.monsters_deck)

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

    def playerRunsAway(self):
        # Roll a dice and decide if the player dies or runs...
        print("We will roll a dice for you. If the number is equal to 5 or higher, you will survive. Else... You will lose all your levels.")
        input("Press ENTER to continue...")
        dice = random.randint(1,6)
        if dice >= 5:
            print("The number is " + str(dice) + ". You are free to go...")
        else:
            print("The number is " + str(dice) + ". You lost your levels.")
            for player in self.allies_side:
                player.level = 1

    def playerFights(self):
        # Calculate the Power of Monster side
        total_monster_power = 0
        for monster in self.enemy_side:
            total_monster_power += monster.power
        print("Total power of the Monsters: " + str(total_monster_power))

        # Calculate the power of Player side
        total_player_power = 0
        for player in self.allies_side:
            total_player_power += player.getTotalPower()
        print("Total power of the players: " + str(total_player_power))

        # Decide on the winner side
        if total_player_power > total_monster_power:
            # Player wins
            print(self.allies_side[0].name + " killed " + self.enemy_side[0].name)
            # Player gets a card
            self.allies_side[0].addItem(self.items_deck.pop(0))

    def askFirstChoice(self):
        print("You have 2 options:")
        print("1) RUN")
        print("2) FIGHT")
        choice = input("Your choice: ")
        if choice == "1":
            self.playerRunsAway()
        elif choice == "2":
            self.playerFights()

