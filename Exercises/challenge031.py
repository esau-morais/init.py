d = float(input("Digite a distância da viagem, em km:"))
p = float(d * 0.50)
p2 = float(d * 0.45)
if d<=200:
    print("O preço da passagem será: {} reais.".format(p))
else:
    print("O preço da passagem será: {} reais.".format(p2))