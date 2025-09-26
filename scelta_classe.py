import barbaro
import paladino
import ladro
import mago
def scegli_classe(numero):
    classe = None
    if numero == 1:
        classe= barbaro.Barbaro()
    if numero == 2:
        classe = paladino.Paladino()
    if numero == 3:
        classe = ladro.Ladro()
    if numero == 4:
        classe = mago.Mago()
    if numero == 0 or numero > 4:
        print("Il numero della classe prescelta non esiste")
    return classe