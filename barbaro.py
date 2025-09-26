from dado import d12

class Barbaro:

    def get_dado(self):
        return d12()

    def get_monete(self):
        i= 0
        monete= 0
        while i < 3:
            monete += self.get_dado()
            i+= 1
        return monete

    def get_nome(self):
        return "Barbaro"

