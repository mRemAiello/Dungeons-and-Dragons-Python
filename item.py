from dado import dx

class Item:

    nome= ""
    costo_vendita= 0

    def __init__(self, nome, costo_vendita):
        self.nome= nome
        self.costo_vendita= costo_vendita

    def __str__(self):
        stringa= f"Nome arma: {self.nome}, Costo di vendita arma: {self.costo_vendita} "
        return stringa

class Weapon(Item):
    attacco= 0

    def __init__(self,nome, costo_vendita, attacco):
        super().__init__(nome, costo_vendita)
        self.attacco= attacco

    def lancia_dado(self):
        return dx(self.attacco)

    def __str__(self):
        stringa= super().__str__()
        stringa += f"Attacco: {self.attacco}"
        return stringa

class Ranged_Weapon(Item):

    attacco= 0

    def __init__(self, nome, costo_vendita, attacco):
        super().__init__(nome, costo_vendita)
        self.attacco = attacco

    def lancia_dado(self):
        return dx(self.attacco)

    def __str__(self):
        stringa = super().__str__()
        stringa += f"Attacco: {self.attacco}"
        return stringa

class Shield(Item):

    difesa= 0

    def __init__(self, nome, costo_vendita, difesa):
        super().__init__(nome, costo_vendita)
        self.difesa= difesa

    def __str__(self):
        stringa= super().__str__()
        stringa += f"Difesa: {self.difesa}"
        return stringa

class Armor(Item):

    difesa = 0

    def __init__(self, nome, costo_vendita, difesa):
        super().__init__(nome, costo_vendita)
        self.difesa = difesa

    def __str__(self):
        stringa = super().__str__()
        stringa += f"Difesa: {self.difesa}"
        return stringa


