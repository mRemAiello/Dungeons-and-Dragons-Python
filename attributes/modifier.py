class Modifier:

    __owner = None
    _value_modifier = 0

    def __init__(self, owner, value):
        self.__owner = owner
        self._value_modifier = value

    def get_value_modifier(self):
        return self._value_modifier

    def calculate_attribute(self, current_value):
        return current_value

    def __str__(self):
        ret = f"+{self._value_modifier}"
        if self._value_modifier < 0:
            ret = f"{self._value_modifier}"
        return f"- {self.__owner} {ret}"