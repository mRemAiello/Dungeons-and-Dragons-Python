from typing import Optional, Union

import umano
import nano
import elfo
import gnomo


Race = Union[umano.Human, nano.Dwarf, elfo.Elf, gnomo.Gnome]


def choose_race(number: int) -> Optional[Race]:
    race: Optional[Race] = None
    if number == 1:
        race = umano.Human()
    if number == 2:
        race = nano.Dwarf()
    if number == 3:
        race = elfo.Elf()
    if number == 4:
        race = gnomo.Gnome()
    if number == 0 or number > 4:
        print("The selected race number does not exist")
    return race
