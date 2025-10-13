from items.item import Item


class Shield(Item):
    defense = 0

    def __init__(self, name, sale_cost, defense):
        super().__init__(name, sale_cost)
        self.defense = defense

    def __str__(self):
        description = super().__str__()
        description += f", Defense: {self.defense}"
        return description