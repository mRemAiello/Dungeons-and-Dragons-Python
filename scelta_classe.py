from typing import Optional, Union

import barbaro
import paladino
import ladro
import mago


CharacterClass = Union[
    barbaro.Barbarian,
    paladino.Paladin,
    ladro.Thief,
    mago.Wizard,
]


def choose_class(number: int) -> Optional[CharacterClass]:
    character_class: Optional[CharacterClass] = None
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
