import game_config
import random

class Character:

    def __init__(self, d_label="Monster", d_name="DefaultName", d_level = 1, d_power = 1):
        self.label = d_label
        self.name = d_name
        self.level = d_level
        self.power = d_power
        self.list_of_items = []

    def addItem(self, item_object):
        self.list_of_items.append(item_object)

    def removeItem(self, item_object):
        self.list_of_items.remove(item_object)

    def sendItemTo(self, character_object, item_object):
        self.removeItem(item_object)
        character_object.addItem(item_object)

    def getTotalPower(self):
        total_power = self.level + self.power
        if len(self.list_of_items)>0:
            for item in self.list_of_items:
                total_power += item.power
        return total_power

class Item:

    def __init__(self, d_label="Item", d_name="DefaultItem", d_power = 1):
        self.label = d_label
        self.name = d_name
        self.power = d_power