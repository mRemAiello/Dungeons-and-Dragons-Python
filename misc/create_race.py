from races.elf import Elf
from races.dwarf import Dwarf
from races.gnome import Gnome
from races.human import Human

# 0: Human
# 1: Elf
# 2: Dwarf
# 3: Gnome


def create_new_race(number):
    if number == 0:
        return Human()
    elif number == 1:
        return Elf()
    elif number == 2:
        return Dwarf()
    elif number == 3:
        return Gnome()
    return None