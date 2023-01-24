import game_config
import random
from classes import User_Character, NPC_Monster, Monsters_Deck, Item, Items_Deck, Arena


main_player = User_Character("Bars", 2)

list_of_monsters = []
for i in range(1,10):
    random_monster_name = game_config.MonsterTypes[random.randint(0,len(game_config.MonsterTypes)-1)]
    random_monster_power = random.randint(1,6)
    list_of_monsters.append(NPC_Monster(random_monster_name, random_monster_power))

items = Items_Deck(30)
monsters = Monsters_Deck(30)
arena = Arena()
main_player = User_Character("Bars", 2, 3)

monsters.release_monster(arena)
monsters.release_monster(arena)
monsters.release_monster(arena)

items.give_card(main_player)
items.give_card(main_player)
items.give_card(main_player)
items.give_card(main_player)

main_player.display_obj_information()
print("end")