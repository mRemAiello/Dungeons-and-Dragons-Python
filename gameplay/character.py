import random
from typing import Any
from misc.dice import d20
from items.item import Item
from items.ranged_weapon import RangedWeapon
from items.weapon import Weapon
from items.armor import Armor
from items.shield import Shield


class Character:

    def __init__(self, name: str, char_race: Any, char_class: Any) -> None:
        self.__name = name
        self.__strength = 0
        self.__dexterity = 0
        self.__constitution = 0
        self.__intelligence = 0
        self.__wisdom = 0
        self.__charisma = 0
        self.__level = 1
        self.__cur_exp = 0
        self.__current_hit_points = 0
        self.__max_hit_points = 0

        #
        self.__char_race = char_race
        self.__char_class = char_class
        self.__inventory = []
        self.__melee_weapon = None
        self.__ranged_weapon = None
        self.__shield = None
        self.__armor = None

        #
        self.coins = char_class.get_coins()
        self.assign_points()

    def get_name(self):
        return self.__name

    def have_weapon(self):
        return self.__melee_weapon is not None

    def have_ranged_weapon(self):
        return self.__ranged_weapon is not None

    def assign_points(self, bonus_points: int = 30) -> None:
        # Base Stats
        self.__strength = 8 + self.__char_race.get_strength()
        self.__dexterity = 8 + self.__char_race.get_dexterity()
        self.__constitution = 8 + self.__char_race.get_constitution()
        self.__intelligence = 8 + self.__char_race.get_intelligence()
        self.__wisdom = 8 + self.__char_race.get_wisdom()
        self.__charisma = 8 + self.__char_race.get_charisma()

        # Bonus
        if bonus_points > 30:
            bonus_points = 30
        while bonus_points > 0:
            roll = random.randint(1, 6)
            if roll == 1:
                self.__strength += 1
            elif roll == 2:
                self.__dexterity += 1
            elif roll == 3:
                self.__constitution += 1
            elif roll == 4:
                self.__intelligence += 1
            elif roll == 5:
                self.__wisdom += 1
            elif roll == 6:
                self.__charisma += 1
            bonus_points -= 1

        # HP
        self.__max_hit_points = self.calculate_max_hp()
        self.__current_hit_points = self.__max_hit_points

    def calculate_max_hp(self):
        hp = self.__char_class.get_base_hp()
        hp += self.__char_class.get_hp_for_level_up() * (self.__level - 1)
        hp += self.__constitution
        return hp

    def gain_experience(self, exp_points: int) -> None:
        self.__cur_exp += exp_points
        while self.__cur_exp >= self.get_experience_to_level_up():
            self.__cur_exp -= self.get_experience_to_level_up()
            self.level_up()

    def get_experience_to_level_up(self) -> int:
        return int(100 * self.__level * (self.__level + 1) / 2)

    def level_up(self) -> None:
        self.__level += 1

        # HP
        self.__max_hit_points = self.calculate_max_hp()
        self.__current_hit_points = self.__max_hit_points

        #
        print(f"{self.__name} ha raggiunto il livello {self.__level}\n\n")

    def earn_coins(self, coins: int) -> None:
        if coins < 0:
            print("Le monete da aggiungere non possono essere minori di 0\n\n")
            return
        self.coins += coins

    def add_item(self, item: Item) -> None:
        self.__inventory.append(item)
        print(f"L'oggetto {item.name} è stato aggiunto all'inventario di {self.__name}\n\n")

    def sell_item(self, item: Item) -> None:
        if item in self.__inventory:
            self.__inventory.remove(item)
            self.coins += item.sale_cost

    def buy_item(self, item: Item) -> None:
        purchase_cost = getattr(item, "purchase_cost", item.sale_cost)
        if self.coins >= purchase_cost:
            self.__inventory.append(item)
            self.coins -= purchase_cost

    def equip_item(self, item: Item) -> None:
        self.add_item(item)
        if isinstance(item, Weapon):
            self.__melee_weapon = item
        if isinstance(item, RangedWeapon):
            self.__ranged_weapon = item
        if isinstance(item, Shield):
            self.__shield = item
        if isinstance(item, Armor):
            self.__armor = item

    def attack(self, target: "Character", base_damage: int, weapon: Weapon, bonus: int, ) -> None:
        if self.is_dead():
            return

        if target.is_dead():
            print("Il bersaglio è morto, non puoi attaccare")
            return

        if weapon is None:
            print(f"{self.__name} non ha nessuna arma equipaggiata")
            return

        if self.attack_hits(target, bonus):
            damage = base_damage
            damage += weapon.attack
            print(f"Colpito {target.get_name()} per {damage} danni da {self.__name}")
            target.take_damage(self, damage)
        else:
            print("Attacco fallito")

    def melee_attack(self, target: "Character") -> None:
        self.attack(target, self.__strength, self.__melee_weapon, self.__strength)

    def ranged_attack(self, target: "Character") -> None:
        self.attack(target, self.__dexterity, self.__ranged_weapon, self.__dexterity)

    def attack_hits(self, target: "Character", bonus: int) -> bool:
        roll = d20()
        if roll == 1:
            return False
        if roll == 20:
            return True
        if 1 < roll < 20:
            if roll + self.__level + bonus > target.get_armor_class():
                return True
        return False

    def get_armor_class(self) -> int:
        armor_class = 5 + (self.__dexterity / 2)
        if self.__armor is not None:
            armor_class += self.__armor.defense
        if self.__shield is not None:
            armor_class += self.__shield.defense
        return int(armor_class)

    def take_damage(self, attacker: "Character", damage: int) -> None:
        self.__current_hit_points -= damage
        if self.__current_hit_points <= 0:
            self.__current_hit_points = 0
            self.die(attacker)

    def die(self, attacker: "Character") -> None:
        print(f"{self.__name} ucciso {attacker.__name}")

    def is_dead(self) -> bool:
        if self.__current_hit_points <= 0:
            return True
        return False

    def observe(self, difficulty: int) -> bool:
        total = 2 + self.__wisdom + d20()
        if total > difficulty:
            return True
        return False

    def listen(self, difficulty: int) -> bool:
        total = 2 + self.__charisma + d20()
        if total > difficulty:
            return True
        return False

    def __str__(self) -> str:
        description = f"--- Character {self.__name} ---\n"
        description += f"Race: {self.__char_race.get_name()}, Class: {self.__char_class.get_name()} "
        description += f"(Level {self.__level}, Experience: {self.__cur_exp}/{self.get_experience_to_level_up()})\n"

        # Stats
        description += f"HP: {self.__current_hit_points}/{self.__max_hit_points}, CA: {self.get_armor_class()}\n"
        description += f"STR: {self.__strength}, DEX: {self.__dexterity}, CON: {self.__constitution}, "
        description += f"INT: {self.__intelligence}, WIS: {self.__wisdom}, CHA: {self.__charisma}\n"

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
