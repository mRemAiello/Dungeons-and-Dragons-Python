class BaseClass:

    # Nome della classe (Da sovrascrivere nelle sottoclassi)
    def get_name(self):
        return ""

    # Lancia il base in base al dado impostato dalla classe (es. Rogue avrà d6, Barbaro d12 ecc)
    # (Da sovrascrivere nelle sottoclassi)
    def roll_dice(self):
        return 0

    # Hp di base della classe
    # (Da sovrascrivere nelle sottoclassi)
    def get_base_hp(self):
        return 0

    # Hp che ottiene il personaggio per ogni level up
    # (Da sovrascrivere nelle sottoclassi)
    def get_hp_for_level_up(self):
        return 0

    # Numero di lanci che deve fare per le monete
    # (Da sovrascrivere nelle sottoclassi)
    def get_money_dice_launches(self):
        return 0

    # Restituisce una lista di Item (armi, armature, ecc) di partenza
    def get_starting_items(self):
        return []

    # In base al dado della classe e ai lanci, mi darà le monete iniziali
    # Da lasciare così com'è, non serve che la sottoclasse sovrascriva la funzione
    # A meno che non si vogliano comportamenti particolari
    def get_coins(self):
        i = 0
        coins = 0
        while i < self.get_money_dice_launches():
            coins += self.roll_dice()
            i += 1
        return coins