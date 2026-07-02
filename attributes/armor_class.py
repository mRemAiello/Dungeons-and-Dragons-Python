from attributes.attribute import Attribute


class ArmorClass(Attribute):

    def __init__(self, name: str, base_value: int, min_value: int = 1, max_value: int = 100, character=None):
        super().__init__(name, base_value, min_value, max_value)
        self.__character = character

    def get_current_value(self):

        # Tipicamente 5 di base
        current_value = self.get_base_value()

        # Aggiungo valori dati dalla formula
        current_value += (self.__character.dexterity.get_current_value() / 2)
        if self.__character.get_armor() is not None:
            current_value += self.__character.get_armor().defense
        if self.__character.get_shield() is not None:
            current_value += self.__character.get_shield().defense

        # Bonus di modificatori ecc
        current_value = self.apply_modifiers(current_value)
        current_value = self.clamp(current_value)
        return int(current_value)