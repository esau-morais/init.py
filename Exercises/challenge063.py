def lin():
    print("-=" * 15)


lin()
print(" == Sequência de Fibonacci == ")
lin()

termos = int(input("Digite o número de termos que você deseja adicionar à sua SF: "))
f1 = 0
f2 = 1
print("= " * 33)
print(f"{f1} → {f2}", end="")
cont = 3
while cont <= termos:
    f3 = f1 + f2
    print(f" → {f3}",end="")
    f1 = f2
    f2 = f3
    cont += 1
print(" → FIM")
