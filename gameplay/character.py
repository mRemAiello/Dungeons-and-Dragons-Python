import random
from typing import Any

from attributes.armor_class import ArmorClass
from attributes.attribute import Attribute
from attributes.fixed_modifier import FixedModifier
from attributes.health import Health
from misc.dice import d20
from items.item import Item
from items.ranged_weapon import RangedWeapon
from items.weapon import Weapon
from items.armor import Armor
from items.shield import Shield


class Character:

    strength = None
    dexterity = None
    constitution = None
    intelligence = None
    wisdom = None
    charisma = None
    hp = None
    armor_class = None

    def __init__(self, name: str, char_race: Any, char_class: Any) -> None:
        #
        self.__char_race = char_race
        self.__char_class = char_class
        self.__inventory = []
        self.__melee_weapon = None
        self.__ranged_weapon = None
        self.__shield = None
        self.__armor = None

        # Attributi
        self.name = name
        self.level = 1
        self.current_exp = 0
        self.hp = Health("HP", self.__char_class.get_base_hp(), 0, 9999, self)
        self.armor_class = ArmorClass("AC", 5, 0, 9999, self)

        #
        self.coins = char_class.get_coins()
        self.assign_points()

    def get_name(self):
        return self.name

    def get_char_class(self):
        return self.__char_class

    def get_armor(self):
        return self.__armor

    def get_shield(self):
        return self.__shield

    def have_weapon(self):
        return self.__melee_weapon is not None

    def have_ranged_weapon(self):
        return self.__ranged_weapon is not None

    def assign_points(self, bonus_points: int = 30) -> None:

        # Base Stats
        self.strength = Attribute("Forza", 8, 1, 99)
        self.dexterity = Attribute("Destrezza", 8, 1, 99)
        self.constitution = Attribute("Costituzione", 8, 1, 99)
        self.intelligence = Attribute("Intelligenza", 8, 1, 99)
        self.wisdom = Attribute("Saggezza", 8, 1, 99)
        self.charisma = Attribute("Carisma", 8, 1, 99)

        # Bonus derivanti da classi / razze
        race_name = self.__char_race.get_name()
        self.strength.add_modifier(FixedModifier(race_name, self.__char_race.get_strength()))
        self.dexterity.add_modifier(FixedModifier(race_name, self.__char_race.get_dexterity()))
        self.constitution.add_modifier(FixedModifier(race_name, self.__char_race.get_constitution()))
        self.intelligence.add_modifier(FixedModifier(race_name, self.__char_race.get_intelligence()))
        self.wisdom.add_modifier(FixedModifier(race_name, self.__char_race.get_wisdom()))
        self.charisma.add_modifier(FixedModifier(race_name, self.__char_race.get_charisma()))

        #
        self.assign_bonus_points(bonus_points)

    def assign_bonus_points(self, bonus_points: int = 30):
        # Bonus
        strength = 0
        dexterity = 0
        intelligence = 0
        constitution = 0
        wisdom = 0
        charisma = 0
        if bonus_points > 30:
            bonus_points = 30
        while bonus_points > 0:
            roll = random.randint(1, 6)
            if roll == 1:
                strength += 1
            elif roll == 2:
                dexterity += 1
            elif roll == 3:
                constitution += 1
            elif roll == 4:
                intelligence += 1
            elif roll == 5:
                wisdom += 1
            elif roll == 6:
                charisma += 1
            bonus_points -= 1

        self.strength.add_modifier(FixedModifier("Bonus Points", strength))
        self.dexterity.add_modifier(FixedModifier("Bonus Points", dexterity))
        self.intelligence.add_modifier(FixedModifier("Bonus Points", intelligence))
        self.constitution.add_modifier(FixedModifier("Bonus Points", constitution))
        self.wisdom.add_modifier(FixedModifier("Bonus Points", wisdom))
        self.charisma.add_modifier(FixedModifier("Bonus Points", charisma))

    def get_level(self):
        return self.level

    def gain_experience(self, exp_points: int) -> None:
        self.current_exp += exp_points
        while self.current_exp >= self.get_experience_to_level_up():
            self.current_exp -= self.get_experience_to_level_up()
            self.level_up()

    def get_experience_to_level_up(self) -> int:
        return int(100 * self.level * (self.level + 1) / 2)

    def level_up(self, show_print=False) -> None:
        self.level += 1

        #
        if show_print:
            print(f"{self.name} ha raggiunto il livello {self.level}\n")

    def earn_coins(self, coins: int) -> None:
        if coins < 0:
            print("Le monete da aggiungere non possono essere minori di 0\n")
            return
        self.coins += coins

    def add_item(self, item: Item, show_print=False) -> None:
        self.__inventory.append(item)
        if show_print:
            print(f"L'oggetto {item.name} è stato aggiunto all'inventario di {self.name}\n")

    def sell_item(self, item: Item) -> None:
        if item in self.__inventory:
            self.__inventory.remove(item)
            self.coins += item.sale_cost

    def buy_item(self, item: Item) -> None:
        purchase_cost = getattr(item, "purchase_cost", item.sale_cost)
        if self.coins >= purchase_cost:
            self.__inventory.append(item)
            self.coins -= purchase_cost

    # TODO: Fixare le chiamate
    def equip_item(self, item: Item) -> None:
        self.add_item(item)
        if isinstance(item, Weapon):
            self.__melee_weapon = item
            self.__melee_weapon.equip(self)
        if isinstance(item, RangedWeapon):
            self.__ranged_weapon = item
        if isinstance(item, Shield):
            self.__shield = item
        if isinstance(item, Armor):
            self.__armor = item

    def heal(self, healer: "Character", value: int):
        # Niente da fare se il curatore o il bersaglio sono morti
        if self.is_dead() or healer.is_dead():
            return

        # Cura non valida o nulla
        if value <= 0:
            return

        # Applica la cura
        self.hp.heal(value)
        print(f"{healer.get_name()} cura {self.get_name()} di {value}")

    def attack(self, target: "Character", base_damage: int, weapon: Weapon, bonus: int) -> None:
        if self.is_dead():
            return

        if target.is_dead():
            print("Il bersaglio è morto, non puoi attaccare\n")
            return

        if weapon is None:
            print(f"{self.name} non ha nessuna arma equipaggiata\n")
            return

        if self.attack_hits(target, bonus):
            damage = base_damage
            damage += weapon.attack
            target.take_damage(self, damage)
        else:
            print("Attacco fallito")

    def melee_attack(self, target: "Character") -> None:
        str_value = self.strength.get_current_value()
        self.attack(target, str_value, self.__melee_weapon, str_value)

    def ranged_attack(self, target: "Character") -> None:
        dex_value = self.dexterity.get_current_value()
        self.attack(target, dex_value, self.__ranged_weapon, dex_value)

    def attack_hits(self, target: "Character", bonus: int) -> bool:
        roll = d20()
        if roll == 1:
            return False
        if roll == 20:
            return True
        if 1 < roll < 20:
            if roll + self.level + bonus > target.armor_class.get_current_value():
                return True
        return False

    def take_damage(self, attacker: "Character", damage: int) -> None:
        print(f"{attacker.get_name()} colpisce {self.get_name()} infliggendo {damage} danni")
        self.hp.consume(damage)
        if self.hp.get_current_value() <= 0:
            self.die(attacker)

    def die(self, attacker: "Character") -> None:
        print(f"{self.name} ucciso {attacker.name}")

    def is_dead(self) -> bool:
        if self.hp.get_current_value() <= 0:
            return True
        return False

    def observe(self, difficulty: int) -> bool:
        total = 2 + self.wisdom.get_current_value() + d20()
        if total > difficulty:
            return True
        return False

    def listen(self, difficulty: int) -> bool:
        total = 2 + self.charisma.get_current_value() + d20()
        if total > difficulty:
            return True
        return False

    def __str__(self) -> str:
        description = f"--- Character {self.name} ---\n"
        description += f"Race: {self.__char_race.get_name()}, Class: {self.__char_class.get_name()} "
        description += f"(Level {self.level}, Experience: {self.current_exp}/{self.get_experience_to_level_up()})\n"

        # Stats
        description += f"HP: {self.hp.get_current_value()}/{self.hp.get_current_max_value()}"
        description += f", CA: {self.armor_class.get_current_value()}\n"
        description += f"STR: {self.strength.get_current_value()}, DEX: {self.dexterity.get_current_value()}, "
        description += f"CON: {self.constitution.get_current_value()}, INT: {self.intelligence.get_current_value()}, "
        description += f"WIS: {self.wisdom.get_current_value()}, CHA: {self.charisma.get_current_value()}\n"

        # Equipaggiamento
        description += "--- Equipaggiamento ---\n"
        if self.__melee_weapon:
            description += f"Arma: {self.__melee_weapon}\n"
        if self.__ranged_weapon:
            description += f"Arma a distanza: {self.__ranged_weapon}\n"
        if self.__armor:
            description += f"Armatura: {self.__armor}\n"
        if self.__shield:
            description += f"Scudo: {self.__shield}\n"

        # Inventario
        description += "--- Inventario ---\n"
        for item in self.__inventory:
            description += item.__str__() + "\n"
        description += f"Monete: {self.coins}\n"

        return description