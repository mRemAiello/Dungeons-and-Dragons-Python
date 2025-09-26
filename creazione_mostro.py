import random
from scelta_oggetto import scegli_oggetto
from scelta_classe import scegli_classe
from scelta_razza import scegli_razza
from mostro import Mostro

def crea_mostro(nome):
    razza_mostro = int(random.uniform(1, 4))
    razza= scegli_razza(razza_mostro)
    classe_mostro= int(random.uniform(1, 4))
    classe= scegli_classe(classe_mostro)
    mostro= Mostro(nome, razza, classe)
    numero = int(random.uniform(1, 4))
    oggetto= scegli_oggetto(numero)
    mostro.equip_item(oggetto)
    return mostro