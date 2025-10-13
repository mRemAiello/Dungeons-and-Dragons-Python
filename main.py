from misc.create_character import create_new_character
from misc.create_character import create_new_random_character
from misc.create_character import create_new_random_enemy

# Player 1
name = input("Seleziona il nome del tuo personaggio ")
race_number = int(input("Seleziona una razza (0: Umano, 1: Elfo, 2: Nano, 3: Gnomo) "))
class_number = int(input("Seleziona una classe (0: Barbaro, 1: Bardo, 2: Mago, 3: Paladino, 4: Ladro) "))
player = create_new_character(name, race_number, class_number)

# Nemico
enemy = create_new_random_enemy("Bandito")

#
print(player)
print(enemy)

#
player.melee_attack(enemy)
player.melee_attack(enemy)
enemy.handle_attack(player)


# Loop di gameplay
"""comando = int(input("Quale comando vuoi eseguire? (0: Mostra statistiche, -1: Esci) "))
while not comando == -1:

    if comando == 0:
        print(player)
        print()

    # Richiedo comando
    comando = int(input("Quale comando vuoi eseguire? (-1: Esci)"))


# Chiusura programma
print("Gioco concluso, alla prossima!")"""