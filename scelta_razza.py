import umano
import nano
import elfo
import gnomo


def choose_race(number):
    race = None
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
