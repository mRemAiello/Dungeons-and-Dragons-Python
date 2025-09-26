from dado import d10


class Paladin:

    def get_die(self):
        return d10()

    def get_coins(self):
        i = 0
        coins = 0
        while i < 5:
            coins += self.get_die()
            i += 1
        return coins

    def get_name(self):
        return "Paladin"
