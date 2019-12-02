def lin():
    print("-=" * 13)


def lin2():
    print("= " * 18)

lin()
print(" == COMERCIAL CARVALHO == ")
lin()

prod = " "
prec = total = 0
resp = " "

while True:
    prod = str(input("Digite o nome do Produto: "))
    lin2()
    prec = float(input("Digite o preço do Produto: R$  "))
    lin2()
    resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    lin2()
    total += prec
    if resp == "N":
        break
print(f"O valor da sua compra deu R$ {total}. Muito obrigado! Volte sempre!")
