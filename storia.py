import random

from dado import d6
from dado import d20
from dado import d10
from dado import d4
from scelta_oggetto import choose_item
from creazione_mostro import create_monster


def adventure(selected_character):
    roll = d6()
    if roll == 1:
        perform_observe_check(selected_character)
    if roll == 2:
        random_item(selected_character)
    if roll == 3:
        perform_listen_check(selected_character)
    if roll == 4:
        meet_boss(selected_character)
    if 4 < roll < 7:
        meet_boss(selected_character)


def perform_observe_check(selected_character):
    selected_character.observe(d20())
    if selected_character.observe(d20()):
        selected_character.gain_experience(1000)
        print("The ability succeeded and you gained 1000 exp")
        if not selected_character.observe(d20()):
            print("The ability failed")


def random_item(selected_character):
    number = int(random.uniform(1, 4))
    choose_item(number)
    item = choose_item(number)
    selected_character.add_item(item)


def perform_listen_check(selected_character):
    selected_character.listen(d10())
    if selected_character.listen(d10()):
        selected_character.earn_coins(10)
        print("The ability succeeded and you gained 10 coins")
    if not selected_character.listen(d10()):
        print("The ability failed")


def meet_monster(selected_character):
    print("You encountered a monster")
    monster = create_monster("Obelix")
    roll = d6()
    if roll == 1:
        print("Run away")
    if 2 <= roll <= 4:
        print("Your character attacks")
        selected_character.melee_attack(monster)
        selected_character.ranged_attack(monster)
    if roll > 4:
        print("The monster attacks your character")
        monster.melee_attack(selected_character)
        monster.ranged_attack(selected_character)


def meet_boss(selected_character):
    print("You encountered a boss")
    monster = create_monster("Gandalf")
    monster.gain_experience(20000)
    roll = d4()
    if 1 <= roll <= 3:
        print("Run away")
    if roll == 4:
        print("Fight")
        selected_character.melee_attack(monster)
        selected_character.ranged_attack(monster)
        monster.melee_attack(selected_character)
        monster.ranged_attack(selected_character)
