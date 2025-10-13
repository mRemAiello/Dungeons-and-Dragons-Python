from misc.dice import d10
from classes.base_class import BaseClass

# Fighters, Paladins and Rangers start with 10 HP and gain +6 with every level up.


class Paladin(BaseClass):

    def get_base_hp(self):
        return 10

    def get_hp_for_level_up(self):
        return 6

    def get_money_dice_launches(self):
        return 5

    def roll_dice(self):
        return d10()

    def get_name(self):
        return "Paladino"
