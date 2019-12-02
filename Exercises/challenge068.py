import random
def lin():
    print("-=" * 10)
def lin2():
    print("-=" * 26)


lin()
print(" == PAR OU ÍMPAR == ")
lin()
v = 0

while True:
    jog = int(input("Digite um valor: "))
    comp = random.randint(0,11)
    total = jog + comp
    pi = " "
    while pi not in "PpIi":
        pi = str(input("Par ou Ímpar: [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jog} e o computador {comp} → Total de {total}")
    if pi == "P":
        if total % 2 == 0:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU.")
            break
    elif pi == "I":
        if total % 2 == 1:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU.")
            break
        print("Vamos jogar NOVAMENTE...")
print(f"GAME OVER! Você venceu {v} veze(s).")
 