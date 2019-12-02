maior = 0
menor = 0
for p in range(1,6):
    peso = float(input("O peso da {}ª pessoa: ".format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = peso
        if p < maior:
            menor = peso
print("O maior peso lido foi {}\n".format(maior))
print("O menor peso lido foi {}".format(menor))
