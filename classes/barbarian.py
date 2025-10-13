from misc.dice import d12
from classes.base_class import BaseClass
from items.weapon import Weapon
from items.armor import Armor

# Barbarians start with 12 HP and gain +7 with every level up.


class Barbarian(BaseClass):

    def get_base_hp(self):
        return 12

    def get_hp_for_level_up(self):
        return 7

    def get_money_dice_launches(self):
        return 3

    def roll_dice(self):
        return d12()

    def get_starting_items(self):
        greataxe = Weapon("Ascia Grande", 65, 12)
        barbarian_clothes = Armor("Indumenti del Barbaro", 11, 10)
        return [greataxe, barbarian_clothes]

    def get_name(self):
        return "Barbaro"
