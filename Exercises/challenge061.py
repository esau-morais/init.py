def lin():
    print("-=" * 10)


lin()
print(" == Gerador de PA ==")
lin()

a1 = int(input("Digite o primeiro termo da sua PA: "))
r = int(input("Digite a razão da sua PA: "))
t = a1
cont = 1
pa = a1 + (10 - 1) * r
while cont <= 10:
    print(f"{t} → ", end="")
    t += r
    cont += 1
print("FIM")
