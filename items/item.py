class Item:
    name = ""
    sale_cost = 0
    modifiers = []

    def __init__(self, name, sale_cost):
        self.name = name
        self.sale_cost = sale_cost

    def assign_modifiers(self, modifiers):
        self.modifiers = modifiers

    def __str__(self):
        description = f"{self.name}, Sale cost: {self.sale_cost}"
        if len(self.modifiers) > 0:
            description += ", "
        for item_modifier in self.modifiers:
            description += f"{item_modifier.attribute.get_name()}: {item_modifier.modifier.get_value_modifier()}, "
        return description