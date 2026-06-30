from math import floor


class Attribute:

    _modifiers = []

    def __init__(self, name: str, base_value: int, min_value: int = 1, max_value: int = 100):
        self._name = name
        self._base_value = base_value
        self._min_value = min_value
        self._max_value = max_value
        self._modifiers = []

    def add_modifier(self, modifier):
        if modifier.get_value_modifier() == 0:
            return
        self._modifiers.append(modifier)

    def get_current_value(self):
        current_value = self._base_value
        # TODO: Ordinare i modificatori
        for modifier in self._modifiers:
            current_value = modifier.calculate_attribute(current_value)
        if current_value < self._min_value:
            current_value = self._min_value
        if current_value > self._max_value:
            current_value = self._max_value
        return floor(current_value)

    def __str__(self):
        ret = f"{self._name}: {self.get_current_value()} ({self._base_value})\n"
        for modifier in self._modifiers:
            ret += modifier.__str__() + "\n"
        return ret