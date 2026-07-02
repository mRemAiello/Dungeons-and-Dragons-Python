from attributes.modifier import Modifier


class PercentageModifier(Modifier):

    def calculate_attribute(self, current_value):
        return current_value + (current_value * self.__value / 100)

    def __str__(self):
        return super().__str__() + "%"