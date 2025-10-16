from spells.spell import BaseSpell

# Esempi di Magie

# Armatura Magica
# Un campo di forza invisibile ma tangibile circonda il soggetto dell'incantesimo,
# garantendogli Bonus di Armatura +4 alla CA.

# TODO: Questa classe andrebbe generalizzata per gestire più bonus insieme
# TODO: Attualmente ne gestisce solo uno, ed è pure specifico (CA)

# TODO: Andrebbe inserito un sistema di Buff, con una lista che contiene tutti i buff
# TODO: Ed eventualmente controllare i buff, annullarli, impilarli ecc.


class SpellBonusCA(BaseSpell):

    # Questo è il bonus alla CA
    bonus_ca = 0

    def __init__(self, name, level, description, school, bonus_ca):
        super().__init__(name, level, description, school)
        self.bonus_ca = bonus_ca

    def launch(self, invoker, target):
        bonus = target.get_bonus_ca() + self.bonus_ca
        target.set_bonus_ca(bonus)

    def __str__(self):
        ret = super().__str__() + f"\nAggiunge un bonus di {self.bonus_ca} alla CA"
        return ret