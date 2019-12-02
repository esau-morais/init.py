def lin():
    print("-=" * 12)


def lin2():
    print("= " * 24)


lin()
print(" == CAIXA ELETRÔNICO == ")
lin()

num = int(input("Digite o valor (inteiro) a ser sacado: R$ "))
total = num
ced = 50
nced = 0
lin2()
while True:
    if total >= ced:
        total -= ced
        nced += 1
    else:
        print(f"Total de {nced} nota(s) de R$ {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        nced = 0
        if total == 0:
            break
