class BaseSpell:

    name = ""
    description = ""
    level = 0
    school = ""

    def __init__(self, name, level, description, school):
        self.name = name
        self.level = level
        self.description = description
        self.school = school

    def launch(self, invoker, target):
        return

    def __str__(self):
        ret = f"{self.name} Livello {self.level}, Scuola {self.school}\n"
        ret += f"Descrizione: {self.description}"
        return ret