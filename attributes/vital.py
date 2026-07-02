from math import floor
from attributes.attribute import Attribute


class Vital(Attribute):

    __current_value = 1

    def __init__(self, name: str, base_value: int, min_value: int = 1, max_value: int = 100):
        super().__init__(name, base_value, min_value, max_value)
        self.__current_value = 1

    def heal(self, value):
        if value <= 0:
            print("Il valore non può essere negativo o nullo")
            return

        self.__current_value = self.clamp(self.get_current_value() + value) / self.get_current_max_value()

    def consume(self, value):
        if value <= 0:
            print("Il valore non può essere negativo o nullo")
            return

        self.__current_value = self.clamp(self.get_current_value() - value) / self.get_current_max_value()

    def get_current_value(self):
        return floor(self.__current_value * self.get_current_max_value())

    def get_current_max_value(self):
        current_value = self.get_base_value()
        current_value = self.apply_modifiers(current_value)
        current_value = self.clamp(current_value)
        return floor(current_value)

    def __str__(self):
        ret = f"{self.get_name()}: {self.get_current_value()} / {self.get_current_max_value()} ({self.get_base_value()})\n"
        for modifier in self.get_modifiers():
            ret += modifier.__str__() + "\n"
        return ret