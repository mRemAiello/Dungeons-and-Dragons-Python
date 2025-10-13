from misc.dice import d12
from classes.base_class import BaseClass

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

    def get_name(self):
        return "Barbaro"
