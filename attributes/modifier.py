class Modifier:

    __owner = None
    __value = 0

    def __init__(self, owner, value):
        self.__owner = owner
        self.__value = value

    def get_value_modifier(self):
        return self.__value

    def calculate_attribute(self, current_value):
        return current_value

    def __str__(self):
        ret = f"+{self.__value}"
        if self.__value < 0:
            ret = f"{self.__value}"
        return f"- {self.__owner.get_name()} {ret}"