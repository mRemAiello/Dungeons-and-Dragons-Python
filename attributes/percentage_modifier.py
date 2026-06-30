from attributes.modifier import Modifier


class PercentageModifier(Modifier):

    def calculate_attribute(self, current_value):
        return current_value + (current_value * self._value_modifier / 100)

    def __str__(self):
        return super().__str__() + "%"