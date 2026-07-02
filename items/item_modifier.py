from attributes.attribute import Attribute
from attributes.modifier import Modifier


class ItemModifier:

    modifier: Modifier = None
    attribute: Attribute = None

    def __init__(self, modifier, attribute):
        self.modifier = modifier
        self.attribute = attribute