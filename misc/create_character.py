from misc.create_race import create_new_race
from misc.create_class import create_new_class
from gameplay.character import Character
from gameplay.enemy import Enemy
import random


def create_new_character(name, race_number, class_number):

    char_race = create_new_race(race_number)
    char_class = create_new_class(class_number)
    character = Character(name, char_race, char_class)

    # Equipaggia oggetti
    for item in char_class.get_starting_items():
        character.equip_item(item)

    return character


def create_new_random_character(name):

    race_number = int(random.uniform(0, 4))
    class_number = int(random.uniform(0, 5))
    character = create_new_character(name, race_number, class_number)
    return character


def create_new_enemy(name, race_number, class_number):
    char_race = create_new_race(race_number)
    char_class = create_new_class(class_number)
    enemy = Enemy(name, char_race, char_class)

    # Equipaggia oggetti
    for item in char_class.get_starting_items():
        enemy.equip_item(item)

    return enemy


def create_new_random_enemy(name):
    race_number = int(random.uniform(0, 4))
    class_number = int(random.uniform(0, 5))
    enemy = create_new_enemy(name, race_number, class_number)
    return enemy