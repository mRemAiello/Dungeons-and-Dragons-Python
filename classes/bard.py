from misc.dice import d6
from classes.base_class import BaseClass

# Bards, Clerics, Druids, Monks, Rogues and Warlocks start with 8 HP and gain +5 with every level up.
# Il bardo è una classe che parte con 100 monete di default, senza casualità nè altro.


class Bard(BaseClass):

    def get_base_hp(self):
        return 5

    def get_hp_for_level_up(self):
        return 4

    def get_money_dice_launches(self):
        return 0

    def roll_dice(self):
        return d6()

    def get_coins(self):
        return 100

    def get_name(self):
        return "Bardo"