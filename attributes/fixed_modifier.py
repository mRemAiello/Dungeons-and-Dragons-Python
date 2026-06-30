from attributes.modifier import Modifier


class FixedModifier(Modifier):

    def calculate_attribute(self, current_value):
        return current_value + self._value_modifier
