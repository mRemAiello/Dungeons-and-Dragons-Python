import random
from typing import Optional

from item import Item
from mostro import Monster
from scelta_classe import CharacterClass, choose_class
from scelta_oggetto import choose_item
from scelta_razza import Race, choose_race


def create_monster(name: str) -> Monster:
    monster_race_number: int = int(random.uniform(1, 4))
    race: Optional[Race] = choose_race(monster_race_number)
    monster_class_number: int = int(random.uniform(1, 4))
    character_class: Optional[CharacterClass] = choose_class(monster_class_number)
    monster = Monster(name, race, character_class)
    number: int = int(random.uniform(1, 4))
    selected_item: Optional[Item] = choose_item(number)
    monster.equip_item(selected_item)
    return monster
