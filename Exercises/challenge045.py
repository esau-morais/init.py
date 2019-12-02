from random import randint
jogo = ("Pedra", "Papel", "Tesoura")
jog2 = randint(0, 2)
print("""
[0] Pedra
[1] Papel
[2] Tesoura""")
jog1 = int(input("Escolha sua jogada: "))
print("-=" * 10)
print("O jogador jogou {}".format(jogo[jog1]))
print("O computador jogou {}".format(jogo[jog2]))
print("-=" * 11)
if jog2 == 0:
    if jog1 == 0:
        print("EMPATE!")
    elif jog1 == 1:
        print("O jogador VENCEU!")
    elif jog1 == 2:
        print("O computado VENCEU!")
    else:
        print("Jogada INVÁLIDA. Tente novamente.")

elif jog2 == 1:
    if jog1 == 0:
        print("O computador VENCEU!")
    elif jog1 == 1:
        print("EMPATE!")
    elif jog1 == 2:
        print("O jogador VENCEU!")
    else:
        print("Jogada INVÁLIDA. Tente novamente.")

elif jog2 == 2:
    if jog1 == 0:
        print("O jogador VENCEU!")
    elif jog1 == 1:
        print("O computador VENCEU!")
    elif jog1 == 2:
        print("EMPATE!")
    else:
        print("Jogada INVÁLIDA. Tente novamente.")