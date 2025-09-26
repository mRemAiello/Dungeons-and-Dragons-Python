from dado import d6


class Thief:

    def get_die(self):
        return d6()

    def get_coins(self):
        i = 0
        coins = 0
        while i < 4:
            coins += self.get_die()
            i += 1
        return coins

    def get_name(self):
        return "Thief"
