from dado import d10

class Paladino:

    def get_dado(self):
        return d10()

    def get_monete(self):
        i= 0
        monete= 0
        while i < 5:
            monete += self.get_dado()
            i+= 1
        return monete

    def get_nome(self):
        return "Paladino"