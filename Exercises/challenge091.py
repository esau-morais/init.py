from random import randint
from time import sleep
from operator import itemgetter

def line():
    print("-=" * 14)

line()
print(" == DICE GAMES ON PYTHON == ")
line()

players = {"Player 1": randint(1,6), "Player 2": randint(1,6), "Player 3": randint(1,6), 
"Player 4": randint(1,6)}

order = dict()

sleep(1.0)

for p, v in players.items():
    print(f"{p} receab {v}")
    sleep(1.0)

order = sorted(players.items(), key=itemgetter(1), reverse=True)

line()
print("      == POSITION == ")
line()

for p, v in enumerate(order):
    print(f"Position {p + 1}: {v[0]} with {v[1]}")

line()
