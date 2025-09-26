import random

from dado import d20
import math
import item as it


class Personaggio:
    forza= 0
    destrezza= 0
    costituzione= 0
    intelligenza= 0
    saggezza= 0
    carisma= 0
    esperienza= 0
    livello= 1
    moneta= 0
    ps_iniziali= 0
    ps_max= 0
    ps_correnti= 0
    nome= ""
    razza= None
    classe= None
    inventario=[]
    arma= None
    arma_distanza= None
    scudo= None
    armatura= None

    def __init__(self, nome, razza, classe):
        self.moneta= classe.get_monete()
        self.nome= nome
        self.razza= razza
        self.classe= classe
        self.inventario= []
        self.arma= None
        self.arma_distanza= None
        self.scudo= None
        self.armatura= None
        self.punti()

    def punti(self, punti_bonus= 30):
        self.forza = 8 + self.razza.get_forza()
        self.destrezza = 8 + self.razza.get_destrezza()
        self.costituzione = 8 + self.razza.get_costituzione()
        self.intelligenza = 8 + self.razza.get_intelligenza()
        self.saggezza = 8 + self.razza.get_saggezza()
        self.carisma = 8 + self.razza.get_carisma()
        if punti_bonus > 30:
            punti_bonus = 30
        while punti_bonus > 0:
            lancio= random.randint(1,6)
            if lancio == 1:
                self.forza += 1
            elif lancio == 2:
                self.destrezza += 1
            elif lancio == 3:
                self.costituzione += 1
            elif lancio == 4:
                self.intelligenza += 1
            elif lancio == 5:
                self.saggezza += 1
            elif lancio == 6:
                self.carisma += 1
            punti_bonus -= 1
        self.ps_iniziali = 1 + self.classe.get_dado() + self.costituzione
        self.ps_max = self.ps_iniziali
        self.ps_correnti = self.ps_max


    def guadagna_esperienza(self, punti):
        self.esperienza += punti
        while self.esperienza >= self.esperienza_per_salire_livello():
            self.esperienza -= self.esperienza_per_salire_livello()
            self.level_up()

    def esperienza_per_salire_livello(self):
        return int(100 * self.livello * (self.livello +1)/ 2)

    def level_up(self):
        self.livello += 1
        ps_bonus= math.ceil(2 + (self.classe.get_dado()/2) + self.costituzione)
        self.ps_max += ps_bonus
        self.ps_correnti= self.ps_max

    def guadagna_monete(self, coins):
        if coins <=0:
            print("Le monete non possono essere inferiori a zero")
            return
        self.moneta += coins

    def add_item(self, item):
        self.inventario.append(item)
        print(f"Oggetto {item.nome} aggiunto all'inventario di {self.nome}")

    def sell_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
            self.moneta += item.costo_vendita

    def buy_item(self, item):
        if self.moneta >= item.costo_acquisto:
            self.inventario.append(item)
            self.moneta -= item.costo_acquisto

    def equip_item(self, item):
        self.add_item(item)
        if type(item) is it.Weapon:
            self.arma= item
        if type(item) is it.Ranged_Weapon:
            self.arma_distanza= item
        if type(item) is it.Shield:
            self.scudo= item
        if type(item) is it.Armor:
            self.armatura= item

    def attacco(self, bersaglio, danno_base, arma_personaggio, bonus):
        if self.is_death():
            print()
            return
        if bersaglio.is_death():
            print("IL bersaglio è morto, non puoi più colpirlo")
            return
        if arma_personaggio is None:
            print(f"{self.nome} non hai l'arma")
            return
        if self.attacco_a_segno(bersaglio, bonus):
            danno= danno_base
            danno += arma_personaggio.attacco
            print(f"Colpito {bersaglio.nome} per {danno} danni da {self.nome}")
            bersaglio.take_damage(self, danno)
        else:
            print("Attacco fallito")

    def attacco_ravvicinato(self, bersaglio):
        self.attacco(bersaglio, self.forza, self.arma, self.forza)
    def attacco_a_distanza(self, bersaglio):
        self.attacco(bersaglio, self.destrezza, self.arma_distanza, self.destrezza)

    def attacco_a_segno(self, bersaglio, bonus):
        x = d20()
        if x == 1:
            return False
        if x == 20:
            return True
        if 1 < x < 20:
            if x + self.livello + bonus > bersaglio.get_classe_armatura():
                return True
        return False

    def get_classe_armatura(self):
        ac= 10 + (self.destrezza/ 2)
        if self.armatura is not None:
            ac += self.armatura.difesa
        if self.scudo is not None:
            ac += self.scudo.difesa
        return ac

    def take_damage(self, attaccante, danno):
        self.ps_correnti -= danno
        if self.ps_correnti <= 0:
            self.ps_correnti= 0
            self.death(attaccante)

    def death(self, attaccante):
        print(f"{self.nome} ucciso da {attaccante.nome}")

    def is_death(self):
        if self.ps_correnti <= 0:
            return True
        return False

    def osservare(self, valore):
        totale= 2 + self.saggezza + d20()
        if totale > valore:
            return True
        return False

    def ascoltare(self, valore):
        totale = 2 + self.carisma + d20()
        if totale > valore:
            return True
        return False

    def __str__(self):
        stringa=f"Nome: {self.nome}, Razza: {self.razza.get_nome()}, Classe: {self.classe.get_nome()} (Livello {self.livello})\n"
        stringa +=f"Forza: {self.forza}, Destrezza: {self.destrezza}, Costituzione: {self.costituzione}, "
        stringa+=f"Intelligenza: {self.intelligenza}, Saggezza: {self.saggezza}, Carisma: {self.carisma}\n"
        stringa+=f"Esperienza: {self.esperienza}/{self.esperienza_per_salire_livello()}, Monete: {self.moneta}, "
        stringa +=f"PS correnti: {self.ps_correnti}/{self.ps_max}\n"
        stringa+=f"Equipaggiamento:\n"
        stringa +=f"{self.arma}\n{self.arma_distanza}\n{self.armatura}\n{self.scudo}\n"
        stringa += f"Inventario: \n"
        for item in self.inventario:
            stringa += item.__str__() + "\n"
        return stringa













