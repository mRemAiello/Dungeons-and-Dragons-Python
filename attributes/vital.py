from math import floor
from attributes.attribute import Attribute


class Vital(Attribute):

    __current_value = 1

    def __init__(self, name: str, base_value: int, min_value: int = 1, max_value: int = 100):
        super().__init__(name, base_value, min_value, max_value)
        self.__current_value = 1

    def consume(self, value):
        if value <= 0:
            return

        current_value = self.get_current_value() - value
        if current_value < self._min_value:
            current_value = self._min_value
        if current_value > self.get_current_max_value():
            current_value = self.get_current_max_value()

        self.__current_value = current_value / self.get_current_max_value()

    def get_current_value(self):
        return floor(self.__current_value * self.get_current_max_value())

    def get_current_max_value(self):
        return super().get_current_value()