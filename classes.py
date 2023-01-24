import game_config
import random

class Character:

    def __init__(self, d_label="Monster", d_name="DefaultName", d_power = 1):
        self.label = d_label
        self.name = d_name
        self.level = 0
        self.power = d_power
        self.list_of_items = []

    def addItem(self, item_object):
        self.list_of_items.append(item_object)

    def removeItem(self, item_object):
        self.list_of_items.remove(item_object)

    def getTotalPower(self):
        total_power = self.level + self.power
        if len(self.list_of_items)>0:
            for item in self.list_of_items:
                total_power += item.power
        return total_power
    
    def display(self):
        print("Character: "+self.name+" ("+str(self.getTotalPower())+")")

class Item:

    def __init__(self, d_label="Item", d_name="DefaultItem", d_power = 1):
        self.label = d_label
        self.name = d_name
        self.power = d_power

    def display(self):
        print("Item: "+self.name+" ("+str(self.power)+")")

class Deck:

    def __init__(self, size_monsters = 10, size_items=10):
        self.list_of_monsters=[]
        self.list_of_items=[]
        self.createMonsters(size_monsters)
        self.createItems(size_items)

    def createMonsters(self, size_monsters):
        print("size will be "+str(size_monsters))
        for i in range(0, size_monsters):
            self.list_of_monsters.append(Character("Monster", "DefaultMonster", random.randint(1,5)))

    def createItems(self, size_items):
        for i in range(0, size_items):
            self.list_of_items.append(Item("Item", "DefaultItem", random.randint(1,5)))

    def printDeck(self):
        count = 0
        for monster in self.list_of_monsters:
            count += 1
            print(str(count), end=" ")
            monster.display()
        
        count = 0
        for item in self.list_of_items:
            count += 1
            print(str(count), end=" ")
            item.display()
