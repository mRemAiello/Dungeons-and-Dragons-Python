import random

import item

weapon_items = [item.Weapon("Spada", 10, 6), item.Weapon("Ascia", 8, 10)]
ranged_weapon_items = [item.RangedWeapon("Balestra", 15, 12), item.RangedWeapon("Fionda", 4, 3)]
armor_items = [item.Armor("Armatura di cuoio", 18, 12), item.Armor("Armatura a scaglie", 22, 15)]
shield_items = [item.Shield("Scudo rotondo", 11, 8), item.Shield("Scudo torre", 12, 10)]


def choose_item(number):
    selected_item = None
    if number == 1:
        selected_item = random.choice(weapon_items)
    if number == 2:
        selected_item = random.choice(ranged_weapon_items)
    if number == 3:
        selected_item = random.choice(armor_items)
    if number == 4:
        selected_item = random.choice(shield_items)
    if number == 0 or number > 4:
        print("The selected item number does not exist")
    return selected_item
