from attributes.modifier import Modifier


class FixedModifier(Modifier):

    def calculate_attribute(self, current_value):
        return current_value + self.get_value_modifier()
