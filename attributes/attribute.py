from math import floor


class Attribute:

    __modifiers = []

    def __init__(self, name: str, base_value: int, min_value: int = 1, max_value: int = 100):
        self.__name = name
        self.__base_value = base_value
        self.__min_value = min_value
        self.__max_value = max_value
        self.__modifiers = []

    def add_modifier(self, modifier):
        if modifier.get_value_modifier() == 0:
            return
        self.__modifiers.append(modifier)

    def get_current_value(self):
        current_value = self.__base_value
        current_value = self.apply_modifiers(current_value)
        current_value = self.clamp(current_value)
        return floor(current_value)

    def clamp(self, value):
        if value < self.__min_value:
            return self.__min_value
        if value > self.__max_value:
            return self.__max_value
        return value

    def apply_modifiers(self, value):
        # TODO: Ordinare i modificatori
        for modifier in self.__modifiers:
            value = modifier.calculate_attribute(value)
        return value

    def get_name(self):
        return self.__name

    def get_modifiers(self):
        return self.__modifiers.copy()

    def get_base_value(self):
        return self.__base_value

    def get_min_value(self):
        return self.__min_value

    def get_max_value(self):
        return self.__max_value

    def __str__(self):
        ret = f"{self.__name}: {self.get_current_value()} ({self.__base_value})\n"
        for modifier in self.__modifiers:
            ret += modifier.__str__() + "\n"
        return ret