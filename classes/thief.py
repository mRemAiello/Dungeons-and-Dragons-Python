from misc.dice import d6
from classes.base_class import BaseClass

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

    def get_name(self):
        return "Ladro"