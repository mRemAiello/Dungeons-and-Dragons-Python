from dado import d12


class Barbarian:

    def get_die(self):
        return d12()

    def get_coins(self):
        i = 0
        coins = 0
        while i < 3:
            coins += self.get_die()
            i += 1
        return coins

    def get_name(self):
        return "Barbarian"
