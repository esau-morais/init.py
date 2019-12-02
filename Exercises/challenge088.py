import random, time

def lin():
    print("-=" * 13)


lin()
print(" == JOGO DA MEGA SENA == ")
lin()

listan = list()
jogos = list()

njog = int(input("Digite o número de jogadadas que você deseja: "))
tot = 1

time.sleep(0.5)
print(f" == SORTEANDO {njog} JOGADA(S) == ")

while tot <= njog:
    cont = 0
    while True:
        jog = random.randint(1,60)
        if jog not in listan:
            listan.append(jog)
            cont += 1
        if cont >= 6:
            break
    listan.sort()
    jogos.append(listan[:])
    listan.clear()
    tot += 1

for i, l in enumerate(jogos):
    print(f"Jogada {i + 1}: {l}")
    time.sleep(1.5)
