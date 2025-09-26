from dado import d6
from dado import d20
from dado import d10
from dado import d4
import random
from scelta_oggetto import scegli_oggetto
from creazione_mostro import crea_mostro


def avventura(personaggio_scelto):
    lancio= d6()
    if lancio == 1:
        lancia_osservare(personaggio_scelto)
    if lancio == 2:
        oggetto_random(personaggio_scelto)
    if lancio == 3:
        lancia_ascoltare(personaggio_scelto)
    if lancio == 4:
        incontro_boss(personaggio_scelto)
    if  4 < lancio < 7:
        incontro_boss(personaggio_scelto)

def lancia_osservare(personaggio_scelto):
    personaggio_scelto.osservare(d20())
    if personaggio_scelto.osservare(d20()):
        personaggio_scelto.guadagna_esperienza(1000)
        print("L'abilità è andata a buon fine e hai guadagnato 1000 exp")
        if not personaggio_scelto.osservare(d20()):
            print("L'abilità non è andata a buon fine")

def oggetto_random(personaggio_scelto):
    numero = int(random.uniform(1, 4))
    scegli_oggetto(numero)
    item = scegli_oggetto(numero)
    personaggio_scelto.add_item(item)

def lancia_ascoltare(personaggio_scelto):
    personaggio_scelto.ascoltare(d10())
    if personaggio_scelto.ascoltare(d10()):
        personaggio_scelto.guadagna_monete(10)
        print("L'abilità è andata a buon fine e hai guadagnato 10 monete")
    if not personaggio_scelto.ascoltare(d10()):
        print("L'abilità non è andata a buon fine")

def incontro_mostro(personaggio_scelto):
    print("Hai incontrato un mostro")
    mostro = crea_mostro("Obelix")
    lancio = d6()
    if lancio == 1:
        print("Scappa")
    if 2 <= lancio <= 4:
        print("Il tuo personaggio attacca")
        personaggio_scelto.attacco_ravvicinato(mostro)
        personaggio_scelto.attacco_a_distanza(mostro)
    if lancio > 4:
        print("Il mostro attacca il tuo personaggio")
        mostro.attacco_ravvicinato(personaggio_scelto)
        mostro.attacco_a_distanza(personaggio_scelto)

def incontro_boss(personaggio_scelto):
    print("Hai incontrato un boss")
    mostro = crea_mostro("Gandalf")
    mostro.guadagna_esperienza(20000)
    lancio = d4()
    if 1 <= lancio <= 3:
        print("Scappa")
    if lancio == 4:
        print("Combattete")
        personaggio_scelto.attacco_ravvicinato(mostro)
        personaggio_scelto.attacco_a_distanza(mostro)
        mostro.attacco_ravvicinato(personaggio_scelto)
        mostro.attacco_a_distanza(personaggio_scelto)