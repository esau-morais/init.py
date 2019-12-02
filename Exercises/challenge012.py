p=float(input('Digite o preço do produto:'))
d= p * (5/100)
p2= p - d
print('O novo preço do produto, de valor {}, com 5% de desconto, será: {:.5} reais' .format (p,p2))
