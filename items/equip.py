from items.item import Item


class Equip(Item):

    def __init__(self, name, sale_cost):
        super().__init__(name, sale_cost)

    def equip(self, character):
        for item_modifier in self.modifiers:
            item_modifier.attribute.add_modifier(item_modifier.modifier)