import game_config

class Player:

    def __init__(self, name = "DefaultPlayer", power = 1, type = "NPC", description = "TBD"):
        self.name = name
        self.power = power
        self.list_of_items = []
        self.level = 1
        self.type = type
        self.description = description

    def increaseLevel(self):
        self.level += 1

    def decreaseLevel(self):
        self.level -= 1
    
    def addItem(self, item):
        self.list_of_items.append(item)
        print(self.name + " has received an item!")
        print(item.name + " (" + str(item.power) + ")")

    def removeItem(self,item):
        return self.list_of_items.pop(0)

    def getTotalPower(self):
        power = 0
        for item in self.list_of_items:
            power += item.power
        
        return power + (self.level if self.type!="NPC" else 0)

    def describePlayer(self):
        if self.type == "NPC":
            print("")
            print(self.name + " (" + str(self.power) + ")")
            print(self.description)
        elif self.type == "PLAYER":
            print("")
            print(self.name + ", Level: " 
                + str(self.level) + " with a total power: " 
                + str(self.getTotalPower()))
            print("with the following items:")
            for item in self.list_of_items:
                print(item.name + " ("  + str(item.power) + ")")

