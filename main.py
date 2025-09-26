import random
from typing import Optional

from item import Armor
from item import Item
from item import RangedWeapon
from item import Shield
from item import Weapon
from scelta_classe import choose_class
from scelta_razza import choose_race
from storia import adventure
from personaggio import Character

race_number = int(input("1. Umano, 2. Nano, 3. Elfo, 4. Gnomo"))
class_number = int(input("1. Barbaro, 2. Paladino, 3. Ladro, 4. Mago"))
selected_race = choose_race(race_number)
selected_class = choose_class(class_number)
selected_item: Optional[Item] = None
if race_number == 1:
    selected_item = Weapon("Mazza", 10, 10)
if race_number == 2:
    selected_item = RangedWeapon("Arco", 11, 12)
if race_number == 3:
    selected_item = Armor("Antica", 10, 13)
if race_number == 4:
    selected_item = Shield("Runico", 10, 12)
character_name = input("Dimmi il nome del tuo personaggio")
sale_price = int(random.uniform(1, 10))
selected_character = Character(character_name, selected_race, selected_class)
if selected_item is not None:
    selected_character.equip_item(selected_item)
print(selected_character)
while not selected_character.is_dead():
    adventure(selected_character)
