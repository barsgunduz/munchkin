import game_config
import random

class User_Character:
    created_user_count = 0

    def __init__(self, d_obj_name="DefaultName", d_level=1, d_power=0, d_ally=None):
        print("Creating a new user character: " + d_obj_name)
        User_Character.created_user_count += 1
        self.obj_name = d_obj_name
        self.level = d_level
        self.power = d_power
        self.ally = d_ally
        self.list_of_items = []
        self.status = "alive"

    def display_obj_information(self):
        print("Name: " + self.obj_name)
        print("Level: " + str(self.level))
        print("Power: " + str(self.power))
        if len(self.list_of_items) > 0:
            for item in self.list_of_items:
                print("Item: "+item.obj_name+" ("+str(item.power)+")")
        if self.ally is not None:
            print("Ally: " + self.ally.obj_name)

    def getItem(self, item_obj):
        print("You got item "+ item_obj.obj_name + " with its "+str(item_obj.power)+" power.")
        self.list_of_items.append(item_obj)

    def attack(self, monster_obj):
        monster_obj.battle(self)


class NPC_Monster:
    created_npc_monster_count = 0

    def __init__(self, d_obj_name="DefaultMonster", d_power=1):
        print("Creating a new NPC Monster character: " + d_obj_name)
        NPC_Monster.created_npc_monster_count += 1
        self.obj_name = d_obj_name
        self.power = d_power
    
    def display_obj_information(self):
        print("Name: " + self.obj_name)
        print("Power: " + str(self.power))

    def die(self, attacker, ally=None):
        print("The monster "+ self.obj_name+" has been killed by "+ attacker.obj_name)
        attacker.level += 1

    def kill(self, attacker, ally=None):
        print("The monster "+ self.obj_name+" has killed "+ attacker.obj_name)
        attacker.level -= 1
    
    def battle(self, attacker, ally=None):
        print(attacker.obj_name + "is attacking to the monster "+ self.obj_name)
        if attacker.power+attacker.level > self.power:
            self.die(attacker, ally)
        else:
            self.kill()

class Monsters_Deck:
    def __init__(self, size_of_deck=10):
        self.list_of_monsters = []
        for i in range(1,size_of_deck):
            random_monster_name = game_config.MonsterTypes[random.randint(0,len(game_config.MonsterTypes)-1)]
            random_monster_power = random.randint(1,6)
            self.list_of_monsters.append(NPC_Monster(random_monster_name, random_monster_power))

    def release_monster(self, arena_obj):
        arena_obj.monster_list.append(self.list_of_monsters.pop(0))

class Item:
    created_item_count = 0

    def __init__(self, d_obj_name="DefaultItem", d_power=1):
        print("Creating a new item: " + d_obj_name)
        Item.created_item_count += 1
        self.obj_name = d_obj_name
        self.power = d_power

    def display_obj_information(self):
        print("Name: " + self.obj_name)
        print("Power: " + str(self.power))

class Items_Deck:

    def __init__(self, size_of_deck=10):
        self.list_of_items = []
        for i in range(1,size_of_deck):
            random_item_name = game_config.ItemTypes[random.randint(0,len(game_config.ItemTypes)-1)]
            random_item_power = random.randint(1,4)
            self.list_of_items.append(Item(random_item_name, random_item_power))

    def give_card(self, player_obj):
        player_obj.list_of_items.append(self.list_of_items.pop(0))

class Arena:

    def __init__(self):
        self.monster_list = []
        self.player_list = []
