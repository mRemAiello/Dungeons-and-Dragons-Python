from spells.spell import BaseSpell
from misc.dice import dx


# Appoggiando la mano su una creatura vivente, si infonde energia positiva che cura 3d8 danni +1 danno
# per livello dell’incantatore (massimo +15).
# Dal momento che i Non Morti sono animati da energia negativa, questo incantesimo infligge loro danni piuttosto
# che curare le loro ferite.
# Una creatura Non Morta può applicare la sua Resistenza agli Incantesimi,
# e tentare un Tiro Salvezza su Volontà per dimezzare i danni subiti.

# TODO: Qualora il target sia un non morto, la magia infligge danni

# TODO: Scalare in base al livello dell'incantatore (e inserire un massimo)
# TODO: il livello del personaggio e il livello incantatore sono diversi
# TODO: Un personaggio può essere livello 20 ma avere 19 livelli Rogue e 1 Invocazione.
# TODO: In quel caso, avrebbe livello incantatore 1

class SpellHeal(BaseSpell):

    # Questo è il danno fisso, ad esempio nel Dardo Incantanto indica il +1 alla fine (2d4 + 1)
    fixed_heal = 0
    # Questo è il massimo bonus fisso che posso avere. Ex. livello inc. 20 dovrebbe curare 20 ma si ferma a +15
    max_fixed_heal = 0
    # Questo è il dado da lanciare (ex. Dardo Incantanto d4)
    dice = 0
    # Questo è QUANTE volte lanci il dado (ex. Dardo incantato 2 volte)
    dice_launch = 0

    def __init__(self, name, level, description, school, fixed_heal, max_fixed_heal, dice, dice_launch):
        super().__init__(name, level, description, school)
        self.fixed_heal = fixed_heal
        self.max_fixed_heal = max_fixed_heal
        self.dice = dice
        self.dice_launch = dice_launch

    def launch(self, invoker, target):
        heal = min(self.fixed_heal * invoker.get_level(), self.max_fixed_heal)
        i = 0
        while i < self.dice_launch:
            heal += dx(self.dice)
            i = i + 1
        target.heal(invoker, heal)

    def __str__(self):
        ret = super().__str__() + f"\nCura {self.dice_launch}D{self.dice}"
        if self.fixed_heal > 0:
            ret += f"+{self.fixed_heal}"
        ret += " PV al bersaglio"
        return ret