class Item:
    name = ""
    sale_cost = 0

    def __init__(self, name, sale_cost):
        self.name = name
        self.sale_cost = sale_cost

    def __str__(self):
        description = f"{self.name}, Sale cost: {self.sale_cost}"
        return description