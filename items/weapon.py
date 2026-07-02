from items.equip import Equip
from misc.dice import dx


class Weapon(Equip):
    attack = 0

    def __init__(self, name, sale_cost, attack):
        super().__init__(name, sale_cost)
        self.attack = attack

    def roll_die(self):
        return dx(self.attack)

    def __str__(self):
        description = super().__str__()
        description += f"Attack: D{self.attack}"
        return description