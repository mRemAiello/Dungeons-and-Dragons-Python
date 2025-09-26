import item
import random

lista_ogg_Weapon=[item.Weapon("Spada",10, 6), item.Weapon("Ascia", 8, 10)]
lista_ogg_Ranged_Weapon= [item.Ranged_Weapon("Balestra", 15, 12), item.Ranged_Weapon("Fionda", 4, 3)]
lista_ogg_Armor= [item.Armor("Armatura di cuoio", 18, 12), item.Armor("Armatura a scaglie", 22, 15)]
lista_ogg_Shield = [item.Shield("Scudo rotondo", 11, 8), item.Shield("Scudo torre", 12, 10)]

def scegli_oggetto(numero):
    ogg = None
    if numero == 1:
        ogg= random.choice(lista_ogg_Weapon)
    if numero == 2:
        ogg= random.choice(lista_ogg_Ranged_Weapon)
    if numero == 3:
        ogg= random.choice(lista_ogg_Armor)
    if numero == 4:
        ogg= random.choice(lista_ogg_Shield)
    if numero == 0 or numero > 4:
        print("Il numero dell'oggetto prescelto non esiste")
    return ogg
