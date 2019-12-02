preço = float(input("Digite o preço da compra: R$ "))
print("""Formas de pagamento: 
[1] À vista(dinheiro)/Cheque
[2] À vista (cartão)
[3] 2x no cartão
[4] 3x(ou mais) no cartão""")
opção = int(input("Digite a opção: "))
if opção == 1:
    d1 = float(preço - (10 / 100 * preço))
    print("O preço da compra será R${}".format(d1))
elif opção == 2:
    d2 = float(preço - (5 / 100 * preço))
    print("O preço da compra será R${}".format(d2))
elif opção == 3:
    c1 = float(preço)
    print("O preço da compra, dividida em 2x, será R${}".format(c1))
elif opção == 4:
    c2 = float(preço + (preço * 20 / 100))
    parcelas = int(input("Digite o número de parcelas:"))
    total = preço + (c2 / parcelas)
    print("O preço da compra, com juros de 20%, divida em {}x, será R${}".format(parcelas,total))