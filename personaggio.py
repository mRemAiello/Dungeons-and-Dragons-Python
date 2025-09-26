from __future__ import annotations

import random
import math
from typing import Any, Iterable, Optional, Union

from dado import d20
import item as it

InventoryItems = Iterable[it.Item]
CharacterWeapon = Optional[Union[it.Weapon, it.RangedWeapon]]


class Character:

    def __init__(self, name: str, race: Any, character_class: Any) -> None:
        self.coins = character_class.get_coins()
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.inventory: list[it.Item] = []
        self.melee_weapon: Optional[it.Weapon] = None
        self.ranged_weapon: Optional[it.RangedWeapon] = None
        self.shield: Optional[it.Shield] = None
        self.armor: Optional[it.Armor] = None
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.initial_hit_points = 0
        self.max_hit_points = 0
        self.current_hit_points = 0
        self.assign_points()

    def assign_points(self, bonus_points: int = 30) -> None:
        self.strength = 8 + self.race.get_strength()
        self.dexterity = 8 + self.race.get_dexterity()
        self.constitution = 8 + self.race.get_constitution()
        self.intelligence = 8 + self.race.get_intelligence()
        self.wisdom = 8 + self.race.get_wisdom()
        self.charisma = 8 + self.race.get_charisma()
        if bonus_points > 30:
            bonus_points = 30
        while bonus_points > 0:
            roll = random.randint(1, 6)
            if roll == 1:
                self.strength += 1
            elif roll == 2:
                self.dexterity += 1
            elif roll == 3:
                self.constitution += 1
            elif roll == 4:
                self.intelligence += 1
            elif roll == 5:
                self.wisdom += 1
            elif roll == 6:
                self.charisma += 1
            bonus_points -= 1
        self.initial_hit_points = 1 + self.character_class.get_die() + self.constitution
        self.max_hit_points = self.initial_hit_points
        self.current_hit_points = self.max_hit_points

    def gain_experience(self, points: int) -> None:
        self.experience += points
        while self.experience >= self.experience_to_level_up():
            self.experience -= self.experience_to_level_up()
            self.level_up()

    def experience_to_level_up(self) -> int:
        return int(100 * self.level * (self.level + 1) / 2)

    def level_up(self) -> None:
        self.level += 1
        bonus_hit_points = math.ceil(2 + (self.character_class.get_die() / 2) + self.constitution)
        self.max_hit_points += bonus_hit_points
        self.current_hit_points = self.max_hit_points

    def earn_coins(self, coins: int) -> None:
        if coins <= 0:
            print("Coins cannot be less than zero")
            return
        self.coins += coins

    def add_item(self, item: it.Item) -> None:
        self.inventory.append(item)
        print(f"Item {item.name} added to {self.name}'s inventory")

    def sell_item(self, item: it.Item) -> None:
        if item in self.inventory:
            self.inventory.remove(item)
            self.coins += item.sale_cost

    def buy_item(self, item: it.Item) -> None:
        purchase_cost = getattr(item, "purchase_cost", item.sale_cost)
        if self.coins >= purchase_cost:
            self.inventory.append(item)
            self.coins -= purchase_cost

    def equip_item(self, item: it.Item) -> None:
        self.add_item(item)
        if isinstance(item, it.Weapon):
            self.melee_weapon = item
        if isinstance(item, it.RangedWeapon):
            self.ranged_weapon = item
        if isinstance(item, it.Shield):
            self.shield = item
        if isinstance(item, it.Armor):
            self.armor = item

    def attack(
        self,
        target: "Character",
        base_damage: int,
        character_weapon: CharacterWeapon,
        bonus: int,
    ) -> None:
        if self.is_dead():
            print()
            return
        if target.is_dead():
            print("The target is dead, you cannot hit it anymore")
            return
        if character_weapon is None:
            print(f"{self.name} you do not have the weapon equipped")
            return
        if self.attack_hits(target, bonus):
            damage = base_damage
            damage += character_weapon.attack
            print(f"Hit {target.name} for {damage} damage from {self.name}")
            target.take_damage(self, damage)
        else:
            print("Attack missed")

    def melee_attack(self, target: "Character") -> None:
        self.attack(target, self.strength, self.melee_weapon, self.strength)

    def ranged_attack(self, target: "Character") -> None:
        self.attack(target, self.dexterity, self.ranged_weapon, self.dexterity)

    def attack_hits(self, target: "Character", bonus: int) -> bool:
        roll = d20()
        if roll == 1:
            return False
        if roll == 20:
            return True
        if 1 < roll < 20:
            if roll + self.level + bonus > target.get_armor_class():
                return True
        return False

    def get_armor_class(self) -> float:
        armor_class = 10 + (self.dexterity / 2)
        if self.armor is not None:
            armor_class += self.armor.defense
        if self.shield is not None:
            armor_class += self.shield.defense
        return armor_class

    def take_damage(self, attacker: "Character", damage: int) -> None:
        self.current_hit_points -= damage
        if self.current_hit_points <= 0:
            self.current_hit_points = 0
            self.die(attacker)

    def die(self, attacker: "Character") -> None:
        print(f"{self.name} killed by {attacker.name}")

    def is_dead(self) -> bool:
        if self.current_hit_points <= 0:
            return True
        return False

    def observe(self, difficulty: int) -> bool:
        total = 2 + self.wisdom + d20()
        if total > difficulty:
            return True
        return False

    def listen(self, difficulty: int) -> bool:
        total = 2 + self.charisma + d20()
        if total > difficulty:
            return True
        return False

    def __str__(self) -> str:
        description = (
            f"Name: {self.name}, Race: {self.race.get_name()}, Class: {self.character_class.get_name()} "
            f"(Level {self.level})\n"
        )
        description += (
            f"Strength: {self.strength}, Dexterity: {self.dexterity}, Constitution: {self.constitution}, "
        )
        description += (
            f"Intelligence: {self.intelligence}, Wisdom: {self.wisdom}, Charisma: {self.charisma}\n"
        )
        description += (
            f"Experience: {self.experience}/{self.experience_to_level_up()}, Coins: {self.coins}, "
        )
        description += f"Current HP: {self.current_hit_points}/{self.max_hit_points}\n"
        description += "Equipment:\n"
        description += f"{self.melee_weapon}\n{self.ranged_weapon}\n{self.armor}\n{self.shield}\n"
        description += "Inventory: \n"
        inventory_items: InventoryItems = self.inventory
        for item in inventory_items:
            description += item.__str__() + "\n"
        return description
