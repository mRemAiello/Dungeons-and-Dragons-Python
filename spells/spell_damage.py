from spells.spell import BaseSpell
from misc.dice import dx

# Esempi di Magie

# Affondo Mentale I
# Questo attacco infligge 1d6 danni per livello dell'incantatore (massimo 5d6).
# Il bersaglio riceve un Tiro Salvezza su Volontà per dimezzare il danno.
# Questo attacco non ha effetto su creature senza un punteggio di Intelligenza.

# Dardo Incantato (Mitico)
# Un dardo di energia magica scaturisce dalle proprie dita e colpisce il bersaglio, infliggendo 2d4+1 danni da forza.
# Il dardo non manca mai il bersaglio anche se quest'ultimo è in mischia oppure beneficia di una copertura o di un Occultamento inferiore a totale.
# Non possono essere colpite parti specifiche di una creature. Questo incantesimo non è in grado di danneggiare oggetti inanimati.
# Ogni 2 livelli dell'incantatore oltre il 1°, si ottiene un ulteriore dardo: 2 al 3° livello, 3 al 5°, 4 al 7°
# fino a un massimo di 5 al 9° livello e oltre.
# Se si è in grado di lanciare più dardi, si può decidere che colpiscano una o più creature.
# Un dardo singolo può colpire una sola creatura. Bisogna designare i bersagli prima di tirare per la Resistenza agli Incantesimi o per i danni.
# Il dardo oltrepassa l'incantesimo Scudo ed altri effetti simili che bloccano la versione non mitica di questo incantesimo.


class SpellDamage(BaseSpell):

    # Questo è il danno fisso, ad esempio nel Dardo Incantanto indica il +1 alla fine (2d4 + 1)
    fixed_damage = 0
    # Questo è il dado da lanciare (ex. Dardo Incantanto d4)
    dice = 0
    # Questo è QUANTE volte lanci il dado (ex. Dardo incantato 2 volte)
    dice_launch = 0

    def __init__(self, name, level, description, school, fixed_damage, dice, dice_launch):
        super().__init__(name, level, description, school)
        self.fixed_damage = fixed_damage
        self.dice = dice
        self.dice_launch = dice_launch

    def launch(self, invoker, target):
        damage = self.fixed_damage
        i = 0
        while i < self.dice_launch:
            damage += dx(self.dice)
            i = i + 1
        target.take_damage(invoker, damage)

    def __str__(self):
        ret = super().__str__() + f"\nInfligge {self.dice_launch}D{self.dice}"
        if self.fixed_damage > 0:
            ret += f"+{self.fixed_damage}"
        ret += " danni al bersaglio"
        return ret