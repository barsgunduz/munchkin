import game_config
import random
from classes import Character, Item, Deck

main_player = Character("Player", "Bars", 0)

deck = Deck(10, 10)
deck.printDeck()