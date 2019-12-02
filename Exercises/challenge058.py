import random

jog = 0
num = random.randint(0,10)
correto = False
tent = 0

def lin():
    print("-=" * 10)
lin()
print("JOGO DA ADIVINHAÇÃO")
lin()

while not correto:
    jog = int(input("Tente adivinhar o número entre 0 e 10: "))
    tent += 1
    if jog == num:
        correto = True
    else:
        if jog > num:
            print("Tente um número MENOR ")
        elif jog < num:
            print('Tente um número MAIOR ')
print(f"Parabéns! Você conseguiu com {tent} tentativa(s)! O número escolhido pelo computador foi {num}")
