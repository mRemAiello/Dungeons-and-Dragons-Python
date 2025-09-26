import barbaro
import paladino
import ladro
import mago


def choose_class(number):
    character_class = None
    if number == 1:
        character_class = barbaro.Barbarian()
    if number == 2:
        character_class = paladino.Paladin()
    if number == 3:
        character_class = ladro.Thief()
    if number == 4:
        character_class = mago.Wizard()
    if number == 0 or number > 4:
        print("The selected class number does not exist")
    return character_class
