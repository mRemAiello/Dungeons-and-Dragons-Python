import random

from scelta_oggetto import choose_item
from scelta_classe import choose_class
from scelta_razza import choose_race
from mostro import Monster


def create_monster(name):
    monster_race_number = int(random.uniform(1, 4))
    race = choose_race(monster_race_number)
    monster_class_number = int(random.uniform(1, 4))
    character_class = choose_class(monster_class_number)
    monster = Monster(name, race, character_class)
    number = int(random.uniform(1, 4))
    selected_item = choose_item(number)
    monster.equip_item(selected_item)
    return monster
