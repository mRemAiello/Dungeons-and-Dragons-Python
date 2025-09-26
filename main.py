import random
from item import Weapon
from item import Ranged_Weapon
from item import Armor
from item import Shield
from scelta_classe import scegli_classe
from scelta_oggetto import scegli_oggetto
from scelta_razza import scegli_razza
from storia import avventura
import personaggio

numero_razza= int(input("1. Umano, 2. Nano, 3. Elfo, 4. Gnomo"))
numero_classe= int(input("1. Barbaro, 2. Paladino, 3. Ladro, 4. Mago"))
razza_scelta= scegli_razza(numero_razza)
classe_scelta= scegli_classe(numero_classe)
item= None
if numero_razza == 1:
    item= Weapon("Mazza", 10, 10)
if numero_razza == 2:
    item = Ranged_Weapon("Arco", 11, 12)
if numero_razza == 3:
    item = Armor("Antica", 10, 13)
if numero_razza == 4:
    item= Shield("Runico", 10, 12)
nome_personaggio= input("Dimmi il nome del tuo personaggio")
costo_vendita= int(random.uniform(1, 10))
personaggio_scelto= personaggio.Personaggio(nome_personaggio, razza_scelta, classe_scelta)
personaggio_scelto.equip_item(item)
print(personaggio_scelto)
while not personaggio_scelto.is_death():
    avventura(personaggio_scelto)

