from classes.barbarian import Barbarian
from classes.bard import Bard
from classes.mage import Mage
from classes.paladin import Paladin
from classes.thief import Thief

# 0: Barbarian
# 1: Bard
# 2: Mage
# 3: Paladin
# 4: Thief


def create_new_class(number):
    if number == 0:
        return Barbarian()
    elif number == 1:
        return Bard()
    elif number == 2:
        return Mage()
    elif number == 3:
        return Paladin()
    elif number == 4:
        return Thief()
    return None