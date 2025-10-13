from classes.base_class import BaseClass
from misc.dice import d6

# Sorcerers and Wizards start with 6 HP and gain +4 with every level up.


class Mage(BaseClass):

    def get_base_hp(self):
        return 6

    def get_hp_for_level_up(self):
        return 4

    def get_money_dice_launches(self):
        return 3

    def roll_dice(self):
        return d6()

    def get_name(self):
        return "Mago"
