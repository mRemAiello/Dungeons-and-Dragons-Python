from attributes.fixed_modifier import FixedModifier
from gameplay.character import Character
from items.item_modifier import ItemModifier
from misc.dice import d6
from classes.base_class import BaseClass
from items.weapon import Weapon
from items.armor import Armor

# Bards, Clerics, Druids, Monks, Rogues and Warlocks start with 8 HP and gain +5 with every level up.


class Thief(BaseClass):

    def get_base_hp(self):
        return 8

    def get_hp_for_level_up(self):
        return 5

    def get_money_dice_launches(self):
        return 4

    def roll_dice(self):
        return d6()

    def get_starting_items(self, character: "Character"):
        short_sword = Weapon("Spada Corta", 16, 6)
        modifiers = [ItemModifier(FixedModifier(short_sword, 5), character.dexterity)]
        short_sword.assign_modifiers(modifiers)
        leather_armor = Armor("Armatura di cuoio", 40, 11)
        return [short_sword, leather_armor]

    def get_name(self):
        return "Ladro"