import umano
import nano
import elfo
import gnomo

def scegli_razza(numero):
    razza = None
    if numero == 1:
        razza = umano.Umano()
    if numero == 2:
        razza = nano.Nano()
    if numero == 3:
        razza = elfo.Elfo()
    if numero == 4:
        razza = gnomo.Gnomo()
    if numero == 0 or numero > 4:
        print("Il numero della razza prescelta non esiste")
    return razza
