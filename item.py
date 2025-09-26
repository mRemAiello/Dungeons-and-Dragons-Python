from dado import dx


class Item:
    name = ""
    sale_cost = 0

    def __init__(self, name, sale_cost):
        self.name = name
        self.sale_cost = sale_cost

    def __str__(self):
        description = f"Item name: {self.name}, Item sale cost: {self.sale_cost} "
        return description


class Weapon(Item):
    attack = 0

    def __init__(self, name, sale_cost, attack):
        super().__init__(name, sale_cost)
        self.attack = attack

    def roll_die(self):
        return dx(self.attack)

    def __str__(self):
        description = super().__str__()
        description += f"Attack: {self.attack}"
        return description


class RangedWeapon(Item):
    attack = 0

    def __init__(self, name, sale_cost, attack):
        super().__init__(name, sale_cost)
        self.attack = attack

    def roll_die(self):
        return dx(self.attack)

    def __str__(self):
        description = super().__str__()
        description += f"Attack: {self.attack}"
        return description


class Shield(Item):
    defense = 0

    def __init__(self, name, sale_cost, defense):
        super().__init__(name, sale_cost)
        self.defense = defense

    def __str__(self):
        description = super().__str__()
        description += f"Defense: {self.defense}"
        return description


class Armor(Item):
    defense = 0

    def __init__(self, name, sale_cost, defense):
        super().__init__(name, sale_cost)
        self.defense = defense

    def __str__(self):
        description = super().__str__()
        description += f"Defense: {self.defense}"
        return description
