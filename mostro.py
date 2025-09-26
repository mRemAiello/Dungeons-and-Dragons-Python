import personaggio as pg

class Mostro(pg.Personaggio):

    exp= 0

    def inventario_mostro(self, items):
        for item in items:
            self.add_item(item)

    def exp_mostro(self, exp):
        if exp <= 0:
            print("L'esperienza è minore di 0")
            return
        self.exp= exp

    def monete_mostro(self, moneta):
        if moneta <= 0:
            print("Le monete sono minori di 0")
            return
        self.moneta= moneta

    def death(self, attaccante):
        for item in self.inventario:
            attaccante.add_item(item)
        attaccante.guadagna_esperienza(self.exp)
        attaccante.guadagna_monete(self.moneta)