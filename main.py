from misc.create_character import create_new_character
from misc.create_character import create_new_random_character
from misc.create_character import create_new_random_enemy
from spells.spell_damage import SpellDamage
from spells.spell_heal import SpellHeal
from spells.spell_bonus_ca import SpellBonusCA

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

spell = SpellDamage("Dardo Incantato (Mitico)", 1, "", "Invocazione", 1, 4, 2)
spell.launch(player, enemy)
spell.launch(player, enemy)

spell2 = SpellHeal("Cura Ferite Gravi", 1, "", "Invocazione", 1, 5, 8, 1)
spell2.launch(player, enemy)

spell3 = SpellBonusCA("Armatura Magica", 1, "", "Evocazione (Forza)", 4)
spell3.launch(player, player)

print(player)

print()
print()

print(enemy)

#
"""player.melee_attack(enemy)
player.melee_attack(enemy)
enemy.handle_attack(player)
"""

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