from gameplay.character import Character


class Enemy(Character):

    def handle_attack(self, target):
        if self.have_weapon():
            self.melee_attack(target)
        elif self.have_ranged_weapon():
            self.ranged_attack(target)
        else:
            # Danno a mani nude, da fare
            self.melee_attack(target)

    """experience_reward = 0

    def populate_inventory(self, items: Iterable[it.Item]) -> None:
        for item in items:
            self.add_item(item)

    def set_experience_reward(self, experience: int) -> None:
        if experience <= 0:
            print("Experience must be greater than 0")
            return
        self.experience_reward = experience

    def set_coin_reward(self, coins: int) -> None:
        if coins <= 0:
            print("Coins must be greater than 0")
            return
        self.coins = coins

    def die(self, attacker: Character) -> None:
        for item in self.inventory:
            attacker.add_item(item)
        attacker.gain_experience(self.experience_reward)
        attacker.earn_coins(self.coins)"""
