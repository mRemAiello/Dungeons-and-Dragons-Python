from math import floor
from attributes.vital import Vital


class Health(Vital):

    def __init__(self, name: str, base_value: int, min_value: int = 1, max_value: int = 100, character=None):
        super().__init__(name, base_value, min_value, max_value)
        self.__character = character

    def get_current_max_value(self):

        # Valore base (dato dalla classe iniziale)
        current_value = self.get_base_value()

        # Potenziamenti dati da livello / costituzione / classe
        current_value += self.__character.get_char_class().get_hp_for_level_up() * (self.__character.get_level() - 1)
        current_value += self.__character.constitution.get_current_value()

        # Dopo
        current_value = self.apply_modifiers(current_value)
        current_value = self.clamp(current_value)
        return floor(current_value)
